# hppa (PA-RISC) Supplement

| Variable         | Value                           |
|------------------|---------------------------------|
| `LFS_TGT`        | `hppa-lfs-linux-gnu`            |
| `LFS_ARCH_LINUX` | `parisc`                        |
| `LFS_BITS`       | 32                              |
| `LFS_ENDIAN`     | big                             |
| `LFS_ABI`        | default                         |
| `LFS_GCC_EXTRA`  | `--disable-werror`              |
| Bootloader       | PALO                            |
| Tier             | 3 — experimental                |

## Platform Notes

- Target hardware: HP 9000/700 and 9000/800 series workstations/servers.
- The kernel `ARCH` value is `parisc`, not `hppa` — always set
  `ARCH=parisc` for kernel builds.
- The boot partition must be type `f0` (PA-RISC Linux boot) for PALO.
- GCC produces many warnings treated as errors on PA-RISC; `--disable-werror`
  is required at multiple build stages.
- A 64-bit kernel can run a 32-bit userland (`hppa` triplet); this is the
  default and recommended configuration.

## Bootloader

See [Bootloader Configuration — hppa](../part4-system-config/bootloaders.md#hppa--palo).
