import platform
import subprocess
import datetime
import os

def log_results(output_text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"audit_report_{timestamp}.txt"
    
    # Write to file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_text)
    
    print(f"\n[INFO] Report saved successfully to: {filename}")
    # Print to console so you can see it immediately too
    print("\n--- CONTENT OF LOG FILE ---")
    print(output_text)

def run_linux_audit():
    print(f"Detected OS: Linux. Executing Bash script...\n")
    try:
        # Check permissions first
        subprocess.run(['chmod', '+x', './audit_linux.sh'])
        
        # Run script and capture BOTH stdout and stderr
        result = subprocess.run(
            ['bash', './audit_linux.sh'], 
            capture_output=True, 
            text=True
        )
        
        # Combine output and errors
        full_output = result.stdout + "\n" + result.stderr
        return full_output
        
    except FileNotFoundError:
        return "Error: audit_linux.sh file not found in directory."

def run_windows_audit():
    print(f"Detected OS: Windows. Executing PowerShell script...\n")
    try:
        command = ["powershell", "-ExecutionPolicy", "Bypass", "-File", "./Audit-Windows.ps1"]
        
        # Run script and capture BOTH stdout and stderr
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True
        )
        
        # Combine output and errors
        full_output = result.stdout + "\n" + result.stderr
        return full_output
        
    except FileNotFoundError:
        return "Error: Audit-Windows.ps1 file not found in directory."

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