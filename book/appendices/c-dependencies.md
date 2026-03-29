# Appendix C — Package Dependencies

> **Work in progress.** This appendix will list the build-time and
> run-time dependencies of each package in the book, generated from
> the package metadata.

## Dependency Graph (summary)

```text
GCC ──────────────── needs ──► GMP, MPFR, MPC
Glibc ────────────── needs ──► Linux API headers
Binutils pass 2 ──── needs ──► Glibc headers (via sysroot)
Python ───────────── needs ──► OpenSSL, Libffi, Zlib, Expat, Readline
Perl ─────────────── needs ──► Gdbm, DB (optional)
OpenSSL ──────────── needs ──► Zlib
E2fsprogs ───────── needs ──► Util-linux (libblkid)
Util-linux ──────── needs ──► Readline, Ncurses, Zlib, Libcap, Shadow
Udev ─────────────── needs ──► Kmod, Util-linux
```

A full machine-readable dependency graph will be provided in a future release.
