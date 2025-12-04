import os

def rename_txt_to_md(folder_path):
    """
    Renames all .txt files in the given folder and its subfolders to .md files.

    Args:
        folder_path (str): The path to the main folder to search in.

    Returns:
        str: A message indicating how many files were renamed.
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"The path '{folder_path}' is not a valid directory.")

    renamed_files = 0

    # Walk through the folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file[:-4] + ".md")  # Replace .txt with .md
                os.rename(old_file_path, new_file_path)
                renamed_files += 1

    return f"Renamed {renamed_files} .txt file(s) to .md in '{folder_path}'."