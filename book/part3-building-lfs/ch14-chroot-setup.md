# Chapter 14 — Entering the Chroot Environment

## 14.1 Changing Ownership

As root on the host, transfer ownership of `$LFS` to root:

```bash
chown -R root:root $LFS/{usr,lib,var,etc,bin,sbin,tools}
case $(uname -m) in
    *64 ) chown -R root:root $LFS/lib64 ;;
esac
```

## 14.2 Mounting Virtual Filesystems

```bash
mkdir -pv $LFS/{dev,proc,sys,run}
mount -v --bind /dev $LFS/dev
mount -v --bind /dev/pts $LFS/dev/pts
mount -vt proc proc $LFS/proc
mount -vt sysfs sysfs $LFS/sys
mount -vt tmpfs tmpfs $LFS/run
if [ -h $LFS/dev/shm ]; then
    install -v -d -m 1777 $LFS$(realpath /dev/shm)
else
    mount -vt tmpfs -o nosuid,nodev tmpfs $LFS/dev/shm
fi
```

## 14.3 Entering the Chroot

```bash
chroot "$LFS" /usr/bin/env -i              \
    HOME=/root TERM=$TERM                   \
    PS1='(lfs chroot) \u:\w\$ '            \
    PATH=/usr/bin:/usr/sbin                 \
    MAKEFLAGS="-j$(nproc)"                  \
    TESTSUITEFLAGS="-j$(nproc)"             \
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
