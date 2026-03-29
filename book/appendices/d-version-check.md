# Appendix D — Version Check Script

The `scripts/version-check.sh` script verifies that your host system meets
the minimum software requirements listed in Chapter 1.

## Usage

```bash
bash scripts/version-check.sh
```

## Sample Output (passing host)

```text
OK:      bash 5.2.37
OK:      /bin/sh -> bash
OK:      binutils 2.43.1
OK:      bison 3.8.2
OK:      gcc 14.2.0
OK:      g++ 14.2.0
OK:      glibc 2.40
OK:      grep 3.11
OK:      make 4.4.1
OK:      perl 5.40.0
OK:      python3 3.12.5
OK:      xz 5.6.2
WARNING: qemu-system-alpha not found (optional, needed for emulated builds)
OK:      qemu-system-x86_64 8.2.0
OK:      qemu-system-aarch64 8.2.0
```

## Source

See `scripts/version-check.sh` in the project root.
