from datetime import datetime

def get_current_time():
    """Returns the current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")