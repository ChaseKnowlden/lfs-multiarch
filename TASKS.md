# LFS Multi-Arch — Active Tasks List

This document tracks active development tasks, near-term priorities, and contributor targets for the Multi-Architecture Linux From Scratch book. It translates the high-level goals of the [ROADMAP.md](file:///home/chase/lfs-multiarch/ROADMAP.md) into actionable work items.

---

## Current Progress & Stats

* **Milestone 0 (Project Bootstrap)**: 100% Complete
* **Milestone 1 (Architecture Baseline Research)**: 25% Complete
* **Milestone 2 (Book Skeleton & Core Chapters)**: 40% Complete
* **Milestone 3 (Per-Architecture Chapters)**: 15% Complete
* **Milestone 4 (Package Versioning & Patches)**: 20% Complete
* **Milestone 5 (Build Automation & Testing)**: 10% Complete
* **Milestone 6 (Book Rendering & Publishing)**: 50% Complete
* **Milestone 7 (Community & Governance)**: 20% Complete

---

## Priority Task Board

### 1. Architecture Baseline Research & Supplements
For each architecture, we must document target triplets, kernel variables, endianness, ABI variants, and known toolchain minimum requirements in their supplement files.

| Status | Task | Priority | Complexity | Target Files |
| :---: | :--- | :---: | :---: | :--- |
| 🟢 | Verify Tier 1 supplements (`amd64`, `arm64`, `x86`) | Medium | Low | [amd64.md](file:///home/chase/lfs-multiarch/book/architectures/amd64.md)<br>[arm64.md](file:///home/chase/lfs-multiarch/book/architectures/arm64.md)<br>[x86.md](file:///home/chase/lfs-multiarch/book/architectures/x86.md) |
| 🟡 | Complete Tier 2 baseline research & document supplements | High | Medium | [arm.md](file:///home/chase/lfs-multiarch/book/architectures/arm.md)<br>[loong.md](file:///home/chase/lfs-multiarch/book/architectures/loong.md)<br>[mips.md](file:///home/chase/lfs-multiarch/book/architectures/mips.md)<br>[ppc.md](file:///home/chase/lfs-multiarch/book/architectures/ppc.md)<br>[ppc64.md](file:///home/chase/lfs-multiarch/book/architectures/ppc64.md)<br>[riscv.md](file:///home/chase/lfs-multiarch/book/architectures/riscv.md) |
| 🔴 | Complete Tier 3 baseline research & document supplements | Low | High | [alpha.md](file:///home/chase/lfs-multiarch/book/architectures/alpha.md)<br>[hppa.md](file:///home/chase/lfs-multiarch/book/architectures/hppa.md)<br>[m68k.md](file:///home/chase/lfs-multiarch/book/architectures/m68k.md)<br>[s390.md](file:///home/chase/lfs-multiarch/book/architectures/s390.md)<br>[sparc.md](file:///home/chase/lfs-multiarch/book/architectures/sparc.md) |
| 🔴 | Verify `$LFS_GCC_EXTRA` alignment for all targets in config | High | Low | [arch-config.sh](file:///home/chase/lfs-multiarch/scripts/arch-config.sh) |

*Legend: 🔴 Not Started | 🟡 In Progress | 🟢 Completed*

---

### 2. Core Book Chapters & Package Compilation Instructions
The core chapters need to detail package compilation and layout requirements for the final system.

| Status | Task | Priority | Complexity | Target Files |
| :---: | :--- | :---: | :---: | :--- |
| 🔴 | Document temporary tool packaging steps | High | Medium | [ch11-temp-tools-packages.md](file:///home/chase/lfs-multiarch/book/part3-building-lfs/ch11-temp-tools-packages.md) |
| 🔴 | Expand virtual file system setup details for chroot | High | Low | [ch15-fs-layout.md](file:///home/chase/lfs-multiarch/book/part3-building-lfs/ch15-fs-layout.md) |
| 🔴 | Write compilation instructions for 60+ core LFS packages | High | High | [ch16-system-packages.md](file:///home/chase/lfs-multiarch/book/part3-building-lfs/ch16-system-packages.md) |
| 🔴 | Complete LFS bootscripts and initial SysVinit setup sections | Medium | Medium | [ch20-bootscripts.md](file:///home/chase/lfs-multiarch/book/part5-bootscripts/ch20-bootscripts.md)<br>[ch21-sysvinit.md](file:///home/chase/lfs-multiarch/book/part5-bootscripts/ch21-sysvinit.md) |

---

### 3. Per-Architecture Bootloader & Configuration Guides
Each CPU architecture has specialized boot requirements.

| Status | Task | Priority | Complexity | Target Files |
| :---: | :--- | :---: | :---: | :--- |
| 🟡 | Complete configuration instructions for UEFI/BIOS GRUB | High | Medium | [bootloaders.md](file:///home/chase/lfs-multiarch/book/part4-system-config/bootloaders.md) |
| 🔴 | Document embedded bootloaders (`u-boot` / `opensbi`) | High | High | [bootloaders.md](file:///home/chase/lfs-multiarch/book/part4-system-config/bootloaders.md) |
| 🔴 | Document non-x86 boot chains (`yaboot`, `aboot`, `palo`, `silo`, `zipl`) | Medium | High | [bootloaders.md](file:///home/chase/lfs-multiarch/book/part4-system-config/bootloaders.md) |
| 🟡 | Verify Device Tree compiler (`dtc`) setup instructions | Medium | Low | [bootloaders.md](file:///home/chase/lfs-multiarch/book/part4-system-config/bootloaders.md) |

---

### 4. Patching & Packaging Automations
Managing packages and cross-compilation patches.

| Status | Task | Priority | Complexity | Target Files |
| :---: | :--- | :---: | :---: | :--- |
| 🟢 | Setup version checker script for package tracking | High | Medium | [check-versions.py](file:///home/chase/lfs-multiarch/scripts/check-versions.py) |
| 🔴 | Write automated source download and verification script | High | Medium | `scripts/fetch-packages.sh` (new) |
| 🟡 | Populate architecture-specific patch directories with tested patches | High | High | [patches/README.md](file:///home/chase/lfs-multiarch/patches/README.md)<br>`patches/<arch>/` |
| 🔴 | Write patch validation checks for CI (verify patches apply cleanly) | Medium | Medium | [ci.yml](file:///home/chase/lfs-multiarch/.github/workflows/ci.yml) |

---

### 5. Cross-Toolchain & System Build Automation
Automating and validating the cross-compilation toolchain build.

| Status | Task | Priority | Complexity | Target Files |
| :---: | :--- | :---: | :---: | :--- |
| 🔴 | Implement toolchain build automation script | High | High | `scripts/build-cross-toolchain.sh` (new) |
| 🔴 | Implement temporary tools and system build script | Medium | High | `scripts/build-system.sh` (new) |
| 🔴 | Design QEMU smoke-test script matrix for target architectures | High | High | `scripts/run-qemu.sh` (new) |
| 🔴 | Extend GitHub Actions CI to execute VM test builds | Medium | High | [ci.yml](file:///home/chase/lfs-multiarch/.github/workflows/ci.yml) |

---

### 6. Rendering & Publishing Pipeline
Publishing and quality-assuring output builds.

| Status | Task | Priority | Complexity | Target Files |
| :---: | :--- | :---: | :---: | :--- |
| 🟢 | Setup HTML render pipeline in GitHub Actions | High | Low | [ci.yml](file:///home/chase/lfs-multiarch/.github/workflows/ci.yml) |
| 🟢 | Implement codespell check target | Medium | Low | [Makefile](file:///home/chase/lfs-multiarch/Makefile)<br>[ci.yml](file:///home/chase/lfs-multiarch/.github/workflows/ci.yml) |
| 🟡 | Validate and fix PDF generation target via Pandoc/XeLaTeX | Medium | Medium | [Makefile](file:///home/chase/lfs-multiarch/Makefile) |
| 🟡 | Validate and fix EPUB generation target via Pandoc | Low | Low | [Makefile](file:///home/chase/lfs-multiarch/Makefile) |

---

### 7. Community & Governance
Making it easier for contributors to volunteer and report issues.

| Status | Task | Priority | Complexity | Target Files |
| :---: | :--- | :---: | :---: | :--- |
| 🟢 | Author contribution guidelines and workflow instructions | High | Low | [CONTRIBUTING.md](file:///home/chase/lfs-multiarch/CONTRIBUTING.md) |
| 🔴 | Assign primary and backup maintainers for all target architectures | Medium | Low | [CONTRIBUTING.md](file:///home/chase/lfs-multiarch/CONTRIBUTING.md) |
| 🔴 | Author PR template and issue templates | Medium | Low | `.github/pull_request_template.md` (new)<br>`.github/ISSUE_TEMPLATE/` (new) |
| 🔴 | Set up mailing list/discussion board for contributor coordination | Low | Low | [CONTRIBUTING.md](file:///home/chase/lfs-multiarch/CONTRIBUTING.md) |

---

## Contributor Guide

If you are looking to help:
1. **Choose a task** from the lists above.
2. Check [CONTRIBUTING.md](file:///home/chase/lfs-multiarch/CONTRIBUTING.md) for the expected commit style and branch naming conventions.
3. Open a draft PR referencing the specific target file(s) and architecture.
