# Introduction

Welcome to the **Multi-Architecture Linux From Scratch** book.

This book teaches you how to build a complete Linux system entirely from source
code, targeting the following CPU architectures:

| Short name | Full description                          |
|------------|-------------------------------------------|
| alpha      | DEC/HP Alpha (64-bit, little-endian)      |
| amd64      | x86-64 / AMD64 (64-bit, little-endian)    |
| arm        | ARM 32-bit (ARMv7+, hard-float)           |
| arm64      | AArch64 / ARM 64-bit                      |
| hppa       | PA-RISC (32-bit, big-endian)              |
| loong      | LoongArch64                               |
| m68k       | Motorola 68000 series (32-bit, big-endian)|
| mips       | MIPS (32/64-bit, bi-endian)               |
| ppc        | PowerPC 32-bit (big-endian)               |
| ppc64      | PowerPC 64-bit (ELFv2 LE or ELFv1 BE)    |
| riscv      | RISC-V 64-bit (rv64gc)                    |
| s390       | IBM s390x (64-bit, big-endian)            |
| sparc      | SPARC 64-bit (big-endian)                 |
| x86        | IA-32 / i686 (32-bit, little-endian)      |

## How This Book is Organised

The book is divided into architecture-agnostic core chapters and
per-architecture supplement sections.  Where a step differs between
architectures, an **Arch Note** callout marks the variation.

## Prerequisites

- Familiarity with a Linux command line
- A working Linux host system (see Chapter 1 for minimum versions)
- A host capable of cross-compiling for your target (or QEMU emulation)
- Patience
