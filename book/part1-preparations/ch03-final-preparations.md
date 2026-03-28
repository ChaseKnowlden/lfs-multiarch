# Chapter 3 — Final Preparations

## 3.1 Setting the Target Architecture

Choose your target architecture and set the following variables in your shell
(add them to `~/.bashrc` for persistence across sessions):

```bash
# ---- Edit these two lines for your target ----
export LFS_ARCH=amd64          # one of the 14 short names
export LFS=/mnt/lfs            # mount point for the LFS partition
# ----------------------------------------------
```

Source the arch configuration file to set all remaining variables:

```bash
source $LFS/sources/lfs-arch-config.sh $LFS_ARCH
```

The config script sets:

| Variable         | Example (amd64)                 | Description                       |
|------------------|---------------------------------|-----------------------------------|
| `LFS_TGT`        | `x86_64-lfs-linux-gnu`          | Target triplet                    |
| `LFS_ARCH_LINUX` | `x86_64`                        | Kernel `ARCH=` value              |
| `LFS_BITS`       | `64`                            | Pointer width                     |
| `LFS_ENDIAN`     | `little`                        | Byte order                        |
| `LFS_ABI`        | `LP64`                          | ABI descriptor                    |
| `CC`             | `gcc`                           | Host C compiler                   |
| `CXX`            | `g++`                           | Host C++ compiler                 |

## 3.2 Creating the LFS User

```bash
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs
passwd lfs
chown -v lfs $LFS/{usr{,/*},lib,var,etc,bin,sbin,tools}
case $(uname -m) in
  x86_64 | aarch64 | riscv64 ) chown -v lfs $LFS/lib64 ;;
esac
su - lfs
```

## 3.3 Setting Up the Build Environment

As user `lfs`, create `~/.bash_profile`:

```bash
exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
```

And `~/.bashrc`:

```bash
set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
LFS_TGT=$(cat $LFS/sources/.lfs_tgt)
PATH=/usr/bin
if [ ! -L /bin ]; then PATH=/bin:$PATH; fi
PATH=$LFS/tools/bin:$PATH
CONFIG_SITE=$LFS/usr/share/config.site
export LFS LC_ALL LFS_TGT PATH CONFIG_SITE
```

> **Arch Note — lib64 symlink:** On 64-bit architectures (amd64, arm64,
> riscv, ppc64, loong, alpha, sparc, s390) that use a separate `lib64`
> directory, the book creates `$LFS/lib64` and a compatibility symlink.
> On 32-bit architectures (arm, x86, ppc, m68k, mips, hppa) this is not
> needed.
