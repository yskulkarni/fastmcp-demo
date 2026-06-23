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
- Architecture: The project is organized into tools/ and resources/ directories:
  - main.py: Creates the FastMCP instance and imports tools/ and resources/ modules to register them.
  - tools/: Contains tool implementations (geometry.py, math.py, etc.). Each tool's __init__.py registers functions with the global mcp instance.
  - resources/: Contains resource implementations (system.py, etc.). Each resource's __init__.py registers functions with the global mcp instance.
- Adding new tools:
  - Create a new file in tools/ (e.g., tools/stats.py) with your tool function.
  - Import the function in tools/__init__.py and call mcp.tool()(your_function) to register it.
- Adding new resources:
  - Create a new file in resources/ (e.g., resources/environment.py) with your resource function.
  - Import the function in resources/__init__.py and call mcp.resource("scheme://id")(your_function) to register it.
- Tests: none included. If adding tests, prefer pytest and add it to pyproject.toml.
- Linting/Formatting: none configured. Consider ruff/black for CI and local checks; add commands to pyproject and .github workflows when enabled.

Contributing
- This is a demo repo. Open issues or PRs for improvements; keep changes focused and small.

License
- No license specified. Add a LICENSE file if you intend to publish this repository under a specific license.

README generated/updated on 2026-06-23.
