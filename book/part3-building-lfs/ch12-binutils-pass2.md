# Chapter 12 — Binutils Pass 2

Binutils pass 2 is built inside the chroot using the temporary tools,
producing the final native linker and assembler for the LFS target system.

> **Work in progress.**

## Key Differences from Pass 1

- Built with `--with-sysroot` pointing at the real LFS root, not `$LFS`
- `--enable-shared` is now appropriate
- The result goes into `/usr` (inside the chroot), not `$LFS/tools`

## Arch Notes

See [Architecture Reference](../architectures/arch-notes.md) for per-arch
`--disable-werror` and other flags.
