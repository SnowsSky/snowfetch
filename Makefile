# =========================
# Configuration
# =========================
PROJECT = snowfetch
SRC = snowfetch.py

PREFIX = /usr/local
BINDIR = $(PREFIX)/bin
LIBDIR = $(PREFIX)/lib/$(PROJECT)

BIN = $(BINDIR)/$(PROJECT)
LIB = $(LIBDIR)/$(SRC)

# Detect Python
PYTHON := $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)

# Rules
.PHONY: help run install uninstall clean

#Help
help:
	@echo "Snowfetch – Makefile"
	@echo ""
	@echo "Commands :"
	@echo "  make run        → Start snowfetch (not installing)"
	@echo "  make install    → install snowfetch"
	@echo "  make uninstall  → delete snowfetch"
	@echo "  make clean      → Clean"

run:
	$(PYTHON) $(SRC)

# Install
install:
	@echo "Installing $(PROJECT)..."
	install -d $(LIBDIR)
	install -m644 $(SRC) $(LIB)
	@echo '#!/usr/bin/env sh' > $(BIN)
	@echo 'exec $(PYTHON) $(LIB) "$$@"' >> $(BIN)
	chmod +x $(BIN)
	@echo "Installed ! -->"
	@echo "  $(LIB)"
	@echo "  $(BIN)"

# Delete
uninstall:
	@echo "Suppression de $(PROJECT)..."
	rm -f $(BIN)
	rm -rf $(LIBDIR)
	@echo "Supprimé"

# Clean
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
