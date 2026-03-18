# Chapter 16 — System Package Installation

This chapter installs all final system packages inside the chroot.
Packages are built in the order listed — dependency order matters.

> **Work in progress.** Each section will be expanded with configure flags,
> arch notes, and test suite results.

## Build Order

1. Glibc (final)
2. Zlib
3. Bzip2
4. Xz
5. Zstd
6. File
7. Readline
8. M4
9. Bc
10. Flex
11. Tcl
12. Expect
13. DejaGNU
14. Pkgconf
15. Binutils (final)
16. GMP
17. MPFR
18. MPC
19. Attr
20. Acl
21. Libcap
22. Libxcrypt
23. Shadow
24. GCC (final)
25. Ncurses
26. Sed
27. Psmisc
28. Gettext
29. Bison
30. Grep
31. Bash
32. Libtool
33. GDBM
34. Gperf
35. Expat
36. Inetutils
37. Less
38. Perl
39. XML::Parser
40. Intltool
41. Autoconf
42. Automake
43. OpenSSL
44. Kmod
45. Elfutils (libelf)
46. Libffi
47. Python
48. Flit-core
49. Wheel
50. Setuptools
51. Ninja
52. Meson
53. Coreutils
54. Diffutils
55. Gawk
56. Findutils
57. Groff
58. GRUB *(arch-specific — see [Bootloader Configuration](../part4-system-config/bootloaders.md))*
59. Gzip
60. IPRoute2
61. Kbd
62. Libpipeline
63. Make
64. Patch
65. Tar
66. Texinfo
67. Vim
68. MarkupSafe
69. Jinja2
70. Udev
71. Man-DB
72. Procps-ng
73. Util-linux
74. E2fsprogs
75. Sysklogd
76. Sysvinit
