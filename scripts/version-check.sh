#!/bin/bash
# version-check.sh — verify host system meets LFS build requirements.
# Based on the LFS upstream version-check.sh, extended for multi-arch.

export LC_ALL=C

bail() { echo "FATAL: $1"; exit 1; }
warn() { echo "WARNING: $1"; }
ok()   { echo "OK:      $1"; }

# Bash 3.2+
bash --version | head -1 | grep -E 'version [3-9]\.' > /dev/null \
    && ok "bash $(bash --version | head -1 | awk '{print $4}')" \
    || bail "bash >= 3.2 required"

# /bin/sh must not be dash for some build scripts
if [ -h /bin/sh ]; then
    SHNAME=$(readlink -f /bin/sh | xargs basename)
    [ "$SHNAME" = "bash" ] && ok "/bin/sh -> bash" \
        || warn "/bin/sh -> $SHNAME (bash preferred)"
fi

# ld (binutils)
ld --version | head -1 | awk '{print $NF}' | \
    awk -F. '{if($1>=2 && ($1>2 || $2>=13)) print "OK: binutils "$0; else print "FAIL: binutils "$0}'

# bison 2.7+
bison --version | head -1 | awk '{
    split($NF,v,".");
    if(v[1]>2 || (v[1]==2 && v[2]>=7)) print "OK: bison "$NF;
    else print "FAIL: bison "$NF" (need 2.7+)"
}'

# gcc / g++
for cc in gcc g++; do
    $cc --version | head -1 | awk -v cc=$cc '{
        split($NF,v,".");
        if(v[1]>=5) print "OK: "cc" "$NF;
        else print "FAIL: "cc" "$NF" (need 5+)"
    }'
done

# glibc 2.11+
ldd --version | head -1 | awk '{
    split($NF,v,".");
    if(v[1]>2 || (v[1]==2 && v[2]>=11)) print "OK: glibc "$NF;
    else print "FAIL: glibc "$NF" (need 2.11+)"
}'

# grep 2.5.1+
grep --version | head -1 | awk '{
    split($NF,v,".");
    if(v[1]>2 || (v[1]==2 && v[2]>=5)) print "OK: grep "$NF;
    else print "FAIL: grep "$NF
}'

# make 4.0+
make --version | head -1 | awk '{
    split($3,v,".");
    if(v[1]>=4) print "OK: make "$3;
    else print "FAIL: make "$3" (need 4.0+)"
}'

# perl 5.8.8+
perl -V:version 2>/dev/null | sed "s/version='\(.*\)';/\1/" | awk '{
    split($0,v,".");
    if(v[1]>=6 || (v[1]==5 && v[2]>8) || (v[1]==5 && v[2]==8 && v[3]>=8))
        print "OK: perl "$0;
    else print "FAIL: perl "$0" (need 5.8.8+)"
}'

# python3 3.4+
python3 --version 2>&1 | awk '{
    split($2,v,".");
    if(v[1]==3 && v[2]>=4) print "OK: "$0;
    else print "FAIL: "$0" (need 3.4+)"
}'

# xz
xz --version | head -1 | awk '{print "OK: xz "$4}'

# qemu (optional)
for q in qemu-system-x86_64 qemu-system-aarch64 qemu-system-riscv64 \
          qemu-system-ppc64 qemu-system-mips qemu-system-sparc64; do
    if command -v $q &>/dev/null; then
        ok "$q $($q --version 2>&1 | head -1 | awk '{print $NF}')"
    else
        warn "$q not found (optional, needed for emulated builds)"
    fi
done
