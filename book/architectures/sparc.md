# sparc (SPARC 64-bit) Supplement

| Variable         | Value                           |
|------------------|---------------------------------|
| `LFS_TGT`        | `sparc64-lfs-linux-gnu`         |
| `LFS_ARCH_LINUX` | `sparc`                         |
| `LFS_BITS`       | 64                              |
| `LFS_ENDIAN`     | big                             |
| `LFS_ABI`        | LP64                            |
| `LFS_GCC_EXTRA`  | `--with-cpu=ultrasparc`         |
| Bootloader       | SILO or OpenBoot PROM direct    |
| Tier             | 3 — experimental                |

## Platform Notes

- Target hardware: Sun Ultra workstations and servers (Ultra 5/10/60/80,
  Sun Blade, Sun Fire V-series).
- SPARC systems use OpenBoot PROM (OBP) firmware; SILO is the standard
  secondary bootloader for Linux.
- The kernel `ARCH` is `sparc` for both 32 and 64-bit; use `SPARC64=y` in
  the kernel config for 64-bit.
- A 64-bit kernel can run a 32-bit userland, but this book builds a pure
  64-bit (`sparc64`) userland.

## CPU Tuning

```bash
# UltraSPARC I/II (safe baseline for most systems)
--with-cpu=ultrasparc

# UltraSPARC III+
--with-cpu=ultrasparc3

# SPARC T-series (Niagara)
--with-cpu=niagara
```

## Bootloader

See [Bootloader Configuration — sparc](../part4-system-config/bootloaders.md#sparc--silo).
