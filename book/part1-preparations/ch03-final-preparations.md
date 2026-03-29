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
| `LFS_QEMU_STATIC`| `qemu-x86_64-static`            | QEMU user-static binary name      |

## 3.2 Setting Up QEMU User-Mode Emulation

For any target architecture that differs from the host, the host kernel must be
able to transparently execute foreign-architecture binaries inside the chroot.
This is done with a statically-linked `qemu-<arch>-static` binary registered
via `binfmt_misc`.

### 3.2.1 Verify binfmt_misc is active

```bash
mount | grep binfmt_misc
# or, if not yet mounted:
mount -t binfmt_misc binfmt_misc /proc/sys/fs/binfmt_misc
```

Most systemd and OpenRC hosts mount this automatically at boot.

### 3.2.2 Register the QEMU handler

Many distributions ship a ready-made registration package
(e.g. `qemu-user-static` on Debian/Ubuntu, `qemu-user-binfmt` on Arch).
Installing it will register all supported architectures automatically.

To register a single architecture manually (example: arm64):

```bash
echo ':qemu-aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-aarch64-static:F' \
  > /proc/sys/fs/binfmt_misc/register
```

The `F` flag (fix-binary) keeps the interpreter path valid after the chroot
pivot — it is required here.

### 3.2.3 Copy the static binary into the chroot

The QEMU binary must be present inside `$LFS` at the same absolute path
registered with `binfmt_misc`.  The binary name varies by distribution:

| Distribution          | Binary name example      |
|-----------------------|--------------------------|
| Debian, Ubuntu        | `qemu-aarch64-static`    |
| Gentoo, Arch, others  | `qemu-aarch64`           |

`arch-config.sh` detects which name is present on your host and sets
`LFS_QEMU_STATIC` accordingly.  If neither is found it will warn you.

```bash
# Determine the binary name for your target (set by arch-config.sh)
# e.g. LFS_QEMU_STATIC=qemu-aarch64-static
mkdir -pv $LFS/usr/bin
cp -v /usr/bin/$LFS_QEMU_STATIC $LFS/usr/bin/
```

Verify the registration works before entering the chroot:

```bash
file $LFS/usr/bin/$LFS_QEMU_STATIC
# should report: statically linked
```

> **Note:** The binary only needs to remain in `$LFS/usr/bin` while building
> inside the chroot.  It is not part of the final LFS system and can be removed
> after the build is complete.

## 3.3 Creating the LFS User

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

## 3.4 Setting Up the Build Environment

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
