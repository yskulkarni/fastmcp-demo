from main import mcp
from .system import get_system_info

mcp.resource("system://os-info")(get_system_info)

__all__ = ['get_system_info']
