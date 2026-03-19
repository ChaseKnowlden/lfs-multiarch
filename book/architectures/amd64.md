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

## Toolchain Version Requirements

| Tool     | Minimum version |
|----------|----------------|
| GCC      | 4.8            |
| Binutils | 2.25           |
| Linux    | 4.14           |
| Glibc    | 2.17           |

## ISA Baseline

This book targets the **x86-64 v1** baseline, which assumes SSE2 as the minimum
SIMD instruction set.  The GCC flag `--with-arch=x86-64` selects this baseline.

The x86-64 micro-architecture levels are:

| Level    | Added features                        |
|----------|---------------------------------------|
| v1       | SSE, SSE2 (baseline, used here)       |
| v2       | SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT  |
| v3       | AVX, AVX2, BMI1/2, FMA, MOVBE        |
| v4       | AVX-512                               |

Targeting v1 produces binaries that run on all x86-64 CPUs from approximately
2003 onward.  If your hardware is known to support v2 or v3, you may substitute
`--with-arch=x86-64-v2` or `--with-arch=x86-64-v3` in `LFS_GCC_EXTRA` for
better performance.

## Boot Chain

```
Firmware (BIOS or UEFI)
  └─ GRUB 2
       └─ Linux kernel
```

**BIOS systems** use a small BIOS Boot Partition (1–2 MiB, type `EF02`) so
GRUB can embed its core image.

**UEFI systems** require an EFI System Partition (ESP, FAT32, at least 100 MiB)
mounted at `/boot/efi`.  GRUB installs as a `.efi` application inside the ESP.

For **Secure Boot**, enrol the GRUB signing key in the Machine Owner Key (MOK)
database with `mokutil`; this is not covered in the main book.

## Platform Notes

- This is the primary development and CI target for the book.
- The `lib64` → `lib` symlink is required in the LFS tree for correct
  dynamic linker resolution; the cross-toolchain chapters create it.
- When building on an amd64 host natively (i.e. `LFS_TGT` matches the host
  triplet), the `--with-sysroot` GCC flag is critical to prevent the compiler
  from accidentally picking up host headers.
- Common test platforms: bare metal x86-64 desktop/server, QEMU/KVM
  (`-machine q35` or `-machine pc`), and cloud VMs (AWS x86_64, GCP, Azure).

## Bootloader

See [Bootloader Configuration — amd64](../part4-system-config/bootloaders.md#amd64--x86--grub-bios-or-efi).
