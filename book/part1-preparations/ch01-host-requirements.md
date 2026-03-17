# Chapter 1 — Host System Requirements

## 1.1 Required Software

Your host system must have the following tools at the listed minimum versions.
Run `scripts/version-check.sh` to verify.

| Package       | Minimum version |
|---------------|----------------|
| Bash          | 3.2            |
| Binutils      | 2.13.1         |
| Bison         | 2.7            |
| Coreutils     | 6.9            |
| Diffutils     | 2.8.1          |
| Findutils     | 4.2.31         |
| Gawk          | 4.0.1          |
| GCC           | 5.2 (C and C++)|
| Glibc         | 2.11           |
| Grep          | 2.5.1a         |
| Gzip          | 1.3.12         |
| Linux kernel  | 4.14           |
| M4            | 1.4.10         |
| Make          | 4.0            |
| Patch         | 2.5.4          |
| Perl          | 5.8.8          |
| Python        | 3.4            |
| Sed           | 4.1.5          |
| Tar           | 1.22           |
| Texinfo       | 5.0            |
| Xz            | 5.0.0          |

For **cross-compilation** to a non-host architecture you also need:
- A cross-binutils and cross-gcc for `$LFS_TGT` (the book builds these in Part II)
- QEMU (optional, for testing — `qemu-system-<arch>` or `qemu-<arch>-static`)

## 1.2 Disk Space

A complete LFS build requires approximately:

| Phase                    | Approximate space |
|--------------------------|------------------|
| Source tarballs          | ~500 MB          |
| Cross toolchain build    | ~3 GB            |
| Temporary tools          | ~3 GB            |
| Final system             | ~10 GB           |
| **Total recommended**    | **~20 GB**       |

## 1.3 Architecture-Specific Host Notes

- **alpha, hppa, m68k, s390, sparc**: These are rare architectures.
  Cross-compilation from an amd64 or arm64 host is the standard approach.
  Ensure your host GCC supports the target (`--enable-targets=all` or a
  dedicated cross-gcc package from your distro).

- **loong**: LoongArch cross-toolchain support landed in GCC 12 and
  Binutils 2.38.  Use those versions or newer.

- **riscv**: Cross-toolchain support is mature in GCC 7+ and Binutils 2.28+.

- **mips**: Confirm whether you need big-endian (`mips`) or little-endian
  (`mipsel`) and set `LFS_TGT` accordingly.

- **ppc64**: Decide early between `ppc64le` (ELFv2, modern) and `ppc64` BE
  (ELFv1, legacy).  They use different GCC flags and different glibc ABIs.
