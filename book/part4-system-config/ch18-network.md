# Chapter 18 — Network Configuration

## 18.1 Network Interface Names

Udev assigns predictable network interface names.  Check your interface name:

```bash
ip link
```

## 18.2 Static IP Configuration

```bash
cat > /etc/sysconfig/ifconfig.eth0 << "EOF"
ONBOOT=yes
IFACE=eth0
SERVICE=ipv4-static
IP=192.168.1.2
GATEWAY=192.168.1.1
PREFIX=24
BROADCAST=192.168.1.255
EOF
```

## 18.3 /etc/resolv.conf

```bash
cat > /etc/resolv.conf << "EOF"
nameserver 1.1.1.1
nameserver 8.8.8.8
EOF
```

## 18.4 /etc/hostname

```bash
echo "lfs-$(uname -m)" > /etc/hostname
```

## 18.5 /etc/hosts

```bash
cat > /etc/hosts << "EOF"
127.0.0.1  localhost
127.0.1.1  lfs
::1        localhost ip6-localhost ip6-loopback
EOF
```
