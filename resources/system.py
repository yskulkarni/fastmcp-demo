import platform


def get_system_info() -> str:
    """
    Returns the host operating system information. This provides static read-only 
    context to the LLM about the system it is running on.
    """
    return f"Running on {platform.system()} {platform.release()} ({platform.machine()})"
