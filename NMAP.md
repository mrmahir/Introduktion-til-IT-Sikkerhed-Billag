# NMAP 

## Simpel scan
Simpel scan, der tjekker de 1000 mest almindelige porte med deres retur-svar, samt om målet er i live.

```bash
nmap dr.dk
```
Herfra kan vi se hvilke porte der er åbne og lidt andet. Se med her.
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
Man kan køre dette scan på flere forskellige måder, eksempelvis kan man lave en kort pause (2s) før næste pakke for ikke
at blive blokeret således
```bash
nmap --scan-delay 2s dr.dk
```
Eller lave et stealth scan som har samme formål med
```bash
sudo nmap --sS dr.dk
```
Eller en kombination af begge options. Omvendt kan man køre hurtige scan hvis man scanner flere maskiner på en gang med
```bash
sudo nmap -F dr.dk
```
Eller hvis du øsnker at få feedback imens scanningen er igang
```bash
sudo nmap -v dr.dk
```
## Service Version Detection (option -sV)
For at finde hvilken software og hvilken version der kører bag en port bruger man -sV
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

