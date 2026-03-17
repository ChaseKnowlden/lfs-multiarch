# Chapter 9 — Libstdc++ Pass 1

Libstdc++ is the GNU C++ standard library.  Pass 1 builds a cross version
so that C++ programs can be cross-compiled in Part III.  It is built from
the GCC source tree.

## 9.1 Installation

```bash
# GCC source should still be unpacked from Chapter 6
cd gcc-14.2.0
mkdir -v build2 && cd build2

../libstdc++-v3/configure           \
    --host=$LFS_TGT                 \
    --build=$(../config.guess)      \
    --prefix=/usr                   \
    --disable-multilib              \
    --disable-nls                   \
    --disable-libstdcxx-pch         \
    --with-gxx-include-dir=/tools/$LFS_TGT/include/c++/14.2.0

make
make DESTDIR=$LFS install

# Remove libtool archives which are not needed
rm -v $LFS/usr/lib/lib{stdc++{,exp},supc++}.la
cd ../..
rm -rf gcc-14.2.0
```

## Arch Notes

No architecture-specific variations for this pass.  The `$LFS_TGT` triplet
set by `arch-config.sh` ensures the correct target is used throughout.
