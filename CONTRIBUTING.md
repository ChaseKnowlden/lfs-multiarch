# Contributing

Thank you for helping build the Multi-Arch LFS Book.

## Arch Maintainers

Each architecture should have at least one primary maintainer and one backup.
To volunteer, open an issue with the title `[arch maintainer] <arch>`.

| Arch   | Primary | Backup |
|--------|---------|--------|
| alpha  | TBD     | TBD    |
| amd64  | TBD     | TBD    |
| arm    | TBD     | TBD    |
| arm64  | TBD     | TBD    |
| hppa   | TBD     | TBD    |
| loong  | TBD     | TBD    |
| m68k   | TBD     | TBD    |
| mips   | TBD     | TBD    |
| ppc    | TBD     | TBD    |
| ppc64  | TBD     | TBD    |
| riscv  | TBD     | TBD    |
| s390   | TBD     | TBD    |
| sparc  | TBD     | TBD    |
| x86    | TBD     | TBD    |

## How to Contribute

1. Fork the repository and create a branch named `<arch>/<short-description>` or `core/<short-description>`.
2. Make your changes.
3. Run `scripts/version-check.sh` on a relevant host if touching build instructions.
4. Open a pull request against `main`.

## Book Source Format

Currently Markdown.  A future milestone may migrate to DocBook XML for
compatibility with LFS upstream tooling — see ROADMAP Milestone 6.

## Arch Notes Convention

When a step differs per architecture, use this callout format:

```
> **Arch Note — <arch>:** <description of difference>
```

Or for multi-arch tables, insert an "Arch Notes" table at the end of the
section.

## Commit Style

```
<arch|core>: <short imperative summary>

<optional body>
```

Examples:
- `riscv: add OpenSBI firmware section to bootloader chapter`
- `core: update GCC to 14.2.0`
- `m68k: document Atari bootstrap procedure`

## Testing

- Tier 1 arches (amd64, arm64, x86): test in a VM before submitting.
- Tier 2 arches: QEMU emulation encouraged.
- Tier 3 arches: document test method used (real hardware, QEMU, etc.).
