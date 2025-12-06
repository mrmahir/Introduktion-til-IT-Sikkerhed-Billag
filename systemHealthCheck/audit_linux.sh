#!/bin/bash

# --- Linux Security & Health Auditor ---
# This script checks firewall status, disk usage, and SSH configuration.

# Define Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# TRACKING VARIABLE: Assume system is safe until proven otherwise
ALL_CHECKS_PASSED=true

echo "========================================"
echo "   LINUX SYSTEM DIAGNOSTIC TOOL"
echo "========================================"

# 1. CHECK FIREWALL (UFW)
echo "[*] Checking Firewall Status..."
if sudo ufw status | grep -q "active"; then
    echo -e "${GREEN}[PASS] Firewall is ACTIVE.${NC}"
else
    echo -e "${RED}[FAIL] Firewall is INACTIVE. Recommendation: Enable UFW.${NC}"
    ALL_CHECKS_PASSED=false
fi

# 2. CHECK DISK USAGE (Assuming < 90% is good)
echo "[*] Checking Disk Usage..."
DISK_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
if [ "$DISK_USAGE" -gt 90 ]; then
    echo -e "${RED}[WARNING] Disk usage is critical: $DISK_USAGE%${NC}"
    ALL_CHECKS_PASSED=false
else
    echo -e "${GREEN}[PASS] Disk usage is healthy: $DISK_USAGE%${NC}"
fi

# 3. CHECK FOR ROOT SSH LOGIN
echo "[*] Checking SSH Configuration..."
if grep -q "^PermitRootLogin yes" /etc/ssh/sshd_config; then
    echo -e "${RED}[FAIL] Remote Root Login is ALLOWED (Security Risk).${NC}"
    ALL_CHECKS_PASSED=false
else
    echo -e "${GREEN}[PASS] Remote Root Login looks secure (or is disabled).${NC}"
fi

echo "========================================"

# FINAL VERDICT
if [ "$ALL_CHECKS_PASSED" = true ]; then
    echo ""
    echo -e "${GREEN}Your computer is safe, but your country is never truly safe from the Ottomans 🇹🇷 🇹🇷 🇹🇷${NC}"
    echo ""
fi