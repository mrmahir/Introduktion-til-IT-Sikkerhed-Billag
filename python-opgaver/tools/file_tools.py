import os

def find_config_files(folder_path):
    """
    Searches for files ending with .conf or .config in the specified folder.

    Args:
        folder_path (str): The path to the folder to search in.

    Returns:
        list: A list of file paths that match the criteria.
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"The path '{folder_path}' is not a valid directory.")

    config_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".conf") or file.endswith(".config"):
                config_files.append(os.path.join(root, file))
    return config_files