# ppc (PowerPC 32-bit) Supplement

| Variable         | Value                                        |
|------------------|----------------------------------------------|
| `LFS_TGT`        | `powerpc-lfs-linux-gnu`                      |
| `LFS_ARCH_LINUX` | `powerpc`                                    |
| `LFS_BITS`       | 32                                           |
| `LFS_ENDIAN`     | big                                          |
| `LFS_ABI`        | default                                      |
| `LFS_GCC_EXTRA`  | `--with-cpu=powerpc --enable-secureplt`      |
| Bootloader       | Yaboot (OpenFirmware) or GRUB-IEEE1275       |
| Tier             | 2 — builds, limited testing                  |

## Platform Notes

- Target hardware: Apple PowerPC Macs (G3, G4), IBM RS/6000, PowerMac G4 towers.
- `--enable-secureplt` is needed on some kernels to avoid a GOT overflow
  with large binaries.
- OpenFirmware (OF) machines use `yaboot`; non-OF machines may use GRUB
  with the `powerpc-ieee1275` GRUB target.
- The `powerpc` kernel `ARCH` value is shared with ppc64.

## G3 vs G4 Tuning

```bash
# G3 (750)
--with-cpu=750

# G4 (7400)
--with-cpu=7400

# Generic (safe minimum)
--with-cpu=powerpc
```

## Bootloader

See [Bootloader Configuration — ppc](../part4-system-config/bootloaders.md#ppc-32-bit--yaboot-openfirmware).
