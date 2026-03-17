# Chapter 20 — LFS Bootscripts

The LFS bootscripts provide a System V-style init framework.

> **Work in progress.**

## Overview

The bootscripts are installed by the `lfs-bootscripts` package (Chapter 17).
This chapter documents how to configure and customise them.

## Key Scripts

| Script                        | Purpose                              |
|-------------------------------|--------------------------------------|
| `/etc/rc.d/init.d/checkfs`    | fsck on boot                         |
| `/etc/rc.d/init.d/mountfs`    | Mount local filesystems              |
| `/etc/rc.d/init.d/udev`       | Start udev device manager            |
| `/etc/rc.d/init.d/network`    | Bring up network interfaces          |
| `/etc/rc.d/init.d/syslog`     | Start system logger                  |

## Run Levels

| Level | Meaning                   |
|-------|---------------------------|
| 0     | Halt                      |
| 1     | Single user               |
| 2     | Multi-user (no network)   |
| 3     | Multi-user with network   |
| 5     | Multi-user + GUI          |
| 6     | Reboot                    |
