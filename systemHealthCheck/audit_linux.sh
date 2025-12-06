#!/bin/bash

# --- Linux Security & Health Auditor ---
# This script checks firewall status, disk usage, and SSH configuration.

# Define Colors for nicer output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "========================================"
echo "   LINUX SYSTEM DIAGNOSTIC TOOL"
echo "========================================"

# 1. CHECK FIREWALL (UFW)
# We assume Kali/Ubuntu/Debian based systems
echo "[*] Checking Firewall Status..."
if sudo ufw status | grep -q "active"; then
    echo -e "${GREEN}[PASS] Firewall is ACTIVE.${NC}"
else
    echo -e "${RED}[FAIL] Firewall is INACTIVE. Recommendation: Enable UFW.${NC}"
fi

# 2. CHECK DISK USAGE
# Warn if root partition is over 90% full
echo "[*] Checking Disk Usage..."
DISK_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
if [ "$DISK_USAGE" -gt 90 ]; then
    echo -e "${RED}[WARNING] Disk usage is critical: $DISK_USAGE%${NC}"
else
    echo -e "${GREEN}[PASS] Disk usage is healthy: $DISK_USAGE%${NC}"
fi

# 3. CHECK FOR ROOT SSH LOGIN
# Security best practice: Root should not log in remotely
echo "[*] Checking SSH Configuration..."
if grep -q "^PermitRootLogin yes" /etc/ssh/sshd_config; then
    echo -e "${RED}[FAIL] Remote Root Login is ALLOWED (Security Risk).${NC}"
else
    echo -e "${GREEN}[PASS] Remote Root Login looks secure (or is disabled).${NC}"
fi

echo "========================================"