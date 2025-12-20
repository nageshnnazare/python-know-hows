# Python 3 Tutorial Course - Makefile
# ═══════════════════════════════════════════════════════════════════════

PYTHON := python3
PY_FILES := $(shell find . -name "*.py" -type f)
BASICS := $(shell find basics -name "*.py" -type f | sort)
INTERMEDIATE := $(shell find intermediate -name "*.py" -type f | sort)
ADVANCED := $(shell find advanced -name "*.py" -type f | sort)

# Colors for output (use with printf or echo -e)
RED := \\033[0;31m
GREEN := \\033[0;32m
YELLOW := \\033[1;33m
BLUE := \\033[0;34m
CYAN := \\033[0;36m
BOLD := \\033[1m
NC := \\033[0m

.PHONY: all help test test-basics test-intermediate test-advanced \
        check syntax lint clean run-all info stats

# Default target
all: help

# ═══════════════════════════════════════════════════════════════════════
# HELP - Show available commands
# ═══════════════════════════════════════════════════════════════════════

help:
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)  Python 3 Tutorial Course - Makefile Commands$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n\n"
	@printf "$(GREEN)Testing Commands:$(NC)\n"
	@printf "  make test              - Run all Python files and check for errors\n"
	@printf "  make test-basics       - Run only basics section\n"
	@printf "  make test-intermediate - Run only intermediate section\n"
	@printf "  make test-advanced     - Run only advanced section\n\n"
	@printf "$(GREEN)Quality Checks:$(NC)\n"
	@printf "  make check             - Check all files for syntax errors\n"
	@printf "  make syntax            - Syntax check without running\n"
	@printf "  make lint              - Run linting (requires pylint)\n\n"
	@printf "$(GREEN)Information:$(NC)\n"
	@printf "  make info              - Show course information\n"
	@printf "  make stats             - Show statistics\n"
	@printf "  make list              - List all tutorial files\n\n"
	@printf "$(GREEN)Utilities:$(NC)\n"
	@printf "  make clean             - Remove generated files\n"
	@printf "  make run FILE=path     - Run a specific file\n"
	@printf "  make help              - Show this help message\n\n"
	@printf "$(YELLOW)Examples:$(NC)\n"
	@printf "  make test-basics\n"
	@printf "  make run FILE=basics/01_variables_and_datatypes.py\n"
	@printf "  make stats\n\n"

# ═══════════════════════════════════════════════════════════════════════
# TESTING - Run Python files
# ═══════════════════════════════════════════════════════════════════════

test: info
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)Running ALL Tutorial Files$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@$(MAKE) test-basics
	@$(MAKE) test-intermediate
	@$(MAKE) test-advanced
	@printf "\n$(GREEN)✓ All tests completed!$(NC)\n"

test-basics:
	@printf "\n$(YELLOW)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)\n"
	@printf "$(YELLOW)  BASICS Section ($(words $(BASICS)) files)$(NC)\n"
	@printf "$(YELLOW)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)\n"
	@for file in $(BASICS); do \
		printf "\n$(BLUE)▶ Running: $$file$(NC)\n"; \
		printf "$(BLUE)─────────────────────────────────────────────────────────$(NC)\n"; \
		if $(PYTHON) $$file 2>&1; then \
			printf "$(GREEN)✓ $$file passed$(NC)\n"; \
		else \
			printf "$(RED)✗ $$file failed$(NC)\n"; \
			exit 1; \
		fi; \
	done

test-intermediate:
	@printf "\n$(YELLOW)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)\n"
	@printf "$(YELLOW)  INTERMEDIATE Section ($(words $(INTERMEDIATE)) files)$(NC)\n"
	@printf "$(YELLOW)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)\n"
	@for file in $(INTERMEDIATE); do \
		printf "\n$(BLUE)▶ Running: $$file$(NC)\n"; \
		printf "$(BLUE)─────────────────────────────────────────────────────────$(NC)\n"; \
		if $(PYTHON) $$file 2>&1; then \
			printf "$(GREEN)✓ $$file passed$(NC)\n"; \
		else \
			printf "$(RED)✗ $$file failed$(NC)\n"; \
			exit 1; \
		fi; \
	done

test-advanced:
	@printf "\n$(YELLOW)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)\n"
	@printf "$(YELLOW)  ADVANCED Section ($(words $(ADVANCED)) files)$(NC)\n"
	@printf "$(YELLOW)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)\n"
	@for file in $(ADVANCED); do \
		printf "\n$(BLUE)▶ Running: $$file$(NC)\n"; \
		printf "$(BLUE)─────────────────────────────────────────────────────────$(NC)\n"; \
		if $(PYTHON) $$file 2>&1; then \
			printf "$(GREEN)✓ $$file passed$(NC)\n"; \
		else \
			printf "$(RED)✗ $$file failed$(NC)\n"; \
			exit 1; \
		fi; \
	done

# ═══════════════════════════════════════════════════════════════════════
# QUALITY CHECKS
# ═══════════════════════════════════════════════════════════════════════

check: syntax

syntax:
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)Checking Python Syntax$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@for file in $(PY_FILES); do \
		printf "Checking $$file...\n"; \
		if $(PYTHON) -m py_compile $$file 2>&1; then \
			printf "$(GREEN)✓ $$file$(NC)\n"; \
		else \
			printf "$(RED)✗ $$file has syntax errors$(NC)\n"; \
			exit 1; \
		fi; \
	done
	@printf "\n$(GREEN)✓ All files have valid syntax!$(NC)\n"

lint:
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)Running Linter (pylint)$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@if command -v pylint >/dev/null 2>&1; then \
		for file in $(PY_FILES); do \
			printf "Linting $$file...\n"; \
			pylint $$file || true; \
		done; \
	else \
		printf "$(YELLOW)⚠ pylint not installed. Install with: pip install pylint$(NC)\n"; \
	fi

# ═══════════════════════════════════════════════════════════════════════
# INFORMATION
# ═══════════════════════════════════════════════════════════════════════

info:
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)  Python 3 Tutorial Course$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n\n"
	@printf "$(GREEN)Course Structure:$(NC)\n"
	@printf "  📁 Basics:       $(words $(BASICS)) files\n"
	@printf "  📁 Intermediate: $(words $(INTERMEDIATE)) files\n"
	@printf "  📁 Advanced:     $(words $(ADVANCED)) files\n"
	@printf "  📊 Total:        $(words $(PY_FILES)) Python files\n\n"
	@printf "$(GREEN)Python Version:$(NC)\n"
	@$(PYTHON) --version
	@printf "\n"

stats:
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)Course Statistics$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n\n"
	@printf "$(GREEN)Files by Section:$(NC)\n"
	@printf "  Basics:       $(words $(BASICS)) files\n"
	@printf "  Intermediate: $(words $(INTERMEDIATE)) files\n"
	@printf "  Advanced:     $(words $(ADVANCED)) files\n"
	@printf "  Total:        $(words $(PY_FILES)) files\n\n"
	@printf "$(GREEN)Lines of Code:$(NC)\n"
	@wc -l $(PY_FILES) | tail -1 | awk '{print "  Total: " $$1 " lines"}'
	@printf "\n$(GREEN)Disk Usage:$(NC)\n"
	@du -sh . | awk '{print "  Size: " $$1}'
	@printf "\n$(GREEN)Documentation:$(NC)\n"
	@ls -1 *.md 2>/dev/null | wc -l | awk '{print "  Guides: " $$1 " markdown files"}'
	@printf "\n"

list:
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)All Tutorial Files$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n\n"
	@printf "$(YELLOW)BASICS:$(NC)\n"
	@for file in $(BASICS); do printf "  $$file\n"; done
	@printf "\n$(YELLOW)INTERMEDIATE:$(NC)\n"
	@for file in $(INTERMEDIATE); do printf "  $$file\n"; done
	@printf "\n$(YELLOW)ADVANCED:$(NC)\n"
	@for file in $(ADVANCED); do printf "  $$file\n"; done
	@printf "\n"

