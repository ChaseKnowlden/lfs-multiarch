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
22. Shadow
23. GCC (final)
24. Ncurses
25. Sed
26. Psmisc
27. Gettext
28. Bison
29. Grep
30. Bash
31. Libtool
32. GDBM
33. Gperf
34. Expat
35. Inetutils
36. Less
37. Perl
38. XML::Parser
39. Intltool
40. Autoconf
41. Automake
42. OpenSSL
43. Kmod
44. Elfutils (libelf)
45. Libffi
46. Python
47. Flit-core
48. Wheel
49. Setuptools
50. Ninja
51. Meson
52. Coreutils
53. Check
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
