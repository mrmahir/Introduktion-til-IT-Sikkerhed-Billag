import socket

def check_open_port(host, port, timeout=3):
    """
    Checks if a specific port on a given host is open.

    Args:
        host (str): The hostname or IP address to check.
        port (int): The port number to check.
        timeout (int): Timeout in seconds for the connection attempt.

    Returns:
        str: A message indicating whether the port is open or closed.
    """
    try:
        with socket.create_connection((host, port), timeout):
            return f"Port {port} on {host} is OPEN."
    except (socket.timeout, socket.error):
        return f"Port {port} on {host} is CLOSED."