#!/bin/bash
# arch-config.sh — set LFS cross-compilation variables for a target arch.
# Usage: source scripts/arch-config.sh <arch>
#   arch must be one of: alpha amd64 arm arm64 hppa loong m68k mips
#                        ppc ppc64 riscv s390 sparc x86

set -euo pipefail

ARCH="${1:-}"
if [[ -z "$ARCH" ]]; then
    echo "Usage: source $0 <arch>" >&2
    return 1 2>/dev/null || exit 1
fi

case "$ARCH" in
    alpha)
        export LFS_TGT=alpha-lfs-linux-gnu
        export LFS_ARCH_LINUX=alpha
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--with-arch=ev6"
        export LFS_BOOTLOADER=aboot
        ;;
    amd64)
        export LFS_TGT=x86_64-lfs-linux-gnu
        export LFS_ARCH_LINUX=x86_64
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=LP64
        export LFS_GCC_EXTRA="--with-arch=x86-64"
        export LFS_BOOTLOADER=grub
        ;;
    arm)
        export LFS_TGT=arm-lfs-linux-gnueabihf
        export LFS_ARCH_LINUX=arm
        export LFS_BITS=32
        export LFS_ENDIAN=little
        export LFS_ABI=EABI-hf
        export LFS_GCC_EXTRA="--with-arch=armv7-a --with-fpu=vfpv3-d16 --with-float=hard"
        export LFS_BOOTLOADER=uboot
        ;;
    arm64)
        export LFS_TGT=aarch64-lfs-linux-gnu
        export LFS_ARCH_LINUX=arm64
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=LP64
        export LFS_GCC_EXTRA="--with-arch=armv8-a"
        export LFS_BOOTLOADER=grub-efi
        ;;
    hppa)
        export LFS_TGT=hppa-lfs-linux-gnu
        export LFS_ARCH_LINUX=parisc
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--disable-werror"
        export LFS_BOOTLOADER=palo
        ;;
    loong)
        export LFS_TGT=loongarch64-lfs-linux-gnu
        export LFS_ARCH_LINUX=loongarch
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=lp64d
        export LFS_GCC_EXTRA="--with-arch=loongarch64 --with-abi=lp64d"
        export LFS_BOOTLOADER=grub-efi
        ;;
    m68k)
        export LFS_TGT=m68k-lfs-linux-gnu
        export LFS_ARCH_LINUX=m68k
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--with-cpu=68020"
        export LFS_BOOTLOADER=platform-specific
        ;;
    mips)
        export LFS_TGT=mips-lfs-linux-gnu
        export LFS_ARCH_LINUX=mips
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=O32
        export LFS_GCC_EXTRA="--with-arch=mips32r2 --with-abi=32"
        export LFS_BOOTLOADER=uboot
        ;;
    mipsel)
        export LFS_TGT=mipsel-lfs-linux-gnu
        export LFS_ARCH_LINUX=mips
        export LFS_BITS=32
        export LFS_ENDIAN=little
        export LFS_ABI=O32
        export LFS_GCC_EXTRA="--with-arch=mips32r2 --with-abi=32"
        export LFS_BOOTLOADER=uboot
        ;;
    ppc)
        export LFS_TGT=powerpc-lfs-linux-gnu
        export LFS_ARCH_LINUX=powerpc
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--with-cpu=powerpc --enable-secureplt"
        export LFS_BOOTLOADER=yaboot
        ;;
    ppc64)
        export LFS_TGT=powerpc64le-lfs-linux-gnu
        export LFS_ARCH_LINUX=powerpc
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=ELFv2
        export LFS_GCC_EXTRA="--with-cpu=power8 --with-abi=elfv2"
        export LFS_BOOTLOADER=grub-ieee1275
        ;;
    riscv)
        export LFS_TGT=riscv64-lfs-linux-gnu
        export LFS_ARCH_LINUX=riscv
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=lp64d
        export LFS_GCC_EXTRA="--with-arch=rv64gc --with-abi=lp64d"
        export LFS_BOOTLOADER=opensbi-uboot-grub
        ;;
    s390)
        export LFS_TGT=s390x-lfs-linux-gnu
        export LFS_ARCH_LINUX=s390
        export LFS_BITS=64
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--with-arch=z196"
        export LFS_BOOTLOADER=zipl
        ;;
    sparc)
        export LFS_TGT=sparc64-lfs-linux-gnu
        export LFS_ARCH_LINUX=sparc
        export LFS_BITS=64
        export LFS_ENDIAN=big
        export LFS_ABI=LP64
        export LFS_GCC_EXTRA="--with-cpu=ultrasparc"
        export LFS_BOOTLOADER=silo
        ;;
    x86)
        export LFS_TGT=i686-lfs-linux-gnu
        export LFS_ARCH_LINUX=x86
        export LFS_BITS=32
        export LFS_ENDIAN=little
        export LFS_ABI=IA-32
        export LFS_GCC_EXTRA="--with-arch=i686"
        export LFS_BOOTLOADER=grub-bios
        ;;
    *)
        echo "Unknown arch: $ARCH" >&2
        echo "Valid: alpha amd64 arm arm64 hppa loong m68k mips ppc ppc64 riscv s390 sparc x86" >&2
        return 1 2>/dev/null || exit 1
        ;;
esac

export LFS_ARCH="$ARCH"
echo "LFS_ARCH=$LFS_ARCH  LFS_TGT=$LFS_TGT  (${LFS_BITS}-bit ${LFS_ENDIAN}-endian)"
