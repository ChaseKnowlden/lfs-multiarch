# Multi-Arch LFS Book — Makefile
#
# Targets:
#   make build        Build HTML output (default)
#   make serve        Live-preview in browser (http://localhost:3000)
#   make pdf          Build PDF via Pandoc
#   make epub         Build EPUB via Pandoc
#   make check        Run all linters (spell, links, mdBook test)
#   make spell        Spell-check sources only
#   make linkcheck    Check for broken links
#   make clean        Remove build output
#   make install-deps Install tooling (mdBook, codespell, markdown-link-check)
#
# Variables you can override:
#   ARCH=amd64        Only relevant when running build scripts

SHELL  := /bin/bash
ARCH   ?= amd64

MDBOOK := mdbook
PANDOC := pandoc
PYTHON := python3

BOOK_SRC    := book
OUTPUT_DIR  := output
PANDOC_OUT  := output/pdf

.PHONY: all build serve check spell linkcheck pdf epub clean install-deps arch-check currency currency-update

all: build

# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
build:
	$(MDBOOK) build

serve:
	$(MDBOOK) serve --open

# ---------------------------------------------------------------------------
# Linting & validation
# ---------------------------------------------------------------------------
check: spell linkcheck
	$(MDBOOK) test

spell:
	@echo "==> Spell check"
	codespell \
	    --skip="$(OUTPUT_DIR),*.png,*.jpg,*.svg,.git,node_modules" \
	    --ignore-words=.codespell-ignore \
	    $(BOOK_SRC) scripts ROADMAP.md CONTRIBUTING.md

linkcheck:
	@echo "==> Link check"
	find $(BOOK_SRC) -name '*.md' | \
	    xargs markdown-link-check --config .mlc.json --quiet

# ---------------------------------------------------------------------------
# Alternative output formats (require Pandoc)
# ---------------------------------------------------------------------------
pdf: build
	@mkdir -p $(PANDOC_OUT)
	@echo "==> Generating PDF"
	find $(BOOK_SRC) -name '*.md' ! -name 'SUMMARY.md' | sort | \
	    xargs $(PANDOC) \
	        --from markdown \
	        --to pdf \
	        --pdf-engine=xelatex \
	        --toc \
	        --toc-depth=3 \
	        --metadata title="Multi-Architecture Linux From Scratch" \
	        -o $(PANDOC_OUT)/lfs-multiarch.pdf
	@echo "PDF written to $(PANDOC_OUT)/lfs-multiarch.pdf"

epub: build
	@mkdir -p $(PANDOC_OUT)
	@echo "==> Generating EPUB"
	find $(BOOK_SRC) -name '*.md' ! -name 'SUMMARY.md' | sort | \
	    xargs $(PANDOC) \
	        --from markdown \
	        --to epub \
	        --toc \
	        --metadata title="Multi-Architecture Linux From Scratch" \
	        -o $(PANDOC_OUT)/lfs-multiarch.epub
	@echo "EPUB written to $(PANDOC_OUT)/lfs-multiarch.epub"

# ---------------------------------------------------------------------------
# Architecture-specific build driver (wraps scripts/build-cross-toolchain.sh)
# ---------------------------------------------------------------------------
arch-check:
	@echo "Checking host for LFS_ARCH=$(ARCH)"
	source scripts/arch-config.sh $(ARCH) && scripts/version-check.sh

currency:
	@echo "==> Checking upstream package versions"
	$(PYTHON) scripts/check-versions.py

currency-update:
	@echo "==> Checking upstream package versions and updating ch02-packages.md"
	$(PYTHON) scripts/check-versions.py --update

# ---------------------------------------------------------------------------
# Housekeeping
# ---------------------------------------------------------------------------
clean:
	rm -rf $(OUTPUT_DIR)
	@echo "Cleaned."

install-deps:
	@echo "==> Installing mdBook"
	cargo install mdbook
	@echo "==> Installing codespell"
	$(PYTHON) -m pip install --user codespell
	@echo "==> Installing markdown-link-check"
	npm install -g markdown-link-check
	@echo "All tooling installed."
