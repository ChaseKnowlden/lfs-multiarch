# Patches

Architecture-specific patches are stored here, one directory per architecture.

## Directory Layout

```
patches/
├── README.md        ← this file
├── alpha/
├── amd64/
├── arm/
├── arm64/
├── hppa/
├── loong/
├── m68k/
├── mips/
├── ppc/
├── ppc64/
├── riscv/
├── s390/
├── sparc/
└── x86/
```

## Naming Convention

```
<package>-<version>-<description>-<N>.patch
```

Examples:
- `glibc-2.40-hppa-signal-frames-1.patch`
- `gcc-14.2.0-alpha-ieee-float-1.patch`
- `binutils-2.43.1-mips-fix-got-overflow-1.patch`

## Policy

1. Prefer patches already accepted upstream or in Debian/Fedora.
2. Include a comment block at the top of each patch:
   ```
   # Origin: upstream commit <sha> / Debian #<bug> / ...
   # Applies-to: <package> <version>
   # Purpose: <one-line description>
   ```
3. Open a PR to add or update a patch; the relevant arch maintainer must approve.
4. Remove patches that are no longer needed (absorbed upstream).
