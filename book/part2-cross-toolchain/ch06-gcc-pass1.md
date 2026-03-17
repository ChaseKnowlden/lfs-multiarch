# Chapter 6 — GCC Pass 1

GCC pass 1 builds a cross-compiler targeting `$LFS_TGT`.  At this stage
it has no C library yet, so only the C compiler is built.

## 6.1 Preparation

```bash
tar -xf gcc-14.2.0.tar.xz
cd gcc-14.2.0

# GCC requires its support libraries inside the source tree
tar -xf ../mpfr-4.2.1.tar.xz && mv mpfr-4.2.1 mpfr
tar -xf ../gmp-6.3.0.tar.xz  && mv gmp-6.3.0  gmp
tar -xf ../mpc-1.3.1.tar.gz  && mv mpc-1.3.1  mpc
```

## 6.2 Architecture-Specific Preparation

**x86 only** — set the default 64-bit library directory name:
```bash
case $(uname -m) in
    x86_64) sed -e '/m64=/s/lib64/lib/' \
                -i.orig gcc/config/i386/t-linux64 ;;
esac
```

**arm (32-bit)** — fix multilib conflict:
```bash
sed -e '/mthumb-interwork/s/true/false/' -i.orig gcc/config/arm/linux-eabi.h
```

## 6.3 Configure & Build

```bash
mkdir -v build && cd build

../configure                                         \
    --target=$LFS_TGT                               \
    --prefix=$LFS/tools                             \
    --with-glibc-version=2.40                       \
    --with-sysroot=$LFS                             \
    --with-newlib                                   \
    --without-headers                               \
    --enable-default-pie                            \
    --enable-default-ssp                            \
    --disable-nls                                   \
    --disable-shared                                \
    --disable-multilib                              \
    --disable-threads                               \
    --disable-libatomic                             \
    --disable-libgomp                               \
    --disable-libquadmath                           \
    --disable-libssp                                \
    --disable-libvtv                                \
    --disable-libstdcxx                             \
    --enable-languages=c,c++                        \
    $LFS_GCC_EXTRA

make
make install
```

## 6.4 Create the Limits Header

```bash
cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
    $(dirname $($LFS_TGT-gcc -print-libgcc-file-name))/include/limits.h
```

## Arch Notes

| Arch   | Notable pass-1 behaviour                                                 |
|--------|--------------------------------------------------------------------------|
| alpha  | Add `-mieee` to `CFLAGS` if FP correctness issues appear at later stages |
| arm    | `--with-float=hard` propagated through `$LFS_GCC_EXTRA`                  |
| arm64  | No multilib; `--disable-multilib` correct                                |
| hppa   | GCC may warn about unsupported options; `--disable-werror` advised       |
| loong  | Requires GCC ≥ 12; ABI flag `--with-abi=lp64d` set via `$LFS_GCC_EXTRA` |
| m68k   | `--disable-multilib` important (many sub-arch variants exist)            |
| mips   | Set endianness via triplet (`mips` vs `mipsel`); ABI via `$LFS_GCC_EXTRA`|
| ppc    | `--enable-secureplt` needed on some kernels                              |
| ppc64  | ELFv2 ABI flag via `$LFS_GCC_EXTRA`; pass-1 builds `powerpc64le` cross   |
| riscv  | `--with-arch=rv64gc --with-abi=lp64d` via `$LFS_GCC_EXTRA`              |
| s390   | `--with-arch=z196` sets minimum z-Architecture level                    |
| sparc  | 64-bit target; `--with-cpu=ultrasparc` via `$LFS_GCC_EXTRA`             |
| x86    | 32-bit target; the sed above is NOT needed (only for 64-bit hosts)       |
