fastmcp-demo
=============

A minimal demonstration FastMCP server that registers simple programmatic "tools" and "resources" for an LLM-enabled runtime.

This repository is intentionally small and focused: it shows how to declare tools with @mcp.tool() and static resources with @mcp.resource(...) so the MCP runtime can expose them to language models.

Requirements
- Python >= 3.14 (declared in pyproject.toml)
- Runtime dependencies: fastmcp, mcp[cli]

Installation
- Create and activate a virtualenv:
  - python -m venv .venv && . .venv/bin/activate
- Install runtime dependencies:
  - pip install "fastmcp>=3.4.2" "mcp[cli]>=1.28.0"

Running the server
- Start the demo server:
  - python main.py
- The server registers tools and resources on startup. Tools are defined with the @mcp.tool() decorator; resources use @mcp.resource("scheme://id").

Included tools (example)
- calculate_rectangle_area(width: float, height: float) -> float
  - Returns width * height. Useful for geometric calculations.
- square(number: float) -> float
  - Returns number squared. Simple numeric utility.

Development notes
- File: main.py
  - Creates the FastMCP instance and registers tools/resources at module import time.
  - Keep tool functions small and well-documented: their docstrings become the tool descriptions used by LLMs.
- Tests: none included. If adding tests, prefer pytest and add it to pyproject.toml.
- Linting/Formatting: none configured. Consider ruff/black for CI and local checks; add commands to pyproject and .github workflows when enabled.

Contributing
- This is a demo repo. Open issues or PRs for improvements; keep changes focused and small.

License
- No license specified. Add a LICENSE file if you intend to publish this repository under a specific license.

README generated/updated on 2026-06-23.
