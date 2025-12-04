import os

def search_logs_for_word(directory_path, search_word):
    """
    Recursively scans all .log files in the given directory and subdirectories,
    returning all lines that contain the user-specified word (case-insensitive).
    """
    if not os.path.exists(directory_path):
        raise ValueError(f"Path not found: {directory_path}")

    if not search_word or search_word.strip() == "":
        raise ValueError("Search word cannot be empty.")

    search_word_lower = search_word.lower()
    matched_lines = []

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.lower().endswith(".log"):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line in f:
                            if search_word_lower in line.lower():
                                matched_lines.append(f"{file_path}: {line.strip()}")
                except PermissionError:
                    matched_lines.append(f"[Permission denied] {file_path}")
                except Exception as e:
                    matched_lines.append(f"[Error reading {file_path}] {str(e)}")

    if not matched_lines:
        return f"No entries containing '{search_word}' found in {directory_path} or its subdirectories."
    else:
        return (
            f"Found {len(matched_lines)} entries containing '{search_word}' in .log files under {directory_path}:\n"
            + "\n".join(matched_lines[:50])
            + ("\n\n(...showing first 50 results only)" if len(matched_lines) > 50 else "")
        )
