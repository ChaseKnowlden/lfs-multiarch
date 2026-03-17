# amd64 (x86-64) Supplement

| Variable         | Value                          |
|------------------|--------------------------------|
| `LFS_TGT`        | `x86_64-lfs-linux-gnu`         |
| `LFS_ARCH_LINUX` | `x86_64`                       |
| `LFS_BITS`       | 64                             |
| `LFS_ENDIAN`     | little                         |
| `LFS_ABI`        | LP64                           |
| `LFS_GCC_EXTRA`  | `--with-arch=x86-64`           |
| Bootloader       | GRUB (BIOS or EFI)             |
| Tier             | 1 — well-tested, CI-verified   |

## Platform Notes

- This is the primary development and CI target for the book.
- Supports both BIOS (legacy) and UEFI boot via GRUB.
- For Secure Boot, enrol the GRUB signing key in MOK; not covered in this book.
- The `lib64` → `lib` symlink is required in the LFS tree for correct
  dynamic linker resolution.

## Bootloader

See [Bootloader Configuration — amd64](../part4-system-config/bootloaders.md#amd64--x86--grub-bios-or-efi).
