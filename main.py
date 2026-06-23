from mcp.server.fastmcp import FastMCP 


# Initialize the server application with a display name
mcp = FastMCP("Developer Utility Server")

# Import tool and resource modules - they will register themselves
# when imported because their functions use @mcp.tool() and @mcp.resource() decorators
import tools
import resources

if __name__ == "__main__":
    mcp.run()

