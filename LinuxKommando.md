# Linux Kommandolinje
## directory traversal
1. pwd - Nuværende position i en sti
```bash
pwd
```
```console
┌──(kali㉿kali)-[~]
└─$ pwd         
/home/kali
```
2. skift directory/mappe
```bash
cd /your/path
```
```console
┌──(kali㉿kali)-[~]
└─$ cd /etc/                                
                                                                                                        
┌──(kali㉿kali)-[/etc]
└─$ 
```
3. dan dig et overblik over mapper og filer
```bash
tree
```
```console
┌──(kali㉿kali)-[/etc]
└─$ tree                      
.
├── adduser.conf
├── alsa
│   └── conf.d
│       ├── 10-rate-lav.conf -> /usr/share/alsa/alsa.conf.d/10-rate-lav.conf
│       ├── 10-samplerate.conf -> /usr/share/alsa/alsa.conf.d/10-samplerate.conf
│       ├── 10-speexrate.conf -> /usr/share/alsa/alsa.conf.d/10-speexrate.conf
│       ├── 50-arcam-av-ctl.conf -> /usr/share/alsa/alsa.conf.d/50-arcam-av-ctl.conf
│       ├── 50-jack.conf -> /usr/share/alsa/alsa.conf.d/50-jack.conf
│       ├── 50-oss.conf -> /usr/share/alsa/alsa.conf.d/50-oss.conf
│       ├── 50-pulseaudio.conf -> /usr/share/alsa/alsa.conf.d/50-pulseaudio.conf
│       ├── 60-a52-encoder.conf -> /usr/share/alsa/alsa.conf.d/60-a52-encoder.conf
│       ├── 60-speex.conf -> /usr/share/alsa/alsa.conf.d/60-speex.conf
│       ├── 60-upmix.conf -> /usr/share/alsa/alsa.conf.d/60-upmix.conf
│       ├── 60-vdownmix.conf -> /usr/share/alsa/alsa.conf.d/60-vdownmix.conf
│       ├── 98-usb-stream.conf -> /usr/share/alsa/alsa.conf.d/98-usb-stream.conf
│       ├── 99-pulseaudio-default.conf.example
│       └── 99-pulse.conf -> /usr/share/alsa/alsa.conf.d/pulse.conf
├── alternatives
│   ├── ABORT.7.gz -> /usr/share/postgresql/17/man/man7/ABORT.7.gz
│   ├── ALTER_AGGREGATE.7.gz -> /usr/share/postgresql/17/man/man7/ALTER_AGGREGATE.7.gz
│   ├── ALTER_COLLATION.7.gz -> /usr/share/postgresql/17/man/man7/ALTER_COLLATION.7.gz
│   ├── ALTER_CONVERSION.7.gz -> /usr/share/postgresql/17/man/man7/ALTER_CONVERSION.7.gz

```
4. Find en specific mappe eller fil
```bash
find -name "target.example"
```
```console
──(kali㉿kali)-[~]
└─$ find -name "passwords.txt"
./.cache/vmware/drag_and_drop/VW0wO7/passwords.txt
./.config/google-chrome/ZxcvbnData/3/passwords.txt
./.config/chromium/ZxcvbnData/3/passwords.txt
./.local/share/Trash/files/BastionHostingCreds (2)/passwords.txt
./passwords.txt
```
5. Find en specific mappe eller fil uden at være case sensitive
```bash
find -iname "target.example"
```
```console
┌──(kali㉿kali)-[~]
└─$ find -iname "pAssWordS.txt"
./.cache/vmware/drag_and_drop/VW0wO7/passwords.txt
./.config/google-chrome/ZxcvbnData/3/passwords.txt
./.config/chromium/ZxcvbnData/3/passwords.txt
./.local/share/Trash/files/BastionHostingCreds (2)/passwords.txt
./passwords.txt
```
6. Find fil efter type
```bash
find , -name "*conf"
```
```console
┌──(kali㉿kali)-[~]
└─$ find . -name "*.conf"      
./.cache/vmware/drag_and_drop/hKonY4/python-opgaver/etc/test.conf
./.cache/vmware/drag_and_drop/hKonY4/python-opgaver/etc/verysecret.conf
./.cache/vmware/drag_and_drop/hKonY4/python-opgaver/data/funny_config.conf
./.config/qt6ct/qt6ct.conf
./.goenv/versions/1.23.1/src/net/testdata/freebsd-usevc-resolv.conf
./.goenv/versions/1.23.1/src/net/testdata/linux-use-vc-resolv.conf
./.goenv/versions/1.23.1/src/net/testdata/large-ndots-resolv.conf
```
7. Find fil efter størrelse hvor "+100M" betyder mere end 100 Megabytes".  Med "/" for root og systemet og med "." for nuværende mappe.
```bash
find . -size +100M
```
```console
┌──(kali㉿kali)-[~]
└─$ find . -size +100M 
./google-chrome-stable_current_amd64.deb
./google-chrome-stable_current_amd64.deb.1
./.BurpSuite/burpbrowser/139.0.7258.127/chrome
```
8. Find filer der er ændret for nyligt hvor "-10" betyder "less than 10". Med "/" for root og systemet og med "." for nuværende mappe.
```bash
find . -mmin -10
```
```console
┌──(kali㉿kali)-[~]
└─$ find . -mmin -10
.
./JustCreatedThisFile.txt
./.local/share/gvfs-metadata/home-16b65ecb.log
./.local/share/Trash/info
./.local/share/Trash/info/JustMadeThisFolder.txt.trashinfo
./.local/share/Trash/files
./.local/share/Trash/files/JustMadeThisFolder.txt
```

