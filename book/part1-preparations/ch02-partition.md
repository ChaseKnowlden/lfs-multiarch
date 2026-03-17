# Chapter 2 — Preparing the Build Partition

## 2.1 Overview

LFS is built on a dedicated partition or disk image.  A minimum of 20 GB is
recommended (see Chapter 1 for a breakdown).

## 2.2 Partitioning

Use `fdisk`, `gdisk`, or `parted` to create a partition on your chosen disk.
A minimal setup requires one root partition.  For EFI systems add a small
(512 MiB) FAT32 EFI System Partition (ESP).

```bash
# Example: GPT disk with EFI + root
gdisk /dev/sdX
# n  1   +512M  EF00   (EFI System)
# n  2   <rest> 8300   (Linux filesystem)
# w
```

> **Arch Note — s390:** IBM Z systems use DASD storage (`/dev/dasda`).
> Partition with `fdasd` instead of `fdisk`/`gdisk`.

## 2.3 Creating Filesystems

```bash
mkfs.vfat -F32 /dev/sdX1          # ESP (EFI systems only)
mkfs.ext4 /dev/sdX2               # root
```

> **Arch Note — hppa (PA-RISC):** PALO requires the boot partition to be
> of type `f0` (PA-RISC Linux boot).  Use `fdisk` type `f0` for `/boot`.

## 2.4 Mounting

```bash
export LFS=/mnt/lfs
mkdir -pv $LFS
mount -v /dev/sdX2 $LFS
mkdir -pv $LFS/boot/efi           # EFI systems only
mount -v /dev/sdX1 $LFS/boot/efi  # EFI systems only
```

## 2.5 Setting Up the Source Directory

```bash
mkdir -v $LFS/sources
chmod -v a+wt $LFS/sources
```

Download all packages listed in Chapter 3 into `$LFS/sources`.  Use
`scripts/fetch-packages.sh` (Milestone 4) once available, or download
manually using the wget list provided in the Chapter 3 appendix.
