import psutil

def list_running_processes():
    """
    Lists all running processes and their PIDs.

    Returns:
        list: A list of strings, each containing the process name and its PID.
    """
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            processes.append(f"PID: {pid}, Name: {name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip processes that no longer exist or cannot be accessed
            continue
    return processes