## list (ls)
1. ls (list) - viser indholdet i den mappe du befinder dig i.
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
2. for at se skjulte filer og rettigheder
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
3. for at se alle filerne i human readable
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
4. Se filstørrelse i humand readable
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
5. hvis du ønsker at sortere med sidst ændret først (brug -tr for omvendt rækkefølge)
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
6. Sorteret med sidst ændret først og skjulte filer inkluderet (brug -atr for omvendt rækkefølge)
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
7. Sorteret efter størrelse, største først (brug --lSr for omvendt rækkefølge)
```bash
ls -lS
```
```console
┌──(kali㉿kali)-[~]
└─$ ls -lS             
total 265164
-rw-rw-r-- 1 kali kali 117773952 Nov 11 13:52 google-chrome-stable_current_amd64.deb
-rw-rw-r-- 1 kali kali 117773952 Nov 11 13:52 google-chrome-stable_current_amd64.deb.1
-rwxr-xr-x 1 kali kali  25268408 Oct 23 17:58 ngrok
-rw-rw-r-- 1 kali kali   9322550 Oct 30 05:29 ngrok-v3-stable-linux-amd64.tgz
-rw-rw-r-- 1 kali kali   1227855 Oct 27 07:55 replay_pid1882.log
-rw-rw-r-- 1 kali kali     36916 Oct 27 11:59 article.html
-rw------- 1 kali kali      8302 Oct 23 07:09 AbuIshak.ovpn
drwxr-xr-x 2 kali kali      4096 Oct 30 11:31 Desktop
```
8. Se alle filer i en mappe med dens under-mapper og filer
```bash
ls -R
```
```console
┌──(kali㉿kali)-[~]
└─$ ls -R
.:
1to100.py      extract_article.py                        ngrok                            Templates
AbuIshak.ovpn  fragmentation_scan.txt                    ngrok-v3-stable-linux-amd64.tgz  udp_scan.txt
article.html   google-chrome-stable_current_amd64.deb    numbers.txt                      userpass.txt
combined.txt   google-chrome-stable_current_amd64.deb.1  passwords.txt                    users.txt
Desktop        JustCreatedThisFile.txt                   Pictures                         Videos
Documents      mender.req                                Public
Downloads      mender.txt                                python-opgaver
emails.txt     Music                                     replay_pid1882.log

./Desktop:

./Documents:

./Downloads:
cacert.der  chinese-names.txt.gz  >>>>>>>>> >>>>>>>>> DenneFilLiggerIDownloads.txt <<<<<<<<< <<<<<<<<<
```
9. Klassificer filetyper, for en klar forståelse. Denne sætter eksempelvis et "*" på slutningen af filer som kan køres
```bash
ls -F
```
```console
┌──(kali㉿kali)-[~]
└─$ ls -F
1to100.py      extract_article.py                        ngrok*                           Templates/
AbuIshak.ovpn  fragmentation_scan.txt                    ngrok-v3-stable-linux-amd64.tgz  udp_scan.txt
article.html   google-chrome-stable_current_amd64.deb    numbers.txt                      userpass.txt
combined.txt   google-chrome-stable_current_amd64.deb.1  passwords.txt                    users.txt
```






