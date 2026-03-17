# Chapter 10 — Introduction to Temporary Tools

The packages in this part are cross-compiled using the toolchain built in
Part II.  They are installed into `$LFS/usr` and will be used in the chroot
environment in Part IV.

## Purpose

These tools exist only to bootstrap the final system.  They do not need to
be optimised or complete — they just need to work well enough to build the
packages in Part IV from inside the chroot.

## Build Environment

Ensure the following are set before starting:

```bash
source scripts/arch-config.sh $LFS_ARCH
source ~/.bashrc    # reloads LFS environment variables
echo $LFS_TGT      # must print the correct triplet
```

## General Build Pattern

Most packages in Part III follow this pattern:

```bash
./configure --prefix=/usr   \
            --host=$LFS_TGT \
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install
```

Package-specific variations are noted in the following chapters.
