# mips Supplement

| Variable         | Value (big-endian default)              |
|------------------|-----------------------------------------|
| `LFS_TGT`        | `mips-lfs-linux-gnu`                    |
| `LFS_ARCH_LINUX` | `mips`                                  |
| `LFS_BITS`       | 32                                      |
| `LFS_ENDIAN`     | big (or little: use `mipsel-…` triplet) |
| `LFS_ABI`        | O32                                     |
| `LFS_GCC_EXTRA`  | `--with-arch=mips32r2 --with-abi=32`    |
| Bootloader       | U-Boot, YAMON, or CFE                   |
| Tier             | 2 — builds, limited testing             |

## Endianness and ABI Variants

| Variant   | Triplet                       | `LFS_ENDIAN` |
|-----------|-------------------------------|--------------|
| 32-bit BE | `mips-lfs-linux-gnu`          | big          |
| 32-bit LE | `mipsel-lfs-linux-gnu`        | little       |
| 64-bit BE | `mips64-lfs-linux-gnuabi64`   | big          |
| 64-bit LE | `mips64el-lfs-linux-gnuabi64` | little       |

This book primarily targets 32-bit MIPS.  For 64-bit MIPS (N64 ABI),
adjust `--with-abi=64` and use a 64-bit triplet.

## Platform Notes

- Choose endianness based on your hardware (e.g. Malta dev board is
  big-endian by default but can be LE; MIPS Creator CI20 is LE).
- The `O32` ABI is the most compatible; `N32` and `N64` are 64-bit-only.
- For soft-float hardware, add `--with-float=soft` to `$LFS_GCC_EXTRA`
  and `--without-fp` to the glibc configure.

## Bootloader

See [Bootloader Configuration — mips](../part4-system-config/bootloaders.md#mips--u-boot--yamon).
