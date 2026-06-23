from mcp.server.fastmcp import FastMCP 


# Initialize the server application with a display name
mcp = FastMCP("Developer Utility Server")

# Import tool and resource modules to register with mcp
import tools
import resources

if __name__ == "__main__":
    mcp.run()

