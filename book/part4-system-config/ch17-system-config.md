# Chapter 17 — System Configuration Basics

## 17.1 LFS-Bootscripts

```bash
tar -xf lfs-bootscripts-20240825.tar.xz
cd lfs-bootscripts-20240825
make install
cd ..
```

## 17.2 Udev Rules

```bash
bash /usr/lib/udev/init-net-rules.sh
```

## 17.3 The /etc/inittab File

```bash
cat > /etc/inittab << "EOF"
id:3:initdefault:

si::sysinit:/etc/rc.d/init.d/rc S

l0:0:wait:/etc/rc.d/init.d/rc 0
l1:S1:wait:/etc/rc.d/init.d/rc 1
l2:2:wait:/etc/rc.d/init.d/rc 2
l3:3:wait:/etc/rc.d/init.d/rc 3
l4:4:wait:/etc/rc.d/init.d/rc 4
l5:5:wait:/etc/rc.d/init.d/rc 5
l6:6:wait:/etc/rc.d/init.d/rc 6

ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now

su:S06:once:/sbin/sulogin
EOF
```

> **Arch Note — s390:** IBM Z systems use a different console device.
> Add `s0:12345:respawn:/sbin/agetty -L 9600 ttysclp0 vt100` to inittab.

## 17.4 Setting the System Clock

```bash
cat > /etc/sysconfig/clock << "EOF"
# Set to "UTC" or "localtime"
UTC=1
EOF
```

## 17.5 Locale

```bash
locale -a        # list available locales on host
localedef -i en_US -f UTF-8 en_US.UTF-8

cat > /etc/profile << "EOF"
export LANG=en_US.UTF-8
EOF
```
