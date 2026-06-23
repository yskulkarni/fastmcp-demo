# Copilot instructions for fastmcp-demo

Purpose
- Short guide to help Copilot/AI sessions work effectively in this repository.

Build / install / run
- Python: requires >= 3.14 (see pyproject.toml).
- Install runtime deps directly (recommended for reproducible minimal steps):
  - python -m venv .venv && . .venv/bin/activate
  - pip install "fastmcp>=3.4.2" "mcp[cli]>=1.28.0"
- Run the server locally:
  - python main.py

Tests and linting
- This repository currently has no test or linter configuration.
- If tests are added (pytest), run a single test with:
  - pytest path/to/test_file.py::test_name
- Common linter commands (not configured here) you may expect in similar projects:
  - ruff check .
  - black . --check

High-level architecture (big picture)
- Modular FastMCP server organized into tools/ and resources/ directories:
  - main.py: Creates FastMCP instance, imports tools and resources modules to auto-register them, and runs the server loop.
  - tools/ directory: Contains tool implementations (geometry.py, math.py, etc.). Tools are registered in tools/__init__.py by importing mcp from main and calling mcp.tool() decorator.
  - resources/ directory: Contains resource implementations (system.py, etc.). Resources are registered in resources/__init__.py by importing mcp from main and calling mcp.resource() decorator.
  - Registration pattern: Each submodule's __init__.py imports the mcp instance from main.py and decorates functions to register them, ensuring tools and resources are available to the LLM when main.py imports the modules.
- Intent: Keep tools and resources organized by type, scalable for future additions. Logic remains simple and explicit.

Key conventions and repository-specific patterns
- Module organization:
  - tools/: Place each tool in its own file (geometry.py, math.py, etc.) for clarity and maintainability.
  - resources/: Place each resource in its own file (system.py, etc.).
  - Each directory's __init__.py imports mcp from main.py and registers its functions using @mcp.tool() or @mcp.resource() decorators.
- Registration in submodules:
  - tools/__init__.py and resources/__init__.py import the global mcp instance and manually call mcp.tool() or mcp.resource() on function objects to register them.
  - This pattern allows tools and resources to live in focused modules while maintaining registration at import time.
- Function docstrings are the authoritative short description for tools — keep them concise and focused for good prompt generation.
- Prefer simple, small functions as tools (pure/side-effect-free where possible) to keep behaviour predictable for LLM callers.

Files checked and notes
- pyproject.toml contains project metadata and runtime dependencies (fastmcp, mcp[cli]) and declares python >=3.14.
- README.md contains project overview and getting started instructions.
- Repository is now organized into tools/ and resources/ directories with __init__.py registration modules.
- No CONTRIBUTING.md, test config, or other AI assistant config files (CLAUDE.md, AGENTS.md, .cursorrules, etc.) were found.

If you add more components
- If you add a tests/ suite: include pytest in pyproject and add a short section here with the project test command and examples for running single tests.
- If you add a linter/formatter (ruff/black/flake8), add exact commands under "Tests and linting" so Copilot can suggest CI and local dev commands.

Contact/next steps
- Keep docstrings and resource IDs stable — Copilot uses them to suggest tool calls and generate prompts.

---
(Generated from repository inspection of pyproject.toml and main.py.)