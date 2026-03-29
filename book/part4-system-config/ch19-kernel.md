# Chapter 19 — The Linux Kernel

## 19.1 Configuration

```bash
tar -xf linux-6.10.5.tar.xz
cd linux-6.10.5

make ARCH=$LFS_ARCH_LINUX mrproper
make ARCH=$LFS_ARCH_LINUX defconfig     # start from a sane baseline
make ARCH=$LFS_ARCH_LINUX menuconfig    # customise
```

### Minimum Required Options

Ensure these are set (=y or =m as appropriate):

```text
CONFIG_DEVTMPFS=y
CONFIG_DEVTMPFS_MOUNT=y
CONFIG_SYSFS=y
CONFIG_PROC_FS=y
CONFIG_EXT4_FS=y          # or whichever filesystem you used for root
CONFIG_UNIX=y
```

## 19.2 Build and Install

```bash
make ARCH=$LFS_ARCH_LINUX -j$(nproc)
make ARCH=$LFS_ARCH_LINUX modules_install
```

### Kernel image names by architecture

| Arch   | Image file              | Install command / notes                         |
|--------|-------------------------|-------------------------------------------------|
| alpha  | `arch/alpha/boot/vmlinux.gz` | `cp vmlinux.gz /boot/`                     |
| amd64  | `arch/x86/boot/bzImage` | `cp bzImage /boot/vmlinuz-6.10.5`               |
| arm    | `arch/arm/boot/zImage`  | `cp zImage /boot/` + DTB files                  |
| arm64  | `arch/arm64/boot/Image.gz` | `cp Image.gz /boot/` + DTB files             |
| hppa   | `vmlinux`               | `cp vmlinux /boot/`                             |
| loong  | `arch/loongarch/boot/vmlinuz.efi` | Copy to EFI partition                 |
| m68k   | `arch/m68k/boot/vmlinux` | Platform-dependent                             |
| mips   | `arch/mips/boot/vmlinux.gz` | `cp vmlinux.gz /boot/`                      |
| ppc    | `arch/powerpc/boot/vmlinux` | `cp vmlinux /boot/`                         |
| ppc64  | `arch/powerpc/boot/vmlinux` | `cp vmlinux /boot/`                         |
| riscv  | `arch/riscv/boot/Image.gz` | `cp Image.gz /boot/`                         |
| s390   | `arch/s390/boot/bzImage` | `cp bzImage /boot/image`                        |
| sparc  | `arch/sparc/boot/image` | `cp image /boot/`                               |
| x86    | `arch/x86/boot/bzImage` | `cp bzImage /boot/vmlinuz-6.10.5`               |

## 19.3 Arch-Specific Kernel Notes

### arm / arm64 — Device Tree
```bash
make ARCH=$LFS_ARCH_LINUX dtbs
cp -r arch/$LFS_ARCH_LINUX/boot/dts /boot/dtb
```

### riscv — OpenSBI integration
RISC-V systems typically embed OpenSBI as the M-mode firmware before the
kernel runs.  The kernel itself runs in S-mode.  See the
[Bootloader Configuration](bootloaders.md) chapter.

### s390 — zipl
After copying the kernel, run `zipl` to update the boot record.

### loong — EFI stub
LoongArch kernels include an EFI stub and can be booted directly by the
UEFI firmware or via GRUB.
