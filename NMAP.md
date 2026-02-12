# NMAP 

## Simple scan
Simple scan that checks the 1000 most common ports with their return responses and if the target is alive.

```bash
nmap dr.dk
```
From here we can see which ports are open and a bit more. Look here.
```console
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-03 12:07 EST
Nmap scan report for dr.dk (2.23.172.114)
Host is up (0.0032s latency).
Other addresses for dr.dk (not scanned): 2.23.172.130 2a02:26f0:a00::17c7:4b63 2a02:26f0:a00::17c7:4b48
rDNS record for 2.23.172.114: a2-23-172-114.deploy.static.akamaitechnologies.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 4.44 seconds

```
You can run this scan in several different ways, for example you can make a short pause (2s) before the next package to not
be blocked by doing so
```bash
nmap --scan-delay 2s dr.dk
```
Or do a stealth scan which has the same purpose with
```bash
sudo nmap --sS dr.dk
```
Or a combination of both options. Conversely, you can run fast scans if you scan multiple machines at once with
```bash
sudo nmap -F dr.dk
```
Or if you want to get feedback while the scan is in progress (note, this type of scan requires "sudo" to work)
```bash
sudo nmap -v dr.dk
```
## Service Version Detection (option -sV)
To find which software and which version is running behind a port, use -sV
```bash
nmap --sV dr.dk
```
```console
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-03 12:34 EST
Nmap scan report for dr.dk (2.23.172.114)
Host is up (0.0036s latency).
Other addresses for dr.dk (not scanned): 2.23.172.130 2a02:26f0:a00::17c7:4b63 2a02:26f0:a00::17c7:4b48
rDNS record for 2.23.172.114: a2-23-172-114.deploy.static.akamaitechnologies.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)
443/tcp open  ssl/http AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.37 seconds
```
## OS detection
To find the operating system and thereby have a strong recon overview of your target, you can run this (note, this type of scan requires "sudo" to work)
```bash
nmap --O dr.dk
```
```console
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-03 12:38 EST
Nmap scan report for dr.dk (2.23.172.114)
Host is up (0.0036s latency).
Other addresses for dr.dk (not scanned): 2.23.172.130 2a02:26f0:a00::17c7:4b48 2a02:26f0:a00::17c7:4b63
rDNS record for 2.23.172.114: a2-23-172-114.deploy.static.akamaitechnologies.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, Linux 4.19, Linux 5.0 - 5.14, OpenWrt 21.02 (Linux 5.4), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 5 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.41 seconds

```


