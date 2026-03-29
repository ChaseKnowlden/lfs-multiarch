# Chapter 14 — Entering the Chroot Environment

## 14.1 Changing Ownership

As root on the host, transfer ownership of `$LFS` to root:

```bash
chown -R root:root $LFS/{usr,lib,var,etc,bin,sbin,tools}
case $(uname -m) in
    *64 ) chown -R root:root $LFS/lib64 ;;
esac
```

## 14.2 Copying the QEMU Binary

Before entering the chroot, copy the QEMU user-mode binary into `$LFS` so
that `binfmt_misc` can find it after the pivot.  The binary name is set by
`arch-config.sh` and varies by distribution (e.g. `qemu-aarch64-static` on
Debian/Ubuntu, `qemu-aarch64` on Gentoo):

```bash
mkdir -pv $LFS/usr/bin
cp -v $(command -v $LFS_QEMU_STATIC) $LFS/usr/bin/
```

> **Note:** This binary is only needed during the build.  It is not part of
> the final LFS system and can be removed once the build is complete.

## 14.3 Entering the Chroot

`arch-chroot` from `arch-install-scripts` mounts the virtual filesystems
(`/dev`, `/proc`, `/sys`, `/run`) automatically and cleans them up on exit:

```bash
arch-chroot "$LFS" /usr/bin/env -i      \
    HOME=/root TERM=$TERM               \
    PS1='(lfs chroot) \u:\w\$ '        \
    PATH=/usr/bin:/usr/sbin             \
    MAKEFLAGS="-j$(nproc)"             \
    TESTSUITEFLAGS="-j$(nproc)"        \
    /bin/bash --login
```

## 14.4 Creating Directories

```bash
mkdir -pv /{boot,home,mnt,opt,srv}
mkdir -pv /etc/{opt,sysconfig}
mkdir -pv /lib/firmware
mkdir -pv /media/{floppy,cdrom}
mkdir -pv /usr/{,local/}{include,src}
mkdir -pv /usr/lib/locale
mkdir -pv /usr/local/{bin,lib,sbin}
mkdir -pv /usr/{,local/}share/{color,dict,doc,info,locale,man}
mkdir -pv /usr/{,local/}share/{misc,terminfo,zoneinfo}
mkdir -pv /usr/{,local/}share/man/man{1..8}
mkdir -pv /var/{cache,local,log,mail,opt,spool}
mkdir -pv /var/lib/{color,misc,locate}

install -dv -m 0750 /root
install -dv -m 1777 /tmp /var/tmp
```

> **Arch Note — 64-bit architectures:** Create the `lib64` symlink
> appropriate for your architecture if required by glibc:
> ```bash
> # amd64 / x86_64
> ln -sfv ../lib /usr/lib64
> # arm64
> ln -sfv ../lib /usr/lib64
> # Other 64-bit arches follow the same pattern
> ```

## 14.5 Creating Essential Files and Symlinks

```bash
ln -sv /proc/self/mounts /etc/mtab

cat > /etc/hosts << EOF
127.0.0.1  localhost $(hostname)
::1        localhost
EOF

cat > /etc/passwd << "EOF"
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/dev/null:/usr/bin/false
daemon:x:6:6:Daemon User:/dev/null:/usr/bin/false
nobody:x:65534:65534:Unprivileged User:/dev/null:/usr/bin/false
EOF

cat > /etc/group << "EOF"
root:x:0:
bin:x:1:daemon
sys:x:2:
kmem:x:3:
tape:x:4:
tty:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
cdrom:x:15:
adm:x:16:
messagebus:x:18:
input:x:24:
mail:x:34:
kvm:x:61:
uuidd:x:80:
wheel:x:97:
users:x:999:
nogroup:x:65534:
EOF

touch /var/log/{btmp,lastlog,faillog,wtmp}
chgrp -v utmp /var/log/lastlog
chmod -v 664  /var/log/lastlog
chmod -v 600  /var/log/btmp
```
