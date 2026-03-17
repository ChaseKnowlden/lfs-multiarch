# LFS Multi-Arch Book — ROADMAP

A community-driven Linux From Scratch book targeting 14 architectures:
**alpha, amd64, arm, arm64, hppa, loong, m68k, mips, ppc, ppc64, riscv, s390, sparc, x86**

---

## Milestone 0 — Project Bootstrap *(current)*

- [x] Define target architecture list
- [x] Establish book structure and tooling
- [x] Set up XML/DocBook or Markdown source format decision (Markdown + mdBook)
- [x] Write contributor guidelines (`CONTRIBUTING.md`)
- [x] Set up CI skeleton (build-test, spell-check, link-check)
- [x] Write this ROADMAP

---

## Milestone 1 — Architecture Baseline Research

For each of the 14 target architectures, document:

- [ ] Toolchain triplet (e.g. `aarch64-lfs-linux-gnu`)
- [ ] Kernel architecture name and `ARCH=` make variable
- [ ] Default page size and endianness
- [ ] ABI variants (soft-float, hard-float, multilib, ILP32/LP64, etc.)
- [ ] Minimum host toolchain versions known to work
- [ ] Status: *Tier 1* (well-tested), *Tier 2* (builds, limited testing), *Tier 3* (experimental)

**Architectures and initial tier assignments:**

| Arch   | Triplet (example)                  | Endian  | Bits | Tier |
|--------|------------------------------------|---------|------|------|
| alpha  | `alpha-lfs-linux-gnu`              | little  | 64   | 3    |
| amd64  | `x86_64-lfs-linux-gnu`             | little  | 64   | 1    |
| arm    | `arm-lfs-linux-gnueabihf`          | little  | 32   | 2    |
| arm64  | `aarch64-lfs-linux-gnu`            | little  | 64   | 1    |
| hppa   | `hppa-lfs-linux-gnu`               | big     | 32   | 3    |
| loong  | `loongarch64-lfs-linux-gnu`        | little  | 64   | 2    |
| m68k   | `m68k-lfs-linux-gnu`               | big     | 32   | 3    |
| mips   | `mips-lfs-linux-gnu` / `mipsel-…`  | bi      | 32   | 2    |
| ppc    | `powerpc-lfs-linux-gnu`            | big     | 32   | 2    |
| ppc64  | `powerpc64le-lfs-linux-gnu`        | bi      | 64   | 2    |
| riscv  | `riscv64-lfs-linux-gnu`            | little  | 64   | 2    |
| s390   | `s390x-lfs-linux-gnu`              | big     | 64   | 3    |
| sparc  | `sparc64-lfs-linux-gnu`            | big     | 64   | 3    |
| x86    | `i686-lfs-linux-gnu`               | little  | 32   | 1    |

---

## Milestone 2 — Book Skeleton (Architecture-Agnostic Core)

Write the chapters that apply to all architectures, using `@@ARCH@@`-style
substitution variables where arch-specific values differ.

- [ ] **Prologue** — Introduction, prerequisites, how to read this book
- [ ] **Part I — Preparations**
  - [ ] Ch 1: Introduction & host system requirements
  - [ ] Ch 2: Preparing the build partition
  - [ ] Ch 3: Packages and patches list (arch-annotated)
  - [ ] Ch 4: Final preparations (env vars, `$LFS`, `$LFS_TGT`, etc.)
- [ ] **Part II — Cross-Compilation Toolchain**
  - [ ] Ch 5: Binutils pass 1
  - [ ] Ch 6: GCC pass 1
  - [ ] Ch 7: Linux API headers
  - [ ] Ch 8: Glibc
  - [ ] Ch 9: Libstdc++ (pass 1)
- [ ] **Part III — Cross-Compiling Temporary Tools**
  - [ ] M4, Ncurses, Bash, Coreutils, Diffutils, File, Findutils,
          Gawk, Grep, Gzip, Make, Patch, Sed, Tar, Xz, Binutils pass 2,
          GCC pass 2
- [ ] **Part IV — Building the LFS System**
  - [ ] Glibc, Zlib, Bzip2, Xz, Zstd, File, Readline, M4, Bc, Flex,
          Tcl, Expect, DejaGNU, Binutils, GMP, MPFR, MPC, Attr, Acl,
          Libcap, Shadow, GCC, Pkg-config, Ncurses, Sed, Psmisc, Gettext,
          Bison, Grep, Bash, Libtool, GDBM, Gperf, Expat, Inetutils,
          Less, Perl, XML::Parser, Intltool, Autoconf, Automake, OpenSSL,
          Kmod, Elfutils, Libffi, Python, Flit-core, Wheel, Setuptools,
          Ninja, Meson, Coreutils, Check, Diffutils, Gawk, Findutils,
          Groff, GRUB (arch-varies), Gzip, IPRoute2, Kbd, Libpipeline,
          Make, Patch, Tar, Texinfo, Vim, MarkupSafe, Jinja2, Udev,
          Man-DB, Procps, Util-linux, E2fsprogs
