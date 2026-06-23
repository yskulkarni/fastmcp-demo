from main import mcp


@mcp.tool()
def square(number: float) -> float:
    """
    Returns the square of a number.

    Args:
        number: Numeric value to be squared.
    """
    return number * number

