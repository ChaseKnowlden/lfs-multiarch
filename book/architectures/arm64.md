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

## Toolchain Version Requirements

| Tool     | Minimum version |
|----------|----------------|
| GCC      | 5.0            |
| Binutils | 2.25           |
| Linux    | 4.14           |
| Glibc    | 2.17           |

## ISA and ABI Baseline

This book targets **Armv8.0-A** (`--with-arch=armv8-a`), which is the lowest
common denominator for 64-bit Arm hardware and is supported by all AArch64
CPUs.

Key Armv8 extension levels:

| Profile  | Notable additions                              | Example hardware              |
|----------|------------------------------------------------|-------------------------------|
| v8.0-A   | Baseline, used here                            | Cortex-A53, Cortex-A57        |
| v8.1-A   | LSE atomics, RDMA                              | Cortex-A72, Neoverse N1       |
| v8.2-A   | SVE (optional), FP16                           | Cortex-A76, Apple M1          |
| v8.5-A+  | MTE, BTI (memory tagging, branch protection)   | Cortex-X2, Apple M2+          |

The **LP64** ABI uses 64-bit pointers and 64-bit `long`.  The alternative
ILP32 ABI (32-bit pointers in a 64-bit kernel) is not covered.

## Device Tree and Firmware

Most arm64 platforms require a Device Tree Blob (DTB) for the kernel to
discover hardware.  Build all in-tree DTBs with:

```bash
make ARCH=arm64 CROSS_COMPILE=${LFS_TGT}- dtbs
```

DTB files are installed to `/boot/dtbs/<kernel-version>/`.

**Firmware options by platform type:**

| Platform type        | Firmware chain                              |
|----------------------|---------------------------------------------|
| Server (SBSA/SBBR)   | UEFI (Tianocore EDK2) → GRUB EFI → kernel  |
| Embedded (no UEFI)   | U-Boot → kernel via `booti`                 |
| Embedded (UEFI stub) | U-Boot EDK2 → GRUB EFI → kernel            |
| Apple (Asahi)        | m1n1 → U-Boot → GRUB EFI → kernel          |

## Building on an x86-64 Host

Install a cross-compiler targeting `aarch64-linux-gnu`:

- **Debian/Ubuntu**: `apt install gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu`
- **Fedora**: `dnf install gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu`

Then set `LFS_TGT=aarch64-lfs-linux-gnu` and proceed with the cross-toolchain
chapters normally.

## Platform Notes

- AArch64 systems are the second primary Tier 1 target alongside amd64.
- Most modern server-grade hardware (Ampere Altra, AWS Graviton 2/3/4, Apple
  M-series via Asahi) boots via UEFI; use GRUB EFI.
- Embedded boards (Raspberry Pi 4/5, Rock 5, etc.) use U-Boot; some expose
  UEFI via an EDK2 firmware layer, enabling the same GRUB EFI path.
- **ILP32 variant**: Not covered; the standard LP64 ABI is used throughout.
- Common test platforms: QEMU (`-M virt -cpu cortex-a57`), AWS Graviton,
  Raspberry Pi 4/5, Ampere Mt. Collins.

## Cross-Compilation Toolchain

### Binutils Pass 1

No architecture-specific flags are required.  The `aarch64-lfs-linux-gnu`
triplet is unambiguous; all aarch64 Linux targets use the same ELF64 LE
object format and the GNU assembler handles all standard Armv8 encodings
without extra flags.

### GCC Pass 1

The key flags for arm64:

| Flag | Purpose |
|------|---------|
| `--with-arch=armv8-a` | Targets the Armv8.0-A baseline; set via `$LFS_GCC_EXTRA` |
| `--disable-multilib` | aarch64 has no 32-bit multilib in this book; ILP32 is not built |
| `--with-newlib` / `--without-headers` | No C library yet at this stage |

There are no pre-configure sed steps required for arm64.  The standard
GCC pass 1 configure line from Chapter 6, with `$LFS_GCC_EXTRA` expanding
to `--with-arch=armv8-a`, is sufficient.

### Page Size Considerations

Glibc is built assuming the host and target share the same kernel page size.
The standard arm64 page size is 4 KiB.  If the target system uses a non-default
page size (16 KiB on Apple Silicon or Ampere Altra, 64 KiB on some HPC kernels),
the Glibc built here will not load correctly on that kernel.  For maximum
compatibility, build with the default 4 KiB page size and use a matching kernel
configuration (`CONFIG_ARM64_PAGE_SHIFT=12`).

### Glibc

No architecture-specific configure flags are needed for arm64 with the LP64
ABI.  The `--host=$LFS_TGT` triplet (`aarch64-lfs-linux-gnu`) is sufficient to
select the correct ABI.

The dynamic linker path for arm64 is:

```text
/lib/ld-linux-aarch64.so.1
```

No `lib64` symlink is needed; arm64 Glibc installs into `/lib` and `/usr/lib`
directly (unlike amd64, which uses `lib64`).

### Sanity Check

After building Glibc, verify the dynamic linker path:

```bash
echo 'int main(){}' | $LFS_TGT-gcc -xc -
readelf -l a.out | grep interpreter
```

Expected output:
```text
[Requesting program interpreter: /lib/ld-linux-aarch64.so.1]
```

## Bootloader

See [Bootloader Configuration — arm64](../part4-system-config/bootloaders.md#arm64--grub-efi).