- [ ] **Part V — System Configuration**
  - [ ] LFS-Bootscripts, network, locale, /etc/fstab, kernel config
  - [ ] Bootloader configuration (arch-varies: GRUB/EFI, GRUB/BIOS,
          yaboot, SILO, ELILO, OpenFirmware, IPL, SBL, etc.)
- [ ] **Appendices** — Acronyms, acknowledgements, dependencies, version-check script

---

## Milestone 3 — Per-Architecture Chapters

For each architecture write or verify arch-specific sections:

- [ ] **alpha** — SRM bootloader, `aboot`, GCC `-mieee` flag considerations
- [ ] **amd64** — GRUB EFI + BIOS, UEFI Secure Boot notes
- [ ] **arm** — Device Tree, U-Boot, `armhf` vs `armel` ABI, GRUB on EFI boards
- [ ] **arm64** — GRUB EFI, U-Boot, `ILP32` variant note
- [ ] **hppa** — PALO bootloader, 32/64-bit kernel on 32-bit userland
- [ ] **loong** — GRUB EFI (UEFI), LoongArch ABI notes, glibc loong patches
- [ ] **m68k** — Atari/Amiga/VME/Q40 sub-architectures, `amiboot`/`atari-bootstrap`
- [ ] **mips** — LE vs BE, O32/N32/N64 ABI, YAMON/U-Boot/CFE bootloaders
- [ ] **ppc** — `powerpc` 32-bit, Yaboot / GRUB-IEEE1275, G3/G4 notes
- [ ] **ppc64** — ELFv2 ABI (`ppc64le`) vs ELFv1 (`ppc64` BE), OPAL/GRUB
- [ ] **riscv** — `rv64gc` baseline, OpenSBI + U-Boot, GRUB EFI
- [ ] **s390** — `s390x`, z/VM vs LPAR, zipl bootloader, DASD storage
- [ ] **sparc** — `sparc64`, SILO bootloader, OpenBoot PROM
- [ ] **x86** — 32-bit (`i686`), GRUB BIOS, PAE kernel note

---

## Milestone 4 — Package Version Tracking & Patch Management

- [ ] Central `packages.ent` (or YAML/TOML) listing package versions + checksums
- [ ] Per-arch patch sets in `patches/<arch>/`
- [ ] Upstream patch tracking policy (how to update, who reviews)
- [ ] Automated fetch+verify script (`scripts/fetch-packages.sh`)

---

## Milestone 5 — Build Automation & Testing

- [ ] `scripts/build-cross-toolchain.sh` — parameterised by `$LFS_ARCH`
- [ ] `scripts/build-system.sh` — full system build driver
- [ ] QEMU-based smoke test matrix (emulate all 14 arches)
- [ ] CI pipeline (GitHub Actions or similar):
  - Lint / spell-check book sources on every PR
  - Build-test Tier-1 arches on every merge to `main`
  - Build-test Tier-2 arches weekly
  - Build-test Tier-3 arches monthly (or on-demand)
- [ ] Test checklist: system boots, `uname -m` correct, basic commands work

---

## Milestone 6 — Book Rendering & Publishing

- [ ] Choose final source format (DocBook XML preferred for LFS tradition, or AsciiDoc)
- [ ] HTML single-page and chunked-HTML render targets
- [ ] PDF render target (via FOP or dblatex)
- [ ] EPUB render target
- [ ] Versioned releases tagged `vX.Y` aligned to LFS upstream versions
- [ ] Online hosting (GitHub Pages or similar)

---

## Milestone 7 — Community & Governance

- [ ] `CONTRIBUTING.md` with arch maintainer roles
- [ ] Arch maintainer assignments (one primary + one backup per arch)
- [ ] Issue and PR templates
- [ ] Changelog / release notes policy
- [ ] Mailing list or forum for discussion

---

## Long-Term / Stretch Goals

- [ ] BLFS (Beyond LFS) multi-arch companion volume
- [ ] ALFS (Automated LFS) jhalfs-style build system for all 14 arches
- [ ] Live ISO builder per architecture
- [ ] musl libc variant of the book
- [ ] Clang/LLVM toolchain variant

---

## Version History

| Date       | Event                              |
|------------|------------------------------------|
| 2026-03-17 | Project started, ROADMAP drafted   |
| 2026-03-17 | Milestone 0 complete — book structure, tooling, CI, all stubs |
