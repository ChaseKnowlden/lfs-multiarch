# riscv (RISC-V 64-bit) Supplement

| Variable         | Value                                          |
|------------------|------------------------------------------------|
| `LFS_TGT`        | `riscv64-lfs-linux-gnu`                        |
| `LFS_ARCH_LINUX` | `riscv`                                        |
| `LFS_BITS`       | 64                                             |
| `LFS_ENDIAN`     | little                                         |
| `LFS_ABI`        | lp64d (rv64gc, double-precision FP)            |
| `LFS_GCC_EXTRA`  | `--with-arch=rv64gc --with-abi=lp64d`          |
| Bootloader       | OpenSBI → U-Boot → GRUB EFI                    |
| Tier             | 2 — builds, limited testing                    |

## Toolchain Version Requirements

| Tool     | Minimum version |
|----------|----------------|
| GCC      | 7.0            |
| Binutils | 2.28           |
| Linux    | 5.10           |
| Glibc    | 2.27           |

## ISA and ABI Baseline

This book targets `rv64gc`:
- `g` = `imafd` general (integer + multiply + atomic + float + double)
- `c` = compressed instructions

The `lp64d` ABI uses 64-bit pointers and double-precision hardware FP registers.

For embedded targets without FP, use `rv64imac` + `lp64` and adjust
`$LFS_GCC_EXTRA` accordingly (not covered in detail here).

## Boot Chain

```text
OpenSBI (M-mode)
  └─ U-Boot (S-mode, EFI payload) or directly to kernel
       └─ GRUB EFI (optional)
            └─ Linux kernel
```

Hardware that provides UEFI (e.g. StarFive VisionFive 2, SiFive HiFive Unmatched)
can use GRUB EFI.  Hardware without UEFI uses U-Boot's `booti` command directly.

## Platform Notes

- Device Tree is required on most RISC-V boards.
- The SBI (Supervisor Binary Interface) provided by OpenSBI is the standard
  way for the kernel to make firmware calls.

## Bootloader

See [Bootloader Configuration — riscv](../part4-system-config/bootloaders.md#riscv--opensbi--u-boot--grub-efi).
