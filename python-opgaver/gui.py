import tkinter as tk
from tkinter import ttk, simpledialog
from tools.time_tools import get_current_time
from tools.network_tools import get_ip_and_hostname
from tools.file_tools import find_config_files
from tools.specificFile_tools import check_file_exists
from tools.rename_tools import rename_txt_to_md  # Import the new function
from tools.process_tools import list_running_processes  # Import the new function
from tools.port_tools import check_open_port
from tools.disk_tools import check_disk_space
from tools.log_tools import search_logs_for_word
from tools.calc_tools import simple_calculator


def run_calculator():
    num1 = simpledialog.askstring("Calculator", "Enter the first number:")
    if num1 is None:
        return

    num2 = simpledialog.askstring("Calculator", "Enter the second number:")
    if num2 is None:
        return

    operator = simpledialog.askstring("Calculator", "Enter an operator (+, -, *, /):")
    if operator is None:
        return

    try:
        result = simple_calculator(num1, num2, operator)
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result + "\n")
        output_text.config(state="disabled")
    except ValueError as e:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, str(e) + "\n")
        output_text.config(state="disabled")


def search_in_logs():
    directory_path = simpledialog.askstring("Directory Path", "Enter the folder path to search for log files:")
    if not directory_path:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No folder path provided.\n")
        output_text.config(state="disabled")
        return

    search_word = simpledialog.askstring("Search Word", "Enter the word to search for in log files:")
    if not search_word:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No search word provided.\n")
        output_text.config(state="disabled")
        return

    try:
        from tools.log_tools import search_logs_for_word
        result = search_logs_for_word(directory_path, search_word)
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result + "\n")
        output_text.config(state="disabled")
    except ValueError as e:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, str(e) + "\n")
        output_text.config(state="disabled")

def check_disk():
    try:
        result = check_disk_space()
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state="disabled")
    except Exception as e:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}\n")
        output_text.config(state="disabled")


def check_time():
    result = get_current_time()
    output_text.config(state="normal")
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Current Time: {result}\n")
    output_text.config(state="disabled")

def check_network():
    ip, hostname = get_ip_and_hostname()
    output_text.config(state="normal")
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"IP: {ip}\nHostname: {hostname}\n")
    output_text.config(state="disabled")

def check_port():
    # Prompt the user for the host
    host = simpledialog.askstring("Host", "Enter the hostname or IP address (e.g., google.com):")
    if not host:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No host provided.\n")
        output_text.config(state="disabled")
        return

    # Prompt the user for the port
    port = simpledialog.askinteger("Port", "Enter the port number (e.g., 443):")
    if not port:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No port provided.\n")
        output_text.config(state="disabled")
        return

    # Check if the port is open
    try:
        result = check_open_port(host, port)
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result + "\n")
        output_text.config(state="disabled")
    except Exception as e:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}\n")
        output_text.config(state="disabled")


def find_files():
    folder_path = simpledialog.askstring("Folder Path", "Enter the folder path to search:")
    if folder_path:
        try:
            config_files = find_config_files(folder_path)
            output_text.config(state="normal")
            output_text.delete(1.0, tk.END)
            if config_files:
                output_text.insert(tk.END, "Found files:\n" + "\n".join(config_files) + "\n")
            else:
                output_text.insert(tk.END, "No .conf or .config files found.\n")
            output_text.config(state="disabled")
        except ValueError as e:
            output_text.config(state="normal")
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, str(e) + "\n")
            output_text.config(state="disabled")

def check_file():
    folder_path = simpledialog.askstring("Choose Main Folder", "Enter the main folder path:")
    if not folder_path:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No folder path provided.\n")
        output_text.config(state="disabled")
        return

    file_name = simpledialog.askstring("File Name", "Enter the file name (e.g., file.txt):")
    if not file_name:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No file name provided.\n")
        output_text.config(state="disabled")
        return

    try:
        result = check_file_exists(folder_path, file_name)
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result + "\n")
        output_text.config(state="disabled")
    except ValueError as e:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, str(e) + "\n")
        output_text.config(state="disabled")

def rename_files():
    folder_path = simpledialog.askstring("Folder Path", "Enter the folder path to rename .txt files:")
    if not folder_path:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No folder path provided.\n")
        output_text.config(state="disabled")
        return

    try:
        result = rename_txt_to_md(folder_path)
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result + "\n")
        output_text.config(state="disabled")
    except ValueError as e:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, str(e) + "\n")
        output_text.config(state="disabled")

def list_processes():
    try:
        processes = list_running_processes()
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        if processes:
            output_text.insert(tk.END, "Running Processes:\n" + "\n".join(processes) + "\n")
        else:
            output_text.insert(tk.END, "No running processes found.\n")
        output_text.config(state="disabled")
    except Exception as e:
        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}\n")
        output_text.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("Utility Tool")
root.geometry("800x600")  # Increased size for better display
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12))

# Frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

# Buttons in a grid layout
time_button = ttk.Button(button_frame, text="Check Time", command=check_time)
time_button.grid(row=0, column=0, padx=20, pady=10)

calc_button = ttk.Button(button_frame, text="Simple Calculator", command=run_calculator)
calc_button.grid(row=4, column=1, padx=20, pady=10)

network_button = ttk.Button(button_frame, text="Check Network", command=check_network)
network_button.grid(row=0, column=1, padx=20, pady=10)

file_button = ttk.Button(button_frame, text="Find Config Files", command=find_files)
file_button.grid(row=1, column=0, padx=20, pady=10)

check_file_button = ttk.Button(button_frame, text="Check File Exists", command=check_file)
check_file_button.grid(row=1, column=1, padx=20, pady=10)

rename_button = ttk.Button(button_frame, text="Rename .txt to .md", command=rename_files)
rename_button.grid(row=2, column=0, padx=20, pady=10)

process_button = ttk.Button(button_frame, text="List Processes", command=list_processes)
process_button.grid(row=2, column=1, padx=20, pady=10)

port_button = ttk.Button(button_frame, text="Check Open Port", command=check_port)
port_button.grid(row=3, column=0, padx=20, pady=10)

disk_button = ttk.Button(button_frame, text="Check Disk Space", command=check_disk)
disk_button.grid(row=3, column=1, padx=20, pady=10)

log_button = ttk.Button(button_frame, text="Search in Logs", command=search_in_logs)
log_button.grid(row=4, column=0, padx=20, pady=10)

# Scrollable output area
output_frame = ttk.Frame(root)
output_frame.pack(pady=20, fill=tk.BOTH, expand=True)

output_scrollbar = ttk.Scrollbar(output_frame)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(output_frame, wrap=tk.WORD, state="disabled", yscrollcommand=output_scrollbar.set, font=("Arial", 10))
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_scrollbar.config(command=output_text.yview)

# Run the application
root.mainloop()