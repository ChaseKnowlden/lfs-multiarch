# ppc64 (PowerPC 64-bit) Supplement

## Primary: ppc64le (ELFv2, little-endian)

| Variable         | Value                                          |
|------------------|------------------------------------------------|
| `LFS_TGT`        | `powerpc64le-lfs-linux-gnu`                    |
| `LFS_ARCH_LINUX` | `powerpc`                                      |
| `LFS_BITS`       | 64                                             |
| `LFS_ENDIAN`     | little                                         |
| `LFS_ABI`        | ELFv2                                          |
| `LFS_GCC_EXTRA`  | `--with-cpu=power8 --with-abi=elfv2`           |
| Bootloader       | GRUB (OPAL/PowerNV) or GRUB-IEEE1275           |
| Tier             | 2 — builds, limited testing                    |

## Secondary: ppc64 (ELFv1, big-endian)

Change `LFS_TGT` to `powerpc64-lfs-linux-gnu` and `LFS_GCC_EXTRA` to
`--with-cpu=power7` (ELFv1 is used on POWER7 and older by default).

## Platform Notes

- **ELFv2 vs ELFv1**: Modern POWER8+ LE systems use ELFv2; legacy POWER7/BE
  systems use ELFv1.  The ABI is not compatible — choose one and be consistent
  through the entire build.
- `ppc64le` is the mainstream target (IBM POWER8–POWER10, Raptor Talos/Blackbird).
- Both variants share the `powerpc` kernel ARCH value.
- POWER9/POWER10 machines boot via OPAL firmware (Petitboot bootloader on top
  of a small Linux); GRUB is loaded from within that environment.

## Bootloader

See [Bootloader Configuration — ppc64](../part4-system-config/bootloaders.md#ppc64--grub-opal--ieee-1275).
