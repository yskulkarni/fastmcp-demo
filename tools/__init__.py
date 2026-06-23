from main import mcp
from .geometry import calculate_rectangle_area
from .math import square

mcp.tool()(calculate_rectangle_area)
mcp.tool()(square)

__all__ = ['calculate_rectangle_area', 'square']
