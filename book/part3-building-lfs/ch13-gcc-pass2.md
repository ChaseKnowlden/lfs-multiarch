# Chapter 13 — GCC Pass 2

GCC pass 2 produces the final native compiler for the LFS system.
At this point glibc is installed, so the full C and C++ runtimes are built.

> **Work in progress.**

## Key Differences from Pass 1

- `--with-newlib` removed
- `--without-headers` removed
- `--disable-libstdcxx` removed; libstdc++ is now built fully
- Threads and shared libraries enabled

## Arch Notes

All `$LFS_GCC_EXTRA` flags from `arch-config.sh` continue to apply.
Consult [Architecture Reference](../architectures/arch-notes.md) for
per-arch considerations (ELFv2 ABI for ppc64, `-mieee` for alpha, etc.).
