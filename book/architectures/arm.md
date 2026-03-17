# arm (ARMv7 32-bit) Supplement

| Variable         | Value                                                      |
|------------------|------------------------------------------------------------|
| `LFS_TGT`        | `arm-lfs-linux-gnueabihf`                                  |
| `LFS_ARCH_LINUX` | `arm`                                                      |
| `LFS_BITS`       | 32                                                         |
| `LFS_ENDIAN`     | little                                                     |
| `LFS_ABI`        | EABI hard-float (armhf)                                    |
| `LFS_GCC_EXTRA`  | `--with-arch=armv7-a --with-fpu=vfpv3-d16 --with-float=hard` |
| Bootloader       | U-Boot or GRUB EFI (board-dependent)                       |
| Tier             | 2 — builds, limited testing                                |

## Platform Notes

- **ABI**: This book targets the `armhf` (EABI hard-float) ABI.  For soft-float
  (`armel`) boards, change `LFS_TGT` to `arm-lfs-linux-gnueabi` and adjust
  `$LFS_GCC_EXTRA` accordingly.
- **Device Tree**: Most ARM boards require a `.dtb` file alongside the kernel.
  Build DTBs with `make ARCH=arm dtbs` and copy to `/boot/dtb/`.
- **U-Boot**: Many embedded boards use U-Boot.  Consult your board's
  documentation for the correct boot.cmd / boot.scr recipe.
- Minimum ARMv7-A with VFPv3-D16 assumed.  Older ARMv6 (Raspberry Pi 1)
  requires a different ABI and is not covered here.

## Bootloader

See [Bootloader Configuration — arm](../part4-system-config/bootloaders.md#arm--u-boot-typical-embedded-board).
