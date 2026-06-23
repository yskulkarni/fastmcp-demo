import platform
from mcp.server.fastmcp import FastMCP 


# Initialize the server application with a display name
mcp = FastMCP("Developer Utility Server")

@mcp.tool()
def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Calculates the area of a rectangle. Use this tool whenever the user
    needs to find space, dimensions, or geometric areas.

    Args:
        width: The horizontal length of the box or room.
        height: The vertical length of the box or room.
    """
    return width * height


@mcp.tool()
def square(number: float) -> float:
    """
    Returns the square of a number.

    Args:
        number: Numeric value to be squared.
    """
    return number * number

@mcp.resource("system://os-info")
def get_system_info() -> str:
    """
    Returns the host operating system information. This provides static read-only 
    context to the LLM about the system it is running on.
    """
    return f"Running on {platform.system()} {platform.release()} ({platform.machine()})"

if __name__ == "__main__":
    mcp.run()
