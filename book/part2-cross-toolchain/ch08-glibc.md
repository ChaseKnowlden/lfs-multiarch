# Chapter 8 — Glibc

Glibc is the GNU C Library — the most critical component of the cross-toolchain.
It provides the C runtime, syscall wrappers, and the dynamic linker.

## 8.1 Preparation

```bash
tar -xf glibc-2.40.tar.xz
cd glibc-2.40

# Create a symlink for LSB compliance
case $(uname -m) in
    i?86) ln -sfv ld-linux.so.2 $LFS/lib/ld-lsb.so.3 ;;
esac

# Apply architecture-specific patches if present
[ -d $LFS/sources/patches/$LFS_ARCH ] && \
    for p in $LFS/sources/patches/$LFS_ARCH/glibc-*.patch; do
        patch -Np1 -i "$p"
    done

mkdir -v build && cd build
echo "rootsbindir=/usr/sbin" > configparms
```

## 8.2 Configure

```bash
../configure                              \
    --prefix=/usr                         \
    --host=$LFS_TGT                       \
    --build=$(../scripts/config.guess)    \
    --enable-kernel=4.19                  \
    --with-headers=$LFS/usr/include       \
    --disable-nscd                        \
    libc_cv_slibdir=/usr/lib
```

> **Arch Note — arm (32-bit):** Add `--enable-obsolete-rpc` if building for
> older ARM boards that require RPC/NIS support.

> **Arch Note — mips:** Add `--with-fp=soft` for soft-float configurations,
> or `--with-fp=hard` for hard-float.  Ensure the ABI matches `$LFS_ABI`.

> **Arch Note — ppc64 (big-endian):** The `slibdir` may differ; confirm
> with `--libdir=/usr/lib64` if using a multilib layout.

> **Arch Note — loong:** Requires glibc 2.38+ for LoongArch support.
> Check `patches/loong/` for any backports needed against older glibc.

> **Arch Note — riscv:** Requires glibc 2.27+ for RISC-V support.

> **Arch Note — alpha:** Pass `--without-fp` to fall back to software
> float on systems without the FPU (uncommon but possible with `-mieee`).

## 8.3 Build and Install

```bash
make
make DESTDIR=$LFS install

# Fix a hard-coded path in the ldd script
sed '/RTLDLIST=/s@/usr@@g' -i $LFS/usr/bin/ldd
cd ../..
rm -rf glibc-2.40
```

## 8.4 Sanity Check

```bash
echo 'int main(){}' | $LFS_TGT-gcc -xc -
readelf -l a.out | grep ld-linux
rm -v a.out
```

The output should show the correct interpreter for your target:

| Arch   | Dynamic linker path                       |
|--------|-------------------------------------------|
| alpha  | `/lib/ld-linux.so.2`                      |
| amd64  | `/lib64/ld-linux-x86-64.so.2`             |
| arm    | `/lib/ld-linux-armhf.so.3`                |
| arm64  | `/lib/ld-linux-aarch64.so.1`              |
| hppa   | `/lib/ld.so.1`                            |
| loong  | `/lib64/ld-linux-loongarch-lp64d.so.1`    |
| m68k   | `/lib/ld.so.1`                            |
| mips   | `/lib/ld.so.1`                            |
| ppc    | `/lib/ld.so.1`                            |
| ppc64  | `/lib64/ld64.so.2`                        |
| riscv  | `/lib/ld-linux-riscv64-lp64d.so.1`        |
| s390   | `/lib/ld64.so.1`                          |
| sparc  | `/lib64/ld-linux.so.2`                    |
| x86    | `/lib/ld-linux.so.2`                      |
