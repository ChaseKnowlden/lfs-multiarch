# Per-Architecture Notes

This file is the master reference for architecture-specific variables used
throughout the book.  Build scripts and chapter templates substitute these
values via `@@VAR@@` placeholders.

---

## alpha

```text
ARCH=alpha
LFS_TGT=alpha-lfs-linux-gnu
LINUX_ARCH=alpha
BITS=64
ENDIAN=little
ABI=default
BOOTLOADER=aboot (SRM console)
GCC_EXTRA=--with-arch=ev6 -mieee (recommended)
KERNEL_EXTRA=CONFIG_ALPHA_EV6=y
TIER=3
```

## amd64

```text
ARCH=x86_64
LFS_TGT=x86_64-lfs-linux-gnu
LINUX_ARCH=x86_64
BITS=64
ENDIAN=little
PAGE_SIZE=4096
ABI=LP64
BOOTLOADER=GRUB (BIOS or EFI)
GCC_EXTRA=--with-arch=x86-64
TIER=1
```

## arm

```text
ARCH=arm
LFS_TGT=arm-lfs-linux-gnueabihf
LINUX_ARCH=arm
BITS=32
ENDIAN=little
ABI=EABI hard-float (armhf)
BOOTLOADER=U-Boot or GRUB EFI
GCC_EXTRA=--with-arch=armv7-a --with-fpu=vfpv3-d16 --with-float=hard
TIER=2
```

## arm64

```text
ARCH=aarch64
LFS_TGT=aarch64-lfs-linux-gnu
LINUX_ARCH=arm64
BITS=64
ENDIAN=little
PAGE_SIZE=4096 (default; kernel supports 16384 on Apple Silicon/Ampere and 65536 on some HPC configs)
ABI=LP64
BOOTLOADER=GRUB EFI or U-Boot
GCC_EXTRA=--with-arch=armv8-a
TIER=1
```

## hppa

```text
ARCH=hppa
LFS_TGT=hppa-lfs-linux-gnu
LINUX_ARCH=parisc
BITS=32
ENDIAN=big
ABI=default
BOOTLOADER=PALO
GCC_EXTRA=--disable-werror
TIER=3
```

## loong

```text
ARCH=loongarch64
LFS_TGT=loongarch64-lfs-linux-gnu
LINUX_ARCH=loongarch
BITS=64
ENDIAN=little
ABI=LP64D (double-precision FP)
BOOTLOADER=GRUB EFI (UEFI)
GCC_EXTRA=--with-arch=loongarch64 --with-abi=lp64d
TIER=2
```

## m68k

```text
ARCH=m68k
LFS_TGT=m68k-lfs-linux-gnu
LINUX_ARCH=m68k
BITS=32
ENDIAN=big
ABI=default
BOOTLOADER=platform-specific (amiboot, atari-bootstrap, etc.)
GCC_EXTRA=--with-cpu=68020 (minimum; adjust per platform)
TIER=3
```

## mips

### MIPS 32-bit big-endian (default)
```text
ARCH=mips
LFS_TGT=mips-lfs-linux-gnu
LINUX_ARCH=mips
BITS=32
ENDIAN=big
ABI=O32
BOOTLOADER=YAMON / U-Boot / CFE
GCC_EXTRA=--with-arch=mips32r2 --with-abi=32
TIER=2
```

### MIPS 32-bit little-endian variant
```text
LFS_TGT=mipsel-lfs-linux-gnu
ENDIAN=little
```

## ppc

```text
ARCH=powerpc
LFS_TGT=powerpc-lfs-linux-gnu
LINUX_ARCH=powerpc
BITS=32
ENDIAN=big
ABI=default
BOOTLOADER=Yaboot (OF) or GRUB-IEEE1275
GCC_EXTRA=--with-cpu=powerpc --enable-secureplt
TIER=2
```

## ppc64

### ppc64le (little-endian, ELFv2 — primary)
```text
ARCH=powerpc64le
LFS_TGT=powerpc64le-lfs-linux-gnu
LINUX_ARCH=powerpc
BITS=64
ENDIAN=little
ABI=ELFv2
BOOTLOADER=GRUB (OPAL/PowerNV) or GRUB-IEEE1275
GCC_EXTRA=--with-cpu=power8 --with-abi=elfv2
TIER=2
```

### ppc64 (big-endian, ELFv1 — secondary)
```text
ARCH=powerpc64
LFS_TGT=powerpc64-lfs-linux-gnu
ENDIAN=big
ABI=ELFv1
```

## riscv

```text
ARCH=riscv64
LFS_TGT=riscv64-lfs-linux-gnu
LINUX_ARCH=riscv
BITS=64
ENDIAN=little
ABI=lp64d (rv64gc baseline)
BOOTLOADER=OpenSBI + U-Boot + GRUB EFI
GCC_EXTRA=--with-arch=rv64gc --with-abi=lp64d
TIER=2
```

## s390

```text
ARCH=s390x
LFS_TGT=s390x-lfs-linux-gnu
LINUX_ARCH=s390
BITS=64
ENDIAN=big
ABI=default
BOOTLOADER=zipl
GCC_EXTRA=--with-arch=z196 (minimum recommended)
TIER=3
```

## sparc

```text
ARCH=sparc64
LFS_TGT=sparc64-lfs-linux-gnu
LINUX_ARCH=sparc
BITS=64
ENDIAN=big
ABI=LP64
BOOTLOADER=SILO (or OpenBoot PROM direct)
GCC_EXTRA=--with-cpu=ultrasparc
TIER=3
```

## x86

```text
ARCH=i686
LFS_TGT=i686-lfs-linux-gnu
LINUX_ARCH=x86
BITS=32
ENDIAN=little
PAGE_SIZE=4096
ABI=default (IA-32)
BOOTLOADER=GRUB BIOS
GCC_EXTRA=--with-arch=i686
TIER=1
```
