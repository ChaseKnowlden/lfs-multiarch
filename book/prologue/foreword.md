# Foreword

This book is a fork and extension of the Linux From Scratch project,
targeting fourteen CPU architectures rather than the traditional x86-64
primary audience.

## Why Multiple Architectures?

The Linux kernel runs on a remarkable breadth of hardware.  Yet most
build-from-source guides focus on a single mainstream architecture.
This book aims to be the definitive reference for anyone building a
minimal Linux system on any of the following:

- **Tier 1** (well-tested, CI-verified): amd64, arm64, x86
- **Tier 2** (builds, limited testing): arm, loong, mips, ppc, ppc64, riscv
- **Tier 3** (experimental, community-maintained): alpha, hppa, m68k, s390, sparc

## Relationship to Upstream LFS

This book tracks upstream LFS package versions and philosophy closely.
Architecture-specific divergences are called out in **Arch Note** boxes.
Where upstream LFS is silent on a topic relevant to a non-x86 architecture,
this book fills the gap.

## How to Report Issues

Open an issue at the project repository.  Please tag your report with the
affected architecture (e.g. `[riscv]`).
