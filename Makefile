#config
PROJECT = snowfetch
SRC = snowfetch.py
LOGO_DIR = logo

PREFIX = /usr/local
BINDIR = $(PREFIX)/bin
LIBDIR = $(PREFIX)/lib/$(PROJECT)

BIN = $(BINDIR)/$(PROJECT)
LIB = $(LIBDIR)/$(SRC)
LIB_LOGO = $(LIBDIR)/$(LOGO_DIR)

# Detect Python
PYTHON := $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)

# Rules
.PHONY: help run install uninstall clean

# Help
help:
	@echo "Snowfetch – Makefile"
	@echo ""
	@echo "Commands :"
	@echo "  make run        → Start snowfetch (not installing)"
	@echo "  make install    → install snowfetch"
	@echo "  make uninstall  → delete snowfetch"
	@echo "  make clean      → Clean"

# Run
run:
	$(PYTHON) $(SRC)

# Install
install:
	@echo "Installing $(PROJECT)..."
	install -d $(LIBDIR)
	install -m644 $(SRC) $(LIB)
	
	# Copy logo directory
	install -d $(LIB_LOGO)
	cp -r $(LOGO_DIR)/* $(LIB_LOGO)/

	@echo '#!/usr/bin/env sh' > $(BIN)
	@echo 'exec $(PYTHON) $(LIB) "$$@"' >> $(BIN)
	chmod +x $(BIN)
	@echo "Installed ! -->"
	@echo "  $(LIB)"
	@echo "  $(BIN)"
	@echo "  Logos copied to $(LIB_LOGO)"

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
