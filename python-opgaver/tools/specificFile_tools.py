from pathlib import Path

def check_file_exists(folder_path, file_name):
    """
    Recursively checks if a file exists in the given folder or its subfolders.

    Args:
        folder_path (str): The path to the main folder to search in.
        file_name (str): The name of the file to search for (e.g., "file" or "file.txt").

    Returns:
        str: A message indicating whether the file was found or not, and its path if found.
    """
    folder = Path(folder_path)

    if not folder.is_dir():
        raise ValueError(f"The path '{folder_path}' is not a valid directory.")

    # Search for the file in the folder and all subfolders
    matches = []
    for file in folder.rglob("*"):  # rglob searches recursively for all files
        if file.is_file() and (file.stem == file_name or file.stem.startswith(file_name)):
            matches.append(str(file))

    if matches:
        return f"Found {len(matches)} file(s):\n" + "\n".join(matches)
    else:
        return f"File '{file_name}' not found in '{folder_path}' or its subfolders."