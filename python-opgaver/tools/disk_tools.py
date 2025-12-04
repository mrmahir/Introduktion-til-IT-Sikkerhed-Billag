import shutil

def check_disk_space(path="/"):
    """
    Checks disk usage for the given path and returns a message
    if the free space is under 20%.
    """
    total, used, free = shutil.disk_usage(path)
    free_percent = (free / total) * 100

    result = (
        f"Disk total: {total / (1024**3):.2f} GB\n"
        f"Used: {used / (1024**3):.2f} GB\n"
        f"Free: {free / (1024**3):.2f} GB ({free_percent:.2f}%)\n"
    )

    if free_percent < 20:
        result += "⚠️ Warning: Free disk space is below 20%!\n"
    else:
        result += "✅ Disk space is sufficient.\n"

    return result
