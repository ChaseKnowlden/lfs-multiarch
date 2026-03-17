# Chapter 5 — Binutils Pass 1

Cross-binutils provides the linker and assembler that target `$LFS_TGT`.
This is always the first package built.

## 5.1 Installation

```bash
tar -xf binutils-2.43.1.tar.xz
cd binutils-2.43.1
mkdir -v build && cd build

../configure                   \
    --prefix=$LFS/tools        \
    --with-sysroot=$LFS        \
    --target=$LFS_TGT          \
    --disable-nls              \
    --enable-gprofng=no        \
    --disable-werror           \
    --enable-new-dtags         \
    --enable-default-hash-style=gnu

make
make install
cd ../..
rm -rf binutils-2.43.1
```

## Arch Notes

| Arch  | Extra configure flags                        | Notes                                      |
|-------|----------------------------------------------|--------------------------------------------|
| alpha | (none)                                       |                                            |
| hppa  | `--disable-werror` (already included above)  | Upstream warnings treated as errors on PA  |
| m68k  | (none)                                       |                                            |
| mips  | `--enable-targets=mips-linux-gnu,mipsel-…`   | Only if building bi-endian tools           |
| ppc64 | `--enable-ld=default --enable-gold`          | gold linker useful for large C++ projects  |
| s390  | (none)                                       |                                            |
| sparc | (none)                                       |                                            |

> **Verification:** After installation you should find
> `$LFS/tools/bin/$LFS_TGT-ld` and `$LFS/tools/bin/$LFS_TGT-as`.