# ═══════════════════════════════════════════════════════════════════════
# UTILITIES
# ═══════════════════════════════════════════════════════════════════════

run:
	@if [ -z "$(FILE)" ]; then \
		printf "$(RED)Error: Please specify FILE=path/to/file.py$(NC)\n"; \
		exit 1; \
	fi
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)Running: $(FILE)$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@$(PYTHON) $(FILE)

clean:
	@printf "$(BLUE)Cleaning generated files...$(NC)\n"
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name ".DS_Store" -delete
	@rm -f output.prof
	@printf "$(GREEN)✓ Cleaned!$(NC)\n"

# ═══════════════════════════════════════════════════════════════════════
# QUICK START EXAMPLES
# ═══════════════════════════════════════════════════════════════════════

.PHONY: quick-start beginner intermediate advanced

quick-start:
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(BLUE)Quick Start - Running First Tutorial$(NC)\n"
	@printf "$(BLUE)════════════════════════════════════════════════════════════$(NC)\n"
	@$(PYTHON) basics/01_variables_and_datatypes.py

beginner: test-basics

intermediate: test-intermediate

advanced: test-advanced

# ═══════════════════════════════════════════════════════════════════════
# CONTINUOUS INTEGRATION
# ═══════════════════════════════════════════════════════════════════════

ci: syntax test
	@printf "\n$(GREEN)════════════════════════════════════════════════════════════$(NC)\n"
	@printf "$(GREEN)✓ All CI checks passed!$(NC)\n"
	@printf "$(GREEN)════════════════════════════════════════════════════════════$(NC)\n"

# ═══════════════════════════════════════════════════════════════════════
# INSTALLATION & SETUP
# ═══════════════════════════════════════════════════════════════════════

.PHONY: install setup venv

install:
	@printf "$(BLUE)Installing recommended packages...$(NC)\n"
	@pip install --upgrade pip
	@pip install ipython pytest black flake8 pylint mypy

setup: install
	@printf "$(GREEN)✓ Setup complete!$(NC)\n\n"
	@printf "Start learning with:\n"
	@printf "  make quick-start\n"

venv:
	@printf "$(BLUE)Creating virtual environment...$(NC)\n"
	@$(PYTHON) -m venv venv
	@printf "$(GREEN)✓ Virtual environment created!$(NC)\n\n"
	@printf "Activate it with:\n"
	@printf "  source venv/bin/activate  # Linux/Mac\n"
	@printf "  venv\\\\Scripts\\\\activate     # Windows\n"

