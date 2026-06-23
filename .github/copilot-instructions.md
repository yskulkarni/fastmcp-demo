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
  - main.py: Creates FastMCP instance, imports tools and resources modules (which auto-registers all decorated functions), and runs the server loop.
  - tools/ directory: Contains tool implementations (geometry.py, math.py, etc.). Each tool function uses the @mcp.tool() decorator at definition time for automatic registration.
  - resources/ directory: Contains resource implementations (system.py, etc.). Each resource function uses the @mcp.resource("scheme://id") decorator at definition time for automatic registration.
  - Registration pattern: When each tool/resource module is imported, functions decorated with @mcp.tool() or @mcp.resource() are automatically registered with the global mcp instance from main.py.
- Intent: Keep tools and resources organized by type, scalable for future additions. Decorators are applied at function definition, not post-hoc, ensuring proper registration.

Key conventions and repository-specific patterns
- Module organization:
  - tools/: Place each tool in its own file (geometry.py, math.py, etc.) for clarity and maintainability.
  - resources/: Place each resource in its own file (system.py, etc.).
  - Each tool/resource file imports mcp from main and uses @mcp.tool() or @mcp.resource("scheme://id") decorators at function definition time.
- Registration at definition time:
  - Tools and resources are registered via decorators applied directly to function definitions in their respective module files, not in __init__.py.
  - tools/__init__.py and resources/__init__.py simply import the decorated functions (which auto-register) and re-export them for clarity.
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