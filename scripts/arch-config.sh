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
        export LFS_QEMU_STATIC=qemu-alpha-static
        ;;
    amd64)
        export LFS_TGT=x86_64-lfs-linux-gnu
        export LFS_ARCH_LINUX=x86_64
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=LP64
        export LFS_GCC_EXTRA="--with-arch=x86-64"
        export LFS_BOOTLOADER=grub
        export LFS_QEMU_STATIC=qemu-x86_64-static
        ;;
    arm)
        export LFS_TGT=arm-lfs-linux-gnueabihf
        export LFS_ARCH_LINUX=arm
        export LFS_BITS=32
        export LFS_ENDIAN=little
        export LFS_ABI=EABI-hf
        export LFS_GCC_EXTRA="--with-arch=armv7-a --with-fpu=vfpv3-d16 --with-float=hard"
        export LFS_BOOTLOADER=uboot
        export LFS_QEMU_STATIC=qemu-arm-static
        ;;
    arm64)
        export LFS_TGT=aarch64-lfs-linux-gnu
        export LFS_ARCH_LINUX=arm64
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=LP64
        export LFS_GCC_EXTRA="--with-arch=armv8-a"
        export LFS_BOOTLOADER=grub-efi
        export LFS_QEMU_STATIC=qemu-aarch64-static
        ;;
    hppa)
        export LFS_TGT=hppa-lfs-linux-gnu
        export LFS_ARCH_LINUX=parisc
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--disable-werror"
        export LFS_BOOTLOADER=palo
        export LFS_QEMU_STATIC=qemu-hppa-static
        ;;
    loong)
        export LFS_TGT=loongarch64-lfs-linux-gnu
        export LFS_ARCH_LINUX=loongarch
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=lp64d
        export LFS_GCC_EXTRA="--with-arch=loongarch64 --with-abi=lp64d"
        export LFS_BOOTLOADER=grub-efi
        export LFS_QEMU_STATIC=qemu-loongarch64-static
        ;;
    m68k)
        export LFS_TGT=m68k-lfs-linux-gnu
        export LFS_ARCH_LINUX=m68k
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--with-cpu=68020"
        export LFS_BOOTLOADER=platform-specific
        export LFS_QEMU_STATIC=qemu-m68k-static
        ;;
    mips)
        export LFS_TGT=mips-lfs-linux-gnu
        export LFS_ARCH_LINUX=mips
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=O32
        export LFS_GCC_EXTRA="--with-arch=mips32r2 --with-abi=32"
        export LFS_BOOTLOADER=uboot
        export LFS_QEMU_STATIC=qemu-mips-static
        ;;
    mipsel)
        export LFS_TGT=mipsel-lfs-linux-gnu
        export LFS_ARCH_LINUX=mips
        export LFS_BITS=32
        export LFS_ENDIAN=little
        export LFS_ABI=O32
        export LFS_GCC_EXTRA="--with-arch=mips32r2 --with-abi=32"
        export LFS_BOOTLOADER=uboot
        export LFS_QEMU_STATIC=qemu-mipsel-static
        ;;
    ppc)
        export LFS_TGT=powerpc-lfs-linux-gnu
        export LFS_ARCH_LINUX=powerpc
        export LFS_BITS=32
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--with-cpu=powerpc --enable-secureplt"
        export LFS_BOOTLOADER=yaboot
        export LFS_QEMU_STATIC=qemu-ppc-static
        ;;
    ppc64)
        export LFS_TGT=powerpc64le-lfs-linux-gnu
        export LFS_ARCH_LINUX=powerpc
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=ELFv2
        export LFS_GCC_EXTRA="--with-cpu=power8 --with-abi=elfv2"
        export LFS_BOOTLOADER=grub-ieee1275
        export LFS_QEMU_STATIC=qemu-ppc64le-static
        ;;
    riscv)
        export LFS_TGT=riscv64-lfs-linux-gnu
        export LFS_ARCH_LINUX=riscv
        export LFS_BITS=64
        export LFS_ENDIAN=little
        export LFS_ABI=lp64d
        export LFS_GCC_EXTRA="--with-arch=rv64gc --with-abi=lp64d"
        export LFS_BOOTLOADER=opensbi-uboot-grub
        export LFS_QEMU_STATIC=qemu-riscv64-static
        ;;
    s390)
        export LFS_TGT=s390x-lfs-linux-gnu
        export LFS_ARCH_LINUX=s390
        export LFS_BITS=64
        export LFS_ENDIAN=big
        export LFS_ABI=default
        export LFS_GCC_EXTRA="--with-arch=z196"
        export LFS_BOOTLOADER=zipl
        export LFS_QEMU_STATIC=qemu-s390x-static
        ;;
    sparc)
        export LFS_TGT=sparc64-lfs-linux-gnu
        export LFS_ARCH_LINUX=sparc
        export LFS_BITS=64
        export LFS_ENDIAN=big
        export LFS_ABI=LP64
        export LFS_GCC_EXTRA="--with-cpu=ultrasparc"
        export LFS_BOOTLOADER=silo
        export LFS_QEMU_STATIC=qemu-sparc64-static
        ;;
    x86)
        export LFS_TGT=i686-lfs-linux-gnu
        export LFS_ARCH_LINUX=x86
        export LFS_BITS=32
        export LFS_ENDIAN=little
        export LFS_ABI=IA-32
        export LFS_GCC_EXTRA="--with-arch=i686"
        export LFS_BOOTLOADER=grub-bios
        export LFS_QEMU_STATIC=qemu-i386-static
        ;;
    *)
        echo "Unknown arch: $ARCH" >&2
        echo "Valid: alpha amd64 arm arm64 hppa loong m68k mips ppc ppc64 riscv s390 sparc x86" >&2
        return 1 2>/dev/null || exit 1
        ;;
esac

export LFS_ARCH="$ARCH"

# Resolve the actual QEMU static binary name.
# Debian/Ubuntu ship qemu-<arch>-static; Gentoo and some others ship qemu-<arch>.
# Check for both and prefer whichever exists.
_qemu_base="${LFS_QEMU_STATIC%-static}"   # strip trailing -static to get base name
if command -v "$LFS_QEMU_STATIC" &>/dev/null; then
    : # already correct
elif command -v "$_qemu_base" &>/dev/null; then
    export LFS_QEMU_STATIC="$_qemu_base"
else
    echo "Warning: neither $LFS_QEMU_STATIC nor $_qemu_base found in PATH" >&2
    echo "         Set LFS_QEMU_STATIC manually if the binary has a different name." >&2
fi
unset _qemu_base

echo "LFS_ARCH=$LFS_ARCH  LFS_TGT=$LFS_TGT  (${LFS_BITS}-bit ${LFS_ENDIAN}-endian)"
