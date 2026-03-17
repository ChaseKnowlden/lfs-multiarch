# loong (LoongArch64) Supplement

| Variable         | Value                                       |
|------------------|---------------------------------------------|
| `LFS_TGT`        | `loongarch64-lfs-linux-gnu`                 |
| `LFS_ARCH_LINUX` | `loongarch`                                 |
| `LFS_BITS`       | 64                                          |
| `LFS_ENDIAN`     | little                                      |
| `LFS_ABI`        | lp64d (double-precision FP)                 |
| `LFS_GCC_EXTRA`  | `--with-arch=loongarch64 --with-abi=lp64d`  |
| Bootloader       | GRUB EFI (UEFI)                             |
| Tier             | 2 — builds, limited testing                 |

## Toolchain Version Requirements

| Tool     | Minimum version |
|----------|----------------|
| GCC      | 12.0           |
| Binutils | 2.38           |
| Linux    | 5.19           |
| Glibc    | 2.38           |

## Platform Notes

- LoongArch is a MIPS-inspired RISC ISA introduced by Loongson Technology.
- The `lp64d` ABI uses 64-bit pointers and double-precision hardware FP;
  it is the only ABI with upstream glibc support.
- Systems use UEFI; GRUB EFI target is `loongarch64-efi`.
- Check `patches/loong/` for any glibc or kernel patches needed for your
  kernel version.

## Bootloader

See [Bootloader Configuration — loong](../part4-system-config/bootloaders.md#loong--grub-efi-uefi).
