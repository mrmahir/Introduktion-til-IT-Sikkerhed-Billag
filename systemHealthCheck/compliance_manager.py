import platform
import subprocess
import datetime
import os
import sys

# --- Configuration ---
# This script acts as a wrapper. It detects the OS, runs the correct 
# audit script, and logs the results to a file.

def log_results(output_text):
    """
    Saves the audit results to a timestamped file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"audit_report_{timestamp}.txt"
    
    # Write to file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_text)
    
    print(f"\n[INFO] Report saved successfully to: {filename}")
    print("\n--- CONTENT OF LOG FILE ---")
    print(output_text)

def get_script_path(script_name):
    """
    Helper function to get the absolute path of the script files.
    This fixes the 'file not found' error.
    """
    # Get the directory where THIS python file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Join it with the script name to get the full path
    return os.path.join(current_dir, script_name)

def run_linux_audit():
    print(f"Detected OS: Linux. Executing Bash script...\n")
    script_path = get_script_path("audit_linux.sh")
    
    try:
        # Check permissions first
        subprocess.run(['chmod', '+x', script_path])
        
        # Run script
        result = subprocess.run(
            ['bash', script_path], 
            capture_output=True, 
            text=True
        )
        
        full_output = result.stdout + "\n" + result.stderr
        return full_output
        
    except Exception as e:
        return f"Error executing Linux script: {e}"

def run_windows_audit():
    print(f"Detected OS: Windows. Executing PowerShell script...\n")
    script_path = get_script_path("Audit-Windows.ps1")
    
    try:
        # Check if file exists before running
        if not os.path.exists(script_path):
            return f"Error: Could not find file at: {script_path}"

        # We use 'powershell' with ExecutionPolicy Bypass
        command = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path]
        
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True
        )
        
        full_output = result.stdout + "\n" + result.stderr
        return full_output
        
    except Exception as e:
        return f"Error executing Windows script: {e}"

def main():
    os_name = platform.system()
    audit_output = ""

    print("--- CROSS-PLATFORM COMPLIANCE MANAGER v1.0 ---\n")

    if os_name == "Linux":
        audit_output = run_linux_audit()
    elif os_name == "Windows":
        audit_output = run_windows_audit()
    else:
        print("Unsupported Operating System.")
        return

    # Check if output is empty
    if not audit_output.strip():
        audit_output = "[ERROR] The script ran but returned no output. Check permissions or path."

    log_results(audit_output)

if __name__ == "__main__":
    main()