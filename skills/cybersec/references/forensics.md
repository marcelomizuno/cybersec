# Digital Forensics (Memory and Disk)

> Source: huggingface.co/datasets/Vyber07/cyber-security (Apache-2.0). Community-curated reference; verify commands and versions before use.

## How to perform memory forensics on a compromised system?

#### Memory Forensics Guide

##### Memory Acquisition
```bash
# Using WinPmem
winpmem_mini_x64.exe memdump.raw

# Using DumpIt
DumpIt.exe

# Using LiME (Linux)
insmod lime.ko "path=/tmp/mem.lime format=lime"
```

##### Volatility Analysis
```bash
# Identify OS profile
volatility -f memdump.raw imageinfo

# List processes
volatility -f memdump.raw --profile=Win7SP1x64 pslist

# Process tree
volatility -f memdump.raw --profile=Win7SP1x64 pstree

# Hidden processes
volatility -f memdump.raw --profile=Win7SP1x64 psxview

# Network connections
volatility -f memdump.raw --profile=Win7SP1x64 netscan

# Command history
volatility -f memdump.raw --profile=Win7SP1x64 cmdscan
volatility -f memdump.raw --profile=Win7SP1x64 consoles

# DLLs
volatility -f memdump.raw --profile=Win7SP1x64 dlllist

# Injected code
volatility -f memdump.raw --profile=Win7SP1x64 malfind

# Registry
volatility -f memdump.raw --profile=Win7SP1x64 hivelist
volatility -f memdump.raw --profile=Win7SP1x64 hashdump
```

##### Malware Detection
```bash
# YARA scanning
volatility -f memdump.raw --profile=Win7SP1x64 yarascan -Y "rule malware { strings: $a = \"cmd.exe\" condition: $a }"

# API hooking detection
volatility -f memdump.raw --profile=Win7SP1x64 apihooks

# SSDT hooks
volatility -f memdump.raw --profile=Win7SP1x64 ssdt

# Driver analysis
volatility -f memdump.raw --profile=Win7SP1x64 driverscan
volatility -f memdump.raw --profile=Win7SP1x64 modscan
```

##### Evidence Extraction
```bash
# Extract files
volatility -f memdump.raw --profile=Win7SP1x64 filescan
volatility -f memdump.raw --profile=Win7SP1x64 dumpfiles -Q <offset> -D output/

# Extract processes
volatility -f memdump.raw --profile=Win7SP1x64 procdump -D output/

# Extract registry
volatility -f memdump.raw --profile=Win7SP1x64 dumpregistry -D output/
```

##### Tools
- Volatility 2/3
- Rekall
- WinPmem
- LiME
- YARA

## How to perform disk forensics on a seized computer?

#### Disk Forensics Guide

##### Disk Imaging
```bash
# Create forensic image with dd
dd if=/dev/sda of=/evidence/disk.img bs=4M status=progress

# Create with dcfldd (forensic dd)
dcfldd if=/dev/sda of=/evidence/disk.img hash=sha256 hashlog=/evidence/hash.txt

# Create E01 image with ewfmount
ewfacquire /dev/sda

# Verify integrity
sha256sum /evidence/disk.img
md5sum /evidence/disk.img
```

##### Mounting Image
```bash
# Mount raw image
mount -o loop,ro,noexec /evidence/disk.img /mnt/evidence

# Mount E01 image
ewfmount /evidence/disk.E01 /mnt/ewf
mount -o loop,ro,noexec /mnt/ewf/ewf1 /mnt/evidence

# Mount with Sleuth Kit
fls -r /evidence/disk.img
icat /evidence/disk.img <inode> > extracted_file
```

##### File System Analysis
```bash
# List files
fls -r /evidence/disk.img

# File timeline
fls -m "" -r /evidence/disk.img > body.txt
mactime -b body.txt > timeline.csv

# Recover deleted files
fls -d /evidence/disk.img
icat /evidence/disk.img <inode> > recovered_file

# Extract metadata
istat /evidence/disk.img <inode>
```

##### Artifact Analysis
```bash
# Windows artifacts
# Registry hives
regripper -r /mnt/evidence/Windows/System32/config/SYSTEM

# Event logs
evtexport /mnt/evidence/Windows/System32/winevt/Logs/Security.evtx

# Prefetch files
# Located in Windows/Prefetch/

# Browser history
# Chrome: %LOCALAPPDATA%/Google/Chrome/User Data/Default/History
# Firefox: %APPDATA%/Mozilla/Firefox/Profiles/*.default/places.sqlite

# Recent files
# C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\
```

##### Timeline Analysis
```bash
# Create Super Timeline
log2timeline.py --storage-file timeline.plaso /evidence/disk.img
psort.py -o l2tcsv timeline.plaso > timeline.csv

# Analyze with Timeline Explorer
# Import CSV into Timeline Explorer
```

##### Tools
- Sleuth Kit
- Autopsy
- FTK Imager
- EnCase
- Plaso/log2timeline
- RegRipper
- Volatility

## How to perform network forensics after a security incident?

#### Network Forensics Guide

##### Capture Analysis
```bash
# Basic analysis with tshark
tshark -r capture.pcap -T fields -e frame.time -e ip.src -e ip.dst -e tcp.port

# Filter by IP
tshark -r capture.pcap -Y 'ip.addr == 192.168.1.100'

# Filter by time range
tshark -r capture.pcap -Y 'frame.time >= "2024-01-01 10:00:00" && frame.time <= "2024-01-01 12:00:00"'
```

##### Protocol Analysis
```bash
# HTTP requests
tshark -r capture.pcap -Y 'http.request' -T fields -e http.host -e http.request.uri

# DNS queries
tshark -r capture.pcap -Y 'dns' -T fields -e dns.qry.name -e dns.a

# TLS connections
tshark -r capture.pcap -Y 'tls' -T fields -e tls.handshake.type -e tls.handshake.cipher_suites
```

##### Attack Reconstruction
```bash
# Extract files
foremost -i capture.pcap -o extracted/

# Reconstruct TCP streams
tshark -r capture.pcap -q -z follow,tcp,ascii,0

# HTTP objects
tshark -r capture.pcap --export-objects http,exported/

# DNS tunneling detection
tshark -r capture.pcap -Y 'dns.qry.name.len > 50'
```

##### IOC Extraction
```bash
# Extract IPs
tshark -r capture.pcap -T fields -e ip.src | sort | uniq -c | sort -rn

# Extract domains
tshark -r capture.pcap -Y 'dns' -T fields -e dns.qry.name | sort | uniq

# Extract URLs
tshark -r capture.pcap -Y 'http.request' -T fields -e http.host -e http.request.uri

# Extract user agents
tshark -r capture.pcap -Y 'http.request' -T fields -e http.user_agent
```

##### Timeline Reconstruction
```bash
# Create timeline
tshark -r capture.pcap -T fields -e frame.time -e ip.src -e ip.dst -e _ws.col.Protocol -e _ws.col.Info > timeline.csv

# Analyze with Wireshark
# Statistics -> Conversations
# Statistics -> Endpoints
# Statistics -> Protocol Hierarchy
```

##### Tools
- Wireshark
- tshark
- tcpdump
- NetworkMiner
- Chaosreader
- Foremost
