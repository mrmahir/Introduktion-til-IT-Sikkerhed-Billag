# --- Windows Security & Health Auditor ---
# UPDATED: Tracks success status for a special message

# Force console to handle emojis (UTF-8)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# TRACKING VARIABLE
$AllChecksPassed = $true

Write-Output "========================================"
Write-Output "   WINDOWS SYSTEM DIAGNOSTIC TOOL"
Write-Output "========================================"

# 1. CHECK WINDOWS DEFENDER STATUS
Write-Output "[*] Checking Antivirus Status..."
$defender = Get-MpComputerStatus
If ($defender.AntivirusEnabled -eq $true) {
    Write-Output "[PASS] Windows Defender is Active and Running."
}
Else {
    Write-Output "[FAIL] Windows Defender is DISABLED."
    $AllChecksPassed = $false
}

# 2. CHECK DISK SPACE (C: Drive)
Write-Output "[*] Checking C: Drive Storage..."
$disk = Get-Volume -DriveLetter C
$freeSpaceGB = [math]::Round($disk.SizeRemaining / 1GB, 2)

If ($freeSpaceGB -lt 10) {
    Write-Output "[WARNING] Low Disk Space: Only $freeSpaceGB GB remaining."
    $AllChecksPassed = $false
}
Else {
    Write-Output "[PASS] Disk Space Healthy: $freeSpaceGB GB free."
}

# 3. CHECK LAST WINDOWS UPDATE
# We assume simply getting the data is a "Pass" for this basic script
Write-Output "[*] Checking Update History..."
$lastUpdate = Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 1
Write-Output "Last Hotfix Installed: $($lastUpdate.HotFixID) on $($lastUpdate.InstalledOn)"

Write-Output "========================================"

# FINAL VERDICT
If ($AllChecksPassed -eq $true) {
    Write-Output ""
    Write-Output "Your computer is safe, but your country is never truly safe from the Ottomans 🇹🇷 🇹🇷 🇹🇷"
    Write-Output ""
}