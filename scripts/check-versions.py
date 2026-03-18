#!/usr/bin/env python3
"""check-versions.py — compare package versions in ch03-packages.md against upstream.

Usage:
    python3 scripts/check-versions.py [options] [PACKAGE ...]

Options:
    -u, --update   Rewrite outdated versions in ch03-packages.md in-place.
    -j, --json     Output results as JSON instead of a table.
    -q, --quiet    Only print outdated packages.
    PACKAGE        Limit check to specific package name(s) (case-insensitive).
                   If omitted, all known packages are checked.

Exit codes:
    0   All checked packages are current (or upstream unknown).
    1   One or more packages have a newer upstream version.
    2   Usage error.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

PACKAGES_FILE = (
    Path(__file__).resolve().parent.parent
    / "book" / "part1-preparations" / "ch03-packages.md"
)
TIMEOUT = 15
MAX_WORKERS = 8
UA = "lfs-multiarch-version-check/1.0 (+https://github.com/ChaseKnowlden/lfs-multiarch)"

# ---------------------------------------------------------------------------
# .env loader — stdlib only, no python-dotenv required
# ---------------------------------------------------------------------------
def _load_dotenv():
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:   # don't override real env vars
            os.environ[key] = value

_load_dotenv()

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
_GITHUB_HOSTS = ("api.github.com")

# ---------------------------------------------------------------------------
# Terminal colours (disabled when stdout is not a TTY)
# ---------------------------------------------------------------------------
def _c(code):
    return f"\033[{code}m" if sys.stdout.isatty() else ""

RED    = _c("31"); GREEN = _c("32"); YELLOW = _c("33")
CYAN   = _c("36"); BOLD  = _c("1");  RESET  = _c("0")

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------
def fetch(url, *, retries=3):
    headers = {"User-Agent": UA, "Accept": "application/json, text/html, */*"}
    if GITHUB_TOKEN and _GITHUB_HOSTS in url:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.read().decode(errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 429:
                wait = int(e.headers.get("Retry-After", 10 * (attempt + 1)))
                time.sleep(wait)
                continue
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    return None


def fetch_json(url):
    raw = fetch(url)
    return json.loads(raw) if raw else None

# ---------------------------------------------------------------------------
# Version helpers
# ---------------------------------------------------------------------------
_PRE_RE = re.compile(r"(alpha|beta|rc\d*|pre|dev|\.post\d+|-rc\d*|-beta|-alpha)", re.I)


def is_prerelease(v):
    return bool(_PRE_RE.search(str(v)))


def version_tuple(v):
    """'1.2.3' → (1, 2, 3) for numeric comparison."""
    v = re.sub(r"^[vV]", "", str(v).strip())
    result = []
    for part in re.split(r"[._-]", v):
        try:
            result.append(int(part))
        except ValueError:
            result.append(part)
    return tuple(result)


def newer(latest, current):
    try:
        return version_tuple(latest) > version_tuple(current)
    except Exception:
        return str(latest).strip() != str(current).strip()

# ---------------------------------------------------------------------------
# Upstream checkers
# ---------------------------------------------------------------------------
class _HrefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.links.append(v)


def _ftp_dir_versions(url, pat):
    """Parse an FTP/HTTP directory listing and return all matching versions."""
    html = fetch(url)
    if not html:
        return []
    p = _HrefParser()
    p.feed(html)
    compiled = re.compile(pat)
    versions = []
    for link in p.links:
        m = compiled.search(link)
        if m and not is_prerelease(m.group(1)):
            versions.append(m.group(1))
    return versions


def check_gcc():
    # After GCC 3.3.2, releases are placed in per-version subdirectories
    # (e.g. ftp.gnu.org/gnu/gcc/gcc-14.2.0/) rather than as tarballs in
    # the top-level directory.
    html = fetch("https://ftp.gnu.org/gnu/gcc/")
    if not html:
        return None
    versions = [
        m.group(1)
        for m in re.finditer(r'href="gcc-([\d.]+)/"', html)
        if not is_prerelease(m.group(1))
    ]
    return max(versions, key=version_tuple) if versions else None


def check_gnu(pkg):
    versions = _ftp_dir_versions(
        f"https://ftp.gnu.org/gnu/{pkg}/",
        rf"{re.escape(pkg)}-(\d[\d.]+)\.tar",
    )
    return max(versions, key=version_tuple) if versions else None


def check_github_release(owner, repo):
    data = fetch_json(f"https://api.github.com/repos/{owner}/{repo}/releases")
    if not data:
        return None
    for rel in data:
        if rel.get("draft") or rel.get("prerelease"):
            continue
        tag = rel.get("tag_name", "")
        ver = re.sub(r"^[vV]", "", tag)
        if ver and not is_prerelease(ver):
            return ver
    return None


def check_github_tag(owner, repo, pat=r"(\d+\.\d+(?:\.\d+)*)"):
    data = fetch_json(f"https://api.github.com/repos/{owner}/{repo}/tags?per_page=30")
    if not data:
        return None
    compiled = re.compile(pat)
    versions = []
    for tag in data:
        m = compiled.search(tag.get("name", ""))
        if m and not is_prerelease(m.group(1)):
            versions.append(m.group(1))
    return max(versions, key=version_tuple) if versions else None


def check_gitlab_release(namespace, project):
    encoded = urllib.parse.quote(f"{namespace}/{project}", safe="")
    data = fetch_json(f"https://gitlab.com/api/v4/projects/{encoded}/releases")
    if not data:
        return None
    for rel in data:
        tag = rel.get("tag_name", "")
        ver = re.sub(r"^[vV]", "", tag)
        if ver and not is_prerelease(ver):
            return ver
    return None


def check_pypi(pkg):
    data = fetch_json(f"https://pypi.org/pypi/{pkg}/json")
    return data["info"]["version"] if data else None


def check_kernel_org(subpath, name_pat):
    html = fetch(f"https://www.kernel.org/pub/{subpath}")
    if not html:
        return None
    versions = [
        m.group(1) for m in re.finditer(name_pat, html)
        if not is_prerelease(m.group(1))
    ]
    return max(versions, key=version_tuple) if versions else None


def check_linux_kernel():
    data = fetch_json("https://www.kernel.org/releases.json")
    if not data:
        return None
    for rel in data.get("releases", []):
        if rel.get("moniker") == "stable":
            ver = rel.get("version", "")
            if ver and not is_prerelease(ver):
                return ver
    return None


def check_openssl():
    data = fetch_json("https://api.github.com/repos/openssl/openssl/releases")
    if not data:
        return None
    for rel in data:
        if rel.get("draft") or rel.get("prerelease"):
            continue
        tag = rel.get("tag_name", "")
        m = re.search(r"openssl[_-](\d[\d._]+)", tag, re.I)
        if m:
            ver = m.group(1).replace("_", ".")
            if not is_prerelease(ver):
                return ver
    return None


def check_perl():
    data = fetch_json(
        "https://fastapi.metacpan.org/v1/release/latest_by_distribution/perl"
    )
    if data:
        ver = data.get("version", "")
        if ver and not is_prerelease(ver):
            return ver
    return check_github_tag("Perl", "perl5", r"v(\d+\.\d+\.\d+)")


def check_xml_parser():
    data = fetch_json(
        "https://fastapi.metacpan.org/v1/release/latest_by_distribution/XML-Parser"
    )
    if data:
        return data.get("version")
    return None


def check_python():
    data = fetch_json(
        "https://www.python.org/api/v2/downloads/release/"
        "?is_published=true&pre_release=false&limit=20"
    )
    if isinstance(data, dict):
        data = data.get("results", [])
    if data:
        versions = []
        for r in data:
            # 'version' is a numeric release ID; the version string is in 'name'
            # e.g. {"name": "Python 3.12.5", "version": 100, ...}
            name = r.get("name", "") if isinstance(r, dict) else ""
            m = re.search(r"(\d+\.\d+\.\d+)", name)
            if m and not is_prerelease(m.group(1)):
                versions.append(m.group(1))
        if versions:
            return max(versions, key=version_tuple)
    return check_github_release("python", "cpython")


def check_sqlite():
    html = fetch("https://www.sqlite.org/download.html")
    if not html:
        return None
    m = re.search(r"sqlite-autoconf-(\d{7})\.tar", html)
    if not m:
        return None
    raw = m.group(1)          # e.g. 3470100 → 3.47.1
    major = raw[0]
    minor = str(int(raw[1:4]))
    patch = str(int(raw[4:6]))
    return f"{major}.{minor}.{patch}"


def check_tcl():
    # LFS tracks the 8.6 branch; ignore 9.x releases.
    # SourceForge RSS lists all releases; filter to 8.6.x explicitly.
    rss = fetch("https://sourceforge.net/projects/tcl/rss?path=/Tcl")
    if rss:
        versions = [
            m.group(1)
            for m in re.finditer(r"/Tcl/(8\.6\.\d+)/", rss)
            if not is_prerelease(m.group(1))
        ]
        if versions:
            return max(versions, key=version_tuple)
    return None


def check_sourceforge(project, path):
    # Use the SourceForge RSS feed for a given file path to extract versions.
    rss = fetch(f"https://sourceforge.net/projects/{project}/rss?path=/{path}")
    if not rss:
        return None
    versions = [
        m.group(1)
        for m in re.finditer(rf"{re.escape(path)}/([\d.]+)/", rss)
        if not is_prerelease(m.group(1))
    ]
    return max(versions, key=version_tuple) if versions else None


def check_launchpad(project):
    data = fetch_json(f"https://api.launchpad.net/1.0/{project}/releases")
    if not data:
        return None
    versions = [
        e["version"]
        for e in data.get("entries", [])
        if e.get("version") and not is_prerelease(e["version"])
    ]
    return max(versions, key=version_tuple) if versions else None


def check_less():
    html = fetch("https://www.greenwoodsoftware.com/less/")
    if html:
        m = re.search(r"less-(\d+)\.tar", html)
        if m:
            return m.group(1)
    return None


def check_zlib():
    # zlib.net removes old download links when a new version ships;
    # the fossils directory lists all historical tarballs and is stable.
    html = fetch("https://zlib.net/fossils/")
    if not html:
        return None
    versions = [
        m.group(1)
        for m in re.finditer(r"zlib-([\d.]+)\.tar", html)
        if not is_prerelease(m.group(1))
    ]
    return max(versions, key=version_tuple) if versions else None


def check_bzip2():
    html = fetch("https://sourceware.org/pub/bzip2/")
    if not html:
        return None
    versions = [
        m.group(1)
        for m in re.finditer(r"bzip2-([\d.]+)\.tar", html)
        if not is_prerelease(m.group(1))
    ]
    return max(versions, key=version_tuple) if versions else None


def check_elfutils():
    html = fetch("https://sourceware.org/elfutils/ftp/")
    if not html:
        return None
    versions = [
        m.group(1)
        for m in re.finditer(r'href="(\d[\d.]+)/"', html)
        if not is_prerelease(m.group(1))
    ]
    return max(versions, key=version_tuple) if versions else None


def check_vim():
    return check_github_tag("vim", "vim", r"v(\d+\.\d+\.\d+)")


def check_expat():
    # Expat tags: R_2_6_2 → 2.6.2
    data = fetch_json("https://api.github.com/repos/libexpat/libexpat/releases")
    if not data:
        return None
    for rel in data:
        if rel.get("draft") or rel.get("prerelease"):
            continue
        tag = rel.get("tag_name", "")
        m = re.match(r"R_(\d+)_(\d+)_(\d+)", tag)
        if m:
            return f"{m.group(1)}.{m.group(2)}.{m.group(3)}"
    return None


def check_iana_etc():
    # Tags are plain dates: 20240806
    return check_github_tag("Mic92", "iana-etc", r"(\d{8})")


def check_udev():
    # We ship just the udev portion of systemd; track systemd's stable releases.
    data = fetch_json("https://api.github.com/repos/systemd/systemd/releases")
    if not data:
        return None
    for rel in data:
        if rel.get("draft") or rel.get("prerelease"):
            continue
        tag = rel.get("tag_name", "")
        ver = re.sub(r"^[vV]", "", tag)
        if ver and not is_prerelease(ver):
            return ver
    return None


# ---------------------------------------------------------------------------
# Master package → checker mapping
# ---------------------------------------------------------------------------
import urllib.parse  # noqa: E402 (imported here to keep grouping logical)

CHECKERS = {
    "Acl":            lambda: check_kernel_org(
                          "linux/libs/security/linux-privs/libacl1/",
                          r"acl-([\d.]+)\.tar"),
    "Attr":           lambda: check_kernel_org(
                          "linux/libs/security/linux-privs/libattr1/",
                          r"attr-([\d.]+)\.tar"),
    "Autoconf":       lambda: check_gnu("autoconf"),
    "Automake":       lambda: check_gnu("automake"),
    "Bash":           lambda: check_gnu("bash"),
    "Bc":             lambda: check_github_release("gavinhoward", "bc"),
    "Binutils":       lambda: check_gnu("binutils"),
    "Bison":          lambda: check_gnu("bison"),
    "Bzip2":          lambda: check_bzip2(),
    "Coreutils":      lambda: check_gnu("coreutils"),
    "DejaGNU":        lambda: check_gnu("dejagnu"),
    "Diffutils":      lambda: check_gnu("diffutils"),
    "E2fsprogs":      lambda: check_github_release("tytso", "e2fsprogs"),
    "Elfutils":       lambda: check_elfutils(),
    "Expat":          lambda: check_expat(),
    "Expect":         lambda: check_sourceforge("expect", "Expect"),
    "File":           lambda: check_github_release("file", "file"),
    "Findutils":      lambda: check_gnu("findutils"),
    "Flex":           lambda: check_github_release("westes", "flex"),
    "Flit-core":      lambda: check_pypi("flit_core"),
    "Gawk":           lambda: check_gnu("gawk"),
    "GCC":            lambda: check_gcc(),
    "GDBM":           lambda: check_gnu("gdbm"),
    "Gettext":        lambda: check_gnu("gettext"),
    "Glibc":          lambda: check_gnu("libc"),
    "GMP":            lambda: check_gnu("gmp"),
    "Gperf":          lambda: check_gnu("gperf"),
    "Grep":           lambda: check_gnu("grep"),
    "Groff":          lambda: check_gnu("groff"),
    "GRUB":           lambda: check_gnu("grub"),
    "Gzip":           lambda: check_gnu("gzip"),
    "Iana-Etc":       lambda: check_iana_etc(),
    "Inetutils":      lambda: check_gnu("inetutils"),
    "Intltool":       lambda: check_launchpad("intltool"),
    "IPRoute2":       lambda: check_kernel_org(
                          "linux/utils/net/iproute2/",
                          r"iproute2-([\d.]+)\.tar"),
    "Jinja2":         lambda: check_pypi("Jinja2"),
    "Kbd":            lambda: check_kernel_org(
                          "linux/utils/kbd/",
                          r"kbd-([\d.]+)\.tar"),
    "Kmod":           lambda: check_kernel_org(
                          "linux/utils/kernel/kmod/",
                          r"kmod-([\d.]+)\.tar"),
    "Less":           lambda: check_less(),
    "Libcap":         lambda: check_kernel_org(
                          "linux/libs/security/linux-privs/libcap2/",
                          r"libcap-([\d.]+)\.tar"),
    "Libffi":         lambda: check_github_release("libffi", "libffi"),
    "Libpipeline":    lambda: check_gnu("libpipeline"),
    "Libtool":        lambda: check_gnu("libtool"),
    "Libxcrypt":      lambda: check_github_release("besser82", "libxcrypt"),
    "Linux kernel":   lambda: check_linux_kernel(),
    "LZ4":            lambda: check_github_release("lz4", "lz4"),
    "M4":             lambda: check_gnu("m4"),
    "Make":           lambda: check_gnu("make"),
    "Man-DB":         lambda: check_gnu("man-db"),
    "Man-Pages":      lambda: check_kernel_org(
                          "linux/docs/man-pages/",
                          r"man-pages-([\d.]+)\.tar"),
    "MarkupSafe":     lambda: check_pypi("MarkupSafe"),
    "Meson":          lambda: check_pypi("meson"),
    "MPC":            lambda: check_gnu("mpc"),
    "MPFR":           lambda: check_gnu("mpfr"),
    "Ncurses":        lambda: check_gnu("ncurses"),
    "Ninja":          lambda: check_github_release("ninja-build", "ninja"),
    "OpenSSL":        lambda: check_openssl(),
    "packaging":      lambda: check_pypi("packaging"),
    "Patch":          lambda: check_gnu("patch"),
    "PCRE2":          lambda: check_github_release("PCRE2Project", "pcre2"),
    "Perl":           lambda: check_perl(),
    "Pkgconf":        lambda: check_github_release("pkgconf", "pkgconf"),
    "Procps-ng":      lambda: check_gitlab_release("procps-ng", "procps"),
    "Psmisc":         lambda: check_gitlab_release("psmisc", "psmisc"),
    "Python":         lambda: check_python(),
    "Readline":       lambda: check_gnu("readline"),
    "Sed":            lambda: check_gnu("sed"),
    "Setuptools":     lambda: check_pypi("setuptools"),
    "Shadow":         lambda: check_github_release("shadow-maint", "shadow"),
    "SQLite":         lambda: check_sqlite(),
    "Sysklogd":       lambda: check_github_release("troglobit", "sysklogd"),
    "Sysvinit":       lambda: check_github_release("slicer69", "sysvinit"),
    "Tar":            lambda: check_gnu("tar"),
    "Tcl":            lambda: check_tcl(),
    "Texinfo":        lambda: check_gnu("texinfo"),
    "Udev (systemd)": lambda: check_udev(),
    "Util-linux":     lambda: check_kernel_org(
                          "linux/utils/util-linux/",
                          r"util-linux-([\d.]+)\.tar"),
    "Vim":            lambda: check_vim(),
    "Wheel":          lambda: check_pypi("wheel"),
    "XML::Parser":    lambda: check_xml_parser(),
    "Xz":             lambda: check_github_release("tukaani-project", "xz"),
    "Zlib":           lambda: check_zlib(),
    "Zstd":           lambda: check_github_release("facebook", "zstd"),
}

# ---------------------------------------------------------------------------
# Parse / update ch03-packages.md
# ---------------------------------------------------------------------------
_ROW_RE = re.compile(
    r"^\|\s*(?P<pkg>[^|]+?)\s*\|\s*(?P<ver>\S+)\s*\|(?P<rest>.*)$"
)


def parse_book_versions():
    """Return dict of {package_name: version} from the markdown table."""
    versions = {}
    for line in PACKAGES_FILE.read_text().splitlines():
        m = _ROW_RE.match(line)
        if m and m.group("ver")[0].isdigit():
            versions[m.group("pkg")] = m.group("ver")
    return versions


def update_book_version(pkg, new_ver):
    """Rewrite the version cell for *pkg* in ch03-packages.md."""
    text = PACKAGES_FILE.read_text()
    # Match the table row for this exact package name
    pat = re.compile(
        rf"^(\|\s*{re.escape(pkg)}\s*\|)\s*\S+(\s*\|)",
        re.MULTILINE,
    )
    new_text, n = pat.subn(rf"\g<1> {new_ver}\2", text)
    if n:
        PACKAGES_FILE.write_text(new_text)
    return n > 0

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
STATUS_OUTDATED = "OUTDATED"
STATUS_CURRENT  = "current"
STATUS_UNKNOWN  = "unknown"


def check_one(pkg, current):
    checker = CHECKERS.get(pkg)
    if checker is None:
        return pkg, current, None, STATUS_UNKNOWN
    try:
        latest = checker()
    except Exception as exc:
        return pkg, current, None, f"error: {exc}"
    if latest is None:
        return pkg, current, None, STATUS_UNKNOWN
    latest = str(latest).strip()
    if not latest:
        return pkg, current, None, STATUS_UNKNOWN
    status = STATUS_OUTDATED if newer(latest, current) else STATUS_CURRENT
    return pkg, current, latest, status


def main():
    ap = argparse.ArgumentParser(
        description="Check package versions against upstream.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("packages", nargs="*", metavar="PACKAGE",
                    help="Package name(s) to check (default: all).")
    ap.add_argument("-u", "--update", action="store_true",
                    help="Rewrite outdated versions in ch03-packages.md.")
    ap.add_argument("-j", "--json", dest="json_out", action="store_true",
                    help="Output JSON instead of a table.")
    ap.add_argument("-q", "--quiet", action="store_true",
                    help="Only print outdated packages.")
    args = ap.parse_args()

    book_versions = parse_book_versions()

    # Determine which packages to check
    if args.packages:
        lookup = {k.lower(): k for k in book_versions}
        targets = {}
        for name in args.packages:
            key = lookup.get(name.lower())
            if key:
                targets[key] = book_versions[key]
            else:
                print(f"Warning: '{name}' not found in packages file.", file=sys.stderr)
        if not targets:
            ap.error("No valid package names supplied.")
    else:
        targets = book_versions

    print(f"Checking {len(targets)} package(s) with up to {MAX_WORKERS} parallel workers…\n",
          file=sys.stderr)

    results = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {
            pool.submit(check_one, pkg, ver): pkg
            for pkg, ver in targets.items()
        }
        for fut in as_completed(futures):
            pkg, current, latest, status = fut.result()
            results[pkg] = (current, latest, status)
            # Live progress to stderr
            sym = {"current": ".", STATUS_OUTDATED: "!", "unknown": "?"}.get(status, "E")
            print(sym, end="", flush=True, file=sys.stderr)
    print(file=sys.stderr)

    # --json output
    if args.json_out:
        out = [
            {"package": pkg, "current": cur, "latest": lat, "status": st}
            for pkg, (cur, lat, st) in sorted(results.items())
        ]
        print(json.dumps(out, indent=2))
        return 1 if any(v[2] == STATUS_OUTDATED for v in results.values()) else 0

    # Table output
    col_pkg = max(len(p) for p in results) + 2
    col_cur = max(len(v[0]) for v in results.values()) + 2
    col_lat = max((len(v[1]) if v[1] else 7) for v in results.values()) + 2

    header = (
        f"{'Package':<{col_pkg}}  {'Current':<{col_cur}}  {'Latest':<{col_lat}}  Status"
    )
    print(BOLD + header + RESET)
    print("-" * len(header))

    outdated = []
    for pkg in sorted(results):
        current, latest, status = results[pkg]
        if args.quiet and status != STATUS_OUTDATED:
            continue
        latest_str = latest if latest else "-"
        if status == STATUS_OUTDATED:
            colour = RED
            outdated.append((pkg, current, latest))
        elif status == STATUS_CURRENT:
            colour = GREEN
        else:
            colour = YELLOW
        print(
            f"{colour}{pkg:<{col_pkg}}  {current:<{col_cur}}  "
            f"{latest_str:<{col_lat}}  {status}{RESET}"
        )

    print()
    total   = len(results)
    n_out   = sum(1 for v in results.values() if v[2] == STATUS_OUTDATED)
    n_cur   = sum(1 for v in results.values() if v[2] == STATUS_CURRENT)
    n_unk   = total - n_out - n_cur
    print(f"Summary: {total} packages — "
          f"{GREEN}{n_cur} current{RESET}, "
          f"{RED}{n_out} outdated{RESET}, "
          f"{YELLOW}{n_unk} unknown{RESET}")

    if outdated and args.update:
        print()
        updated = []
        for pkg, old, new in outdated:
            if update_book_version(pkg, new):
                print(f"  Updated {pkg}: {old} → {new}")
                updated.append(pkg)
            else:
                print(f"  Could not update {pkg} in {PACKAGES_FILE.name}", file=sys.stderr)
        if updated:
            print(f"\n{len(updated)} package(s) updated in {PACKAGES_FILE.name}.")

    return 1 if outdated else 0


if __name__ == "__main__":
    sys.exit(main())
