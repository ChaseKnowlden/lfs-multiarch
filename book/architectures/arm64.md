# arm64 (AArch64) Supplement

| Variable         | Value                           |
|------------------|---------------------------------|
| `LFS_TGT`        | `aarch64-lfs-linux-gnu`         |
| `LFS_ARCH_LINUX` | `arm64`                         |
| `LFS_BITS`       | 64                              |
| `LFS_ENDIAN`     | little                          |
| `LFS_ABI`        | LP64                            |
| `LFS_GCC_EXTRA`  | `--with-arch=armv8-a`           |
| Bootloader       | GRUB EFI or U-Boot              |
| Tier             | 1 — well-tested, CI-verified    |

## Platform Notes

- AArch64 systems are the second primary Tier 1 target alongside amd64.
- Most modern server-grade ARM64 hardware (Ampere, AWS Graviton, Apple M-series
  via Asahi) boots via UEFI; use GRUB EFI.
- Embedded boards (Raspberry Pi 4/5, Rock 5, etc.) use U-Boot; some also
  expose UEFI via EDK2 firmware.
- **ILP32 variant**: Not covered; the standard LP64 ABI is used throughout.
- Device Tree: built with `make ARCH=arm64 dtbs`.

## Bootloader

See [Bootloader Configuration — arm64](../part4-system-config/bootloaders.md#arm64--grub-efi).
