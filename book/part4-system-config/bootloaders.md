# Bootloader Configuration

Each architecture uses a different bootloader.  Find your architecture below.

---

## amd64 / x86 — GRUB (BIOS or EFI)

### BIOS (legacy)
```bash
grub-install /dev/sdX
cat > /boot/grub/grub.cfg << EOF
set default=0
set timeout=5
menuentry "LFS ($LFS_ARCH)" {
    linux /boot/vmlinuz-$(uname -r) root=/dev/sdXY ro
}
EOF
```

### EFI (amd64)
```bash
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=LFS
# grub.cfg same as above
```

---

## arm64 — GRUB EFI

```bash
grub-install --target=arm64-efi --efi-directory=/boot/efi --bootloader-id=LFS
```

---

## arm — U-Boot (typical embedded board)

Create `/boot/boot.cmd`:
```text
setenv bootargs "root=/dev/mmcblk0p2 rw console=ttyS0,115200"
load mmc 0:1 ${kernel_addr_r}  /boot/zImage
load mmc 0:1 ${fdt_addr_r}     /boot/dtb/${fdtfile}
bootz ${kernel_addr_r} - ${fdt_addr_r}
```
Compile: `mkimage -C none -A arm -T script -d boot.cmd /boot/boot.scr`

---

## alpha — aboot (SRM)

```bash
swriteboot -f3 /dev/sdX /boot/bootlx
cat > /etc/aboot.conf << EOF
0:2/boot/vmlinuz-lfs root=/dev/sdX2 ro
EOF
```

---

## hppa — PALO

```bash
palo -f /etc/palo.conf
```
`/etc/palo.conf`:
```text
--format=new
--kernel=vmlinux
--ramdisk=
--commandline="2/vmlinux HOME=/ TERM=linux root=/dev/sdX2 ro"
```

---

## loong — GRUB EFI (UEFI)

```bash
grub-install --target=loongarch64-efi --efi-directory=/boot/efi
```

---

## m68k — Platform-Specific

- **Amiga**: use `amiboot` from AmigaOS or network-boot via TFTP
- **Atari**: use `atari-bootstrap`
- **VME / Q40**: consult platform documentation

---

## mips — U-Boot / YAMON

U-Boot (most common):
```text
setenv bootargs "root=/dev/sda1 rw console=ttyS0,115200"
bootm ${kernel_addr}
```

---

## ppc (32-bit) — Yaboot (OpenFirmware)

`/etc/yaboot.conf`:
```text
boot=/dev/sdX2
device=hd:
partition=2
root=/dev/sdX3
image=/boot/vmlinux
label=LFS
```
Run `ybin -v` after writing the config.

---

## ppc64 — GRUB (OPAL / IEEE 1275)

```bash
grub-install --target=powerpc-ieee1275 /dev/sdX
```

---

## riscv — OpenSBI + U-Boot + GRUB EFI

RISC-V systems typically chain:
1. OpenSBI (M-mode firmware) — provided by board
2. U-Boot (S-mode, EFI payload)
3. GRUB EFI
4. Linux kernel

```bash
grub-install --target=riscv64-efi --efi-directory=/boot/efi
```

---

## s390 — zipl

```bash
cat > /etc/zipl.conf << EOF
[defaultboot]
default=lfs
target=/boot

[lfs]
image=/boot/image
ramdisk=/boot/initrd
parameters="root=/dev/dasda1 ro"
EOF
zipl
```

---

## sparc — SILO

`/etc/silo.conf`:
```text
partition=1
root=/dev/sda1
read-write
image=/boot/vmlinuz-lfs
label=LFS
```
Run `silo` after writing the config.
