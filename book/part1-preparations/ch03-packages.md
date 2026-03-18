# Chapter 3 — Packages and Patches

All packages listed here are required for a complete LFS build.
Arch-specific patches are stored in `patches/<arch>/`.

## 3.1 Core Packages

| Package           | Version  | Size (approx) | URL / Notes                     |
|-------------------|----------|---------------|---------------------------------|
| Acl               | 2.3.2    | 356 KB        |                                 |
| Attr              | 2.5.2    | 352 KB        |                                 |
| Autoconf          | 2.72     | 1.3 MB        |                                 |
| Automake          | 1.18.1   | 1.5 MB        |                                 |
| Bash              | 5.3      | 10.7 MB       |                                 |
| Bc                | 7.0.3    | 441 KB        |                                 |
| Binutils          | 2.46.0   | 28.6 MB       |                                 |
| Bison             | 3.8.2    | 2.7 MB        |                                 |
| Bzip2             | 1.0.8    | 792 KB        |                                 |
| Coreutils         | 9.10     | 5.6 MB        |                                 |
| DejaGNU           | 1.6.3    | 608 KB        |                                 |
| Diffutils         | 3.12     | 1.5 MB        |                                 |
| E2fsprogs         | 1.47.4   | 9.3 MB        |                                 |
| Elfutils          | 0.194    | 8.8 MB        |                                 |
| Expat             | 2.7.5    | 440 KB        |                                 |
| Expect            | 5.45.4   | 616 KB        |                                 |
| File              | 5.47     | 1.0 MB        |                                 |
| Findutils         | 4.10.0   | 1.9 MB        |                                 |
| Flex              | 2.6.4    | 1.4 MB        |                                 |
| Flit-core         | 3.12.0   | 65 KB         | Python build backend            |
| Gawk              | 5.4.0    | 3.5 MB        |                                 |
| GCC               | 15.2.0   | 87 MB         |                                 |
| GDBM              | 1.26     | 1.1 MB        |                                 |
| Gettext           | 1.0      | 9.9 MB        |                                 |
| Glibc             | 2.43     | 18 MB         |                                 |
| GMP               | 6.3.0    | 1.9 MB        |                                 |
| Gperf             | 3.3      | 1.1 MB        |                                 |
| Grep              | 3.12     | 1.6 MB        |                                 |
| Groff             | 1.24.1   | 7.7 MB        |                                 |
| GRUB              | 2.14     | 6.4 MB        | amd64/arm64/x86/loong/riscv/ppc64|
| Gzip              | 1.14     | 820 KB        |                                 |
| Iana-Etc          | 20260310 | 576 KB        |                                 |
| Inetutils         | 2.7      | 1.5 MB        |                                 |
| Intltool          | 0.51.0   | 192 KB        |                                 |
| IPRoute2          | 6.19.0   | 895 KB        |                                 |
| Jinja2            | 3.1.6    | 240 KB        | Python (for Meson)              |
| Kbd               | 2.9.0    | 1.5 MB        |                                 |
| Kmod              | 34.2     | 564 KB        |                                 |
| Less              | 692      | 348 KB        |                                 |
| Libcap            | 2.77     | 180 KB        |                                 |
| Libffi            | 3.5.2    | 1.3 MB        |                                 |
| Libpipeline       | 1.5.8    | 956 KB        |                                 |
| Libtool           | 2.5.4    | 996 KB        |                                 |
| Libxcrypt         | 4.5.2    | 540 KB        |                                 |
| Linux kernel      | 6.19.8   | 136 MB        |                                 |
| LZ4               | 1.10.0   | 1.4 MB        |                                 |
| M4                | 1.4.21   | 1.6 MB        |                                 |
| Make              | 4.4.1    | 2.3 MB        |                                 |
| Man-DB            | 2.13.1   | 1.9 MB        |                                 |
| Man-Pages         | 6.17     | 1.8 MB        |                                 |
| MarkupSafe        | 3.0.3    | 20 KB         | Python (for Meson)              |
| Meson             | 1.10.2   | 2.2 MB        |                                 |
| MPC               | 1.3.1    | 756 KB        |                                 |
| MPFR              | 4.2.2    | 1.5 MB        |                                 |
| Ncurses           | 6.6      | 3.6 MB        |                                 |
| Ninja             | 1.13.2   | 228 KB        |                                 |
| OpenSSL           | 3.6.1    | 17.8 MB       |                                 |
| packaging         | 26.0     | 148 KB        | Python                          |
| Patch             | 2.8      | 766 KB        |                                 |
| PCRE2             | 10.47    | 1.9 MB        |                                 |
| Perl              | 5.42.1   | 13.2 MB       |                                 |
| Pkgconf           | 2.5.1    | 492 KB        |                                 |
| Procps-ng         | 4.0.6    | 1.4 MB        |                                 |
| Psmisc            | 23.7     | 356 KB        |                                 |
| Python            | 3.14.3   | 20.0 MB       |                                 |
| Readline          | 8.3      | 2.9 MB        |                                 |
| Sed               | 4.9      | 1.3 MB        |                                 |
| Setuptools        | 82.0.1   | 2.2 MB        |                                 |
| Shadow            | 4.19.4   | 1.8 MB        |                                 |
| SQLite            | 3.51.3   | 3.2 MB        |                                 |
| Sysklogd          | 2.7.2    | 489 KB        |                                 |
| Sysvinit          | 3.14     | 236 KB        |                                 |
| Tar               | 1.35     | 2.6 MB        |                                 |
| Tcl               | 8.6.17   | 11.1 MB       |                                 |
| Texinfo           | 7.3      | 5.0 MB        |                                 |
| Udev (systemd)    | 260      | 16.2 MB       | udev rules only                 |
| Util-linux        | 2.41.3   | 8.3 MB        |                                 |
| Vim               | 9.2.0192 | 17.6 MB       |                                 |
| Wheel             | 0.46.3   | 96 KB         | Python                          |
| XML::Parser       | 2.47     | 272 KB        | Perl                            |
| Xz                | 5.8.2    | 1.5 MB        |                                 |
| Zlib              | 1.3.2    | 1.1 MB        |                                 |
| Zstd              | 1.5.7    | 2.3 MB        |                                 |

## 3.2 Architecture-Specific Packages

| Package     | Arch(es)             | Purpose                                  |
|-------------|----------------------|------------------------------------------|
| aboot       | alpha                | SRM-based bootloader                     |
| PALO        | hppa                 | PA-RISC bootloader                       |
| Yaboot      | ppc                  | OpenFirmware bootloader (32-bit PPC)     |
| OpenSBI     | riscv                | RISC-V M-mode firmware                   |
| SILO        | sparc                | SPARC bootloader                         |
| zipl        | s390                 | IBM Z bootloader                         |
| dtc         | arm, arm64, riscv    | Device Tree compiler                     |
| u-boot      | arm, arm64, riscv    | Embedded bootloader (optional)           |

## 3.3 Optional / Test Packages

| Package     | Purpose                                      |
|-------------|----------------------------------------------|
| DejaGNU     | GCC test suite runner                        |
| Expect      | GCC test suite dependency                    |
| Tcl         | GCC test suite dependency                    |

## 3.4 Patches

Architecture-specific patches live in `patches/<arch>/`.
See `patches/README.md` for the naming convention and update policy.
