# Alpha Supplement

| Variable         | Value                        |
|------------------|------------------------------|
| `LFS_TGT`        | `alpha-lfs-linux-gnu`        |
| `LFS_ARCH_LINUX` | `alpha`                      |
| `LFS_BITS`       | 64                           |
| `LFS_ENDIAN`     | little                       |
| `LFS_ABI`        | default                      |
| `LFS_GCC_EXTRA`  | `--with-arch=ev6`            |
| Bootloader       | aboot (SRM)                  |
| Tier             | 3 — experimental             |

## Platform Notes

- Requires a system with SRM console firmware.  Requires the `aboot` package.
- Add `-mieee` to `CFLAGS` when building any package that performs
  floating-point arithmetic to avoid IEEE non-compliance traps.
- GCC targets `ev6` (21264) by default; adjust `--with-arch` for older chips
  (`ev5`, `ev56`, `pca56`).

## Known Issues

- Some `autoconf` tests hang on Alpha; adding `--cache-file=/dev/null` works
  around stale cache assumptions.
- OpenSSL assembly optimisations may need `--no-asm` on very old hardware.

## Bootloader (aboot)

See [Bootloader Configuration — alpha](../part4-system-config/bootloaders.md#alpha).
