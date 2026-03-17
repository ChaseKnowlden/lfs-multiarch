# Chapter 7 — Linux API Headers

The Linux kernel exposes an API to userspace through sanitised header files.
Glibc needs these headers to know which syscalls and structures the kernel
provides.

## 7.1 Installation

```bash
tar -xf linux-6.10.5.tar.xz
cd linux-6.10.5

make mrproper
make ARCH=$LFS_ARCH_LINUX headers
find usr/include -type f ! -name '*.h' -delete
cp -rv usr/include $LFS/usr
cd ..
rm -rf linux-6.10.5
```

## Arch Notes

| Arch   | `ARCH=` value | Notes                                                     |
|--------|--------------|-----------------------------------------------------------|
| alpha  | `alpha`      |                                                           |
| amd64  | `x86_64`     |                                                           |
| arm    | `arm`        |                                                           |
| arm64  | `arm64`      |                                                           |
| hppa   | `parisc`     | Note: kernel arch name differs from GNU triplet prefix    |
| loong  | `loongarch`  |                                                           |
| m68k   | `m68k`       |                                                           |
| mips   | `mips`       |                                                           |
| ppc    | `powerpc`    |                                                           |
| ppc64  | `powerpc`    | Same kernel arch for both BE and LE 64-bit                |
| riscv  | `riscv`      |                                                           |
| s390   | `s390`       |                                                           |
| sparc  | `sparc`      |                                                           |
| x86    | `x86`        |                                                           |

`$LFS_ARCH_LINUX` is set correctly for all supported architectures by
`scripts/arch-config.sh`.
