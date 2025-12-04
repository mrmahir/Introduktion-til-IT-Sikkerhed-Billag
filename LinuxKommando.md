# Linux Kommandolinje
## pwd
pwd - Nuværende position i en sti
```bash
pwd
```
```console
┌──(kali㉿kali)-[~]
└─$ pwd         
/home/kali
```
## list (ls)
ls (list) - viser indholdet i den mappe du befinder dig i.
```bash
ls
```
```console
┌──(kali㉿kali)-[~]
└─$ ls    
1to100.py           fragmentation_scan.txt                    passwords.txt
AbuIshak.ovpn       google-chrome-stable_current_amd64.deb    Pictures
article.html        google-chrome-stable_current_amd64.deb.1  Public
combined.txt        mender.req                                replay_pid1882.log
Desktop             mender.txt                                Templates
```
for at se skjulte filer og rettigheder
```bash
ls -la
```
```console
└─$ la -la
total 265300
drwx------ 22 kali kali      4096 Dec  4 07:32 .
drwxr-xr-x  3 root root      4096 Sep  9 06:19 ..
-rw-rw-r--  1 kali kali       262 Nov  3 14:13 1to100.py
-rw-------  1 kali kali      8302 Oct 23 07:09 AbuIshak.ovpn
-rw-rw-r--  1 kali kali     36916 Oct 27 11:59 article.html
-rw-r--r--  1 kali kali       220 Sep  9 06:19 .bash_logout
-rw-r--r--  1 kali kali      6050 Oct 30 11:22 .bashrc
-rw-r--r--  1 kali kali      3526 Sep  9 06:19 .bashrc.original
drwx------  8 kali kali      4096 Nov 16 10:51 .BurpSuite
```
for at se alle filerne i human readable
```bash
ls -ah
```
```console
┌──(kali㉿kali)-[~]
└─$ ls -ah
.                   .face.icon                                .pki
..                  fragmentation_scan.txt                    .profile
1to100.py           .gnupg                                    Public
AbuIshak.ovpn       .goenv                                    .pyenv
article.html        google-chrome-stable_current_amd64.deb    replay_pid1882.log
.bash_logout        google-chrome-stable_current_amd64.deb.1  .ssh
.bashrc             .ICEauthority                             .sudo_as_admin_successful
.bashrc.original    .java                                     Templates
.BurpSuite          .local                                    udp_scan.txt
.cache              mender.req                                userpass.txt
```
Se filstørrelse i humand readable
```bash
ls -lh
```
```console
┌──(kali㉿kali)-[~]
└─$ ls -lh
total 259M
-rw-rw-r-- 1 kali kali  262 Nov  3 14:13 1to100.py
-rw------- 1 kali kali 8.2K Oct 23 07:09 AbuIshak.ovpn
-rw-rw-r-- 1 kali kali  37K Oct 27 11:59 article.html
-rw-r--r-- 1 kali kali 3.6K Aug 16  2021 combined.txt
drwxr-xr-x 2 kali kali 4.0K Oct 30 11:31 Desktop
drwxr-xr-x 2 kali kali 4.0K Oct 23 06:27 Documents
drwxr-xr-x 2 kali kali 4.0K Nov 22 13:46 Downloads
-rw-r--r-- 1 kali kali 2.8K Aug  9  2021 emails.txt
```


hvis du ønsker at sortere med sidst ændret først
```bash
ls -t
```
```console
┌──(kali㉿kali)-[~]
└─$ ls -t 
udp_scan.txt            Downloads                                 extract_article.py  Pictures
fragmentation_scan.txt  google-chrome-stable_current_amd64.deb    article.html        Public
mender.txt              google-chrome-stable_current_amd64.deb.1  replay_pid1882.log  Templates
mender.req              numbers.txt                               ngrok               Videos
userpass.txt            1to100.py                                 AbuIshak.ovpn       combined.txt
passwords.txt           Desktop                                   Documents           emails.txt
users.txt               ngrok-v3-stable-linux-amd64.tgz           Music
```
Sorteret med sidst ændret først og skjulte filer inkluderet
```bash
ls -at
```
```console
┌──(kali㉿kali)-[~]
└─$ ls -at
.                                         numbers.txt                      .java
.xsession-errors                          1to100.py                        .gnupg
.Xauthority                               Desktop                          .ICEauthority
.xsession-errors.old                      .bashrc                          Documents
.zsh_history                              .zshrc                           Music
udp_scan.txt                              .pyenv                           Pictures
fragmentation_scan.txt                    .goenv                           Public
```






