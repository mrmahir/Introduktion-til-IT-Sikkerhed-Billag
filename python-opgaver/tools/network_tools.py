import socket

def get_ip_and_hostname():
    """Returns the IP address and hostname of the machine."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address, hostname