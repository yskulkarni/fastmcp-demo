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
- Tiny demo FastMCP server exposing programmatic "tools" and "resources":
  - main.py constructs FastMCP("Developer Utility Server") and registers functions with decorators:
    - @mcp.tool() → registers a callable as a tool callable by the LLM
    - @mcp.resource("scheme://name") → exposes static contextual data
  - mcp.run() (in __main__) starts the server loop.
- Intent: host single-file tool/resource definitions that the MCP runtime exposes to LLMs. Keep logic and I/O minimal and explicit.

Key conventions and repository-specific patterns
- Decorators are the primary integration surface:
  - Use @mcp.tool() for functions intended as LLM-invokable tools. Type annotations (arg and return types) and docstrings are used as the tool signature/description.
  - Use @mcp.resource("scheme://id") for static contextual data; resource identifiers follow a scheme://name style (e.g., system://os-info).
- Function docstrings are the authoritative short description for tools — keep them concise and focused for good prompt generation.
- Prefer simple, small functions as tools (pure/side-effect-free where possible) to keep behaviour predictable for LLM callers.
- Keep module-level registration (mcp = FastMCP(...)) in main.py; additional modules may import the mcp instance to register more tools/resources.

Files checked and notes
- pyproject.toml contains project metadata and runtime dependencies (fastmcp, mcp[cli]) and declares python >=3.14.
- README.md is present but minimal.
- No CONTRIBUTING.md, test config, or AI assistant config files (CLAUDE.md, AGENTS.md, .cursorrules, etc.) were found.

If you add more components
- If you add a tests/ suite: include pytest in pyproject and add a short section here with the project test command and examples for running single tests.
- If you add a linter/formatter (ruff/black/flake8), add exact commands under "Tests and linting" so Copilot can suggest CI and local dev commands.

Contact/next steps
- Keep docstrings and resource IDs stable — Copilot uses them to suggest tool calls and generate prompts.

---
(Generated from repository inspection of pyproject.toml and main.py.)