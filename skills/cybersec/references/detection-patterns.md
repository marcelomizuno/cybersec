# Attack Patterns: How They Work and How to Detect Them

> Source: huggingface.co/datasets/Vyber07/cyber-security (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Brute Force Authentication Attack
- **How to attack**: Use Hydra, Medusa, or custom scripts to try thousands of password combinations against login endpoints. Target SSH, RDP, FTP, web logins. Use credential lists from data breaches. Rotate source IPs to avoid rate limiting.
- **How to detect**: Monitor for multiple failed authentication attempts from same source. Threshold: >10 failures in 5 minutes. Watch for distributed brute force from botnets.

### Log analysis

- **Windows event logs**: Event ID 4625 (failed logon) - Filter by SourceNetworkAddress, count by IpAddress. Event ID 4771 (Kerberos pre-auth failed). Event ID 4776 (NTLM auth failed).
- **Linux logs**: cat /var/log/auth.log | grep 'Failed password' | awk '{print $11}' | sort | uniq -c | sort -rn. cat /var/log/secure | grep 'authentication failure'.
- **Web server logs**: cat access.log | grep 'POST /login' | grep '401' | awk '{print $1}' | sort | uniq -c | sort -rn. Count 401 responses per IP.
- **Firewall logs**: grep 'DENY.*22' firewall.log | awk '{print $3}' | sort | uniq -c | sort -rn. Look for repeated connection attempts to auth ports.

### Detection rules

**Sigma**

```yaml
title: Brute Force Detection
detection:
  selection:
    EventID: 4625
  timeframe: 5m
  condition: selection | count(TargetUserName) by IpAddress > 10
```

- **Splunk**: index=windows EventCode=4625 | stats count by IpAddress, TargetUserName | where count > 10
- **Elk**: event.action:"failed-logon" | groupby source.ip | having count > 10
- **Snort**: alert tcp any any -> $HOME_NET 22 (msg:"SSH Brute Force"; flow:to_server; content:"SSH"; threshold:type both, track by_src, count 10, seconds 60; sid:1000001;)

### Defense steps

- Implement account lockout policies (5 attempts, 30 min lockout)
- Enable multi-factor authentication (MFA) on all accounts
- Deploy fail2ban or similar IP blocking
- Use CAPTCHA after 3 failed attempts
- Implement geo-blocking for unexpected regions
- Use certificate-based authentication where possible
- Monitor and alert on brute force patterns
- Implement rate limiting on login endpoints
- Use passwordless authentication (FIDO2/WebAuthn)
- Regular password audits and breach checks

- **Mitre attack**: T1110.001 - Brute Force: Password Guessing
- **Severity**: high

## Lateral Movement via PsExec
- **How to attack**: Use PsExec to execute commands on remote Windows systems. Requires admin credentials. PsExec creates a Windows service on target, executes command, returns output. Common for post-exploitation lateral movement.
- **How to detect**: Monitor for new service creation (Event ID 7045). Watch for PSEXESVC named pipe connections. Detect SMB connections followed by service creation. Monitor for cmd.exe/powershell.exe spawned by services.exe with unusual parents.

### Log analysis

- **Windows event logs**: Event ID 7045 (service installed) - Filter by ServiceName containing 'PSEXE'. Event ID 4624 Type 3 (network logon). Event ID 5145 (network share access). Sysmon Event ID 1 (process creation) with ParentImage services.exe.
- **Network logs**: SMB connections on port 445 followed by named pipe access \\*\pipe\PSEXESVC. Monitor for DCERPC traffic to port 135 followed by SMB.
- **Siem query**: index=windows (EventCode=7045 ServiceName=*PSEX*) OR (EventCode=4624 LogonType=3) | stats count by ComputerName, SubjectUserName

### Detection rules

**Sigma**

```yaml
title: PsExec Execution
detection:
  selection1:
    EventID: 7045
    ServiceName|contains: 'PSEXE'
  selection2:
    EventID: 1
    ParentImage|endswith: '\services.exe'
    Image|endswith: '\cmd.exe'
  condition: selection1 or selection2
```

**Yara**

```
rule PsExec_Detection {
  strings:
    $s1 = "PSEXESVC"
    $s2 = "PsExec"
  condition:
    $s1 or $s2
}
```

- **Splunk**: index=windows (EventCode=7045 ServiceName=*PSEX*) OR (EventCode=1 ParentImage=*services.exe Image=*cmd.exe) | stats count by Computer, Image

### Defense steps

- Implement privileged access workstations (PAW)
- Restrict admin credential usage to specific systems
- Enable PowerShell logging (Module, ScriptBlock, Transcription)
- Deploy EDR with lateral movement detection
- Implement network segmentation between user and server VLANs
- Monitor for new service creation events
- Restrict SMB access between workstations
- Use Windows Defender Application Control (WDAC)
- Implement just-in-time (JIT) admin access
- Regular credential rotation for admin accounts

- **Mitre attack**: T1021.002 - Remote Services: SMB/Windows Admin Shares
- **Severity**: high

## SQL Injection Attack
- **How to attack**: Inject SQL code through user input fields. Use UNION-based, blind boolean, time-based, or error-based techniques. Tools: sqlmap, Havij, manual testing. Target login forms, search fields, URL parameters.
- **How to detect**: Monitor web application logs for SQL keywords in input. Watch for 500 errors with SQL error messages. Detect unusual database query patterns. Monitor for information_schema queries.

### Log analysis

- **Web server logs**: grep -iE '(union|select|insert|update|delete|drop|exec|concat|char|0x)' access.log. grep '500' access.log | grep -i 'sql\|mysql\|oracle\|syntax'. Look for encoded SQL payloads.
- **Waf logs**: grep 'SQL Injection' waf.log | awk '{print $1}' | sort | uniq -c | sort -rn. Check blocked requests with SQL keywords.
- **Database logs**: Enable query logging. Look for SELECT FROM information_schema. Look for UNION SELECT queries. Monitor for database enumeration attempts.
- **Siem query**: index=web (status=500 AND (uri=*union* OR uri=*select* OR uri=*drop*)) OR (waf_action=block AND waf_rule=*sqli*)

### Detection rules

**Sigma**

```yaml
title: SQL Injection Attempt
detection:
  selection:
    EventID: 1
    CommandLine|contains|all:
      - 'union'
      - 'select'
  filter:
    Image|endswith: '\sqlservr.exe'
  condition: selection and not filter
```

- **Snort**: alert tcp any any -> $HOME_NET 80 (msg:"SQL Injection Attempt"; content:"union"; nocase; content:"select"; nocase; http_uri; sid:1000002;)
- **Splunk**: index=web (uri=*union*select*) OR (uri=*' OR *) OR (uri=*--*) | stats count by src_ip, uri | where count > 5

**Yara**

```
rule SQLi_Payload {
  strings:
    $s1 = "union select" nocase
    $s2 = "' or '1'='1" nocase
    $s3 = "; drop table" nocase
  condition:
    any of them
}
```

### Defense steps

- Use parameterized queries / prepared statements for ALL database calls
- Implement input validation and whitelisting
- Deploy Web Application Firewall (WAF) with SQL injection rules
- Use ORM frameworks instead of raw SQL
- Apply principle of least privilege to database accounts
- Disable verbose error messages in production
- Implement rate limiting on database-intensive endpoints
- Regular security testing with sqlmap and manual testing
- Enable database query logging and monitoring
- Use stored procedures with parameterized inputs

- **Mitre attack**: T1190 - Exploit Public-Facing Application
- **Severity**: critical

## Ransomware File Encryption Activity
- **How to attack**: Deploy ransomware payload via phishing, RDP compromise, or exploit. Encrypt files using AES-256 + RSA-2048. Delete shadow copies. Modify MBR. Display ransom note. Exfiltrate data before encryption (double extortion).
- **How to detect**: Monitor for mass file rename operations. Watch for vssadmin delete shadows commands. Detect high CPU/disk usage. Monitor for .encrypted/.locked file extensions. Watch for ransom note file creation.

### Log analysis

- **Windows event logs**: Event ID 4663 (file access) - High volume of file modifications. Event ID 7045 (service creation for persistence). Sysmon Event ID 11 (file creation) with ransom extensions. PowerShell logs for vssadmin commands.
- **File system**: Monitor for mass file extension changes. Watch for README_DECRYPT.txt creation. Detect high file I/O rates. Monitor recycle bin for shadow copy deletion.
- **Network logs**: Look for data exfiltration before encryption. Monitor for C2 communication. Watch for large outbound data transfers.
- **Siem query**: index=windows (EventCode=4663 AND ObjectName=*.* AND AccessMask=0x2) | bucket _time span=1m | stats count by ComputerName | where count > 100

### Detection rules

**Sigma**

```yaml
title: Ransomware Activity
detection:
  selection1:
    EventID: 1
    CommandLine|contains: 'vssadmin delete shadows'
  selection2:
    EventID: 11
    TargetFilename|endswith:
      - '.encrypted'
      - '.locked'
      - '.crypto'
  condition: selection1 or selection2
```

- **Splunk**: index=windows (EventCode=4663) | bucket _time span=1m | stats dc(ObjectName) as files_modified by ComputerName | where files_modified > 100

**Yara**

```
rule Ransomware_Activity {
  strings:
    $s1 = "vssadmin delete shadows" nocase
    $s2 = "@WanaDecryptor@"
    $s3 = "README_DECRYPT"
  condition:
    any of them
}
```

### Defense steps

- Maintain offline/air-gapped backups tested regularly
- Implement network segmentation (IT/OT, user/server)
- Deploy EDR with ransomware behavior detection
- Disable macros in Office documents via Group Policy
- Enable Controlled Folder Access in Windows Defender
- Implement application allowlisting
- Patch all systems within 48 hours for critical vulns
- Enable PowerShell logging and constrain language mode
- Block SMBv1 and restrict lateral movement
- Implement email security gateway with sandboxing
- Regular disaster recovery testing
- Incident response plan with ransomware-specific playbook

- **Mitre attack**: T1486 - Data Encrypted for Impact
- **Severity**: critical

## Credential Dumping via Mimikatz
- **How to attack**: Execute Mimikatz to extract credentials from LSASS memory. Commands: privilege::debug, sekurlsa::logonpasswords, lsadump::sam. Use for pass-the-hash, pass-the-ticket, golden ticket attacks.
- **How to detect**: Monitor for access to LSASS process. Watch for Event ID 4673 (privileged service called). Detect Mimikatz-specific strings in memory. Monitor for suspicious DLLs loaded into LSASS.

### Log analysis

- **Windows event logs**: Sysmon Event ID 10 (ProcessAccess) - TargetImage lsass.exe with GrantedAccess 0x1010. Event ID 4673 (SensSvc privilege). Event ID 4688 (process creation) for mimikatz.exe.
- **Edr logs**: Monitor for LSASS memory access. Watch for known Mimikatz DLL names. Detect credential dumping API calls (MiniDumpWriteDump, ReadProcessMemory).
- **Siem query**: index=sysmon EventCode=10 TargetImage=*lsass.exe GrantedAccess=0x1010 | stats count by SourceImage | where count > 1

### Detection rules

**Sigma**

```yaml
title: Mimikatz Credential Dumping
detection:
  selection:
    EventID: 10
    TargetImage|endswith: '\lsass.exe'
    GrantedAccess|contains: '0x1010'
  condition: selection
```

**Yara**

```
rule Mimikatz {
  strings:
    $s1 = "mimikatz" nocase
    $s2 = "sekurlsa" nocase
    $s3 = "privilege::debug" nocase
    $s4 = "kerberos" nocase
  condition:
    2 of them
}
```

- **Splunk**: index=sysmon EventCode=10 TargetImage=*lsass.exe | stats count by SourceImage, GrantedAccess

### Defense steps

- Enable LSA Protection (RunAsPPL) via Group Policy
- Implement Credential Guard on Windows 10/Server 2016+
- Restrict debug privileges to specific admin accounts
- Deploy EDR with credential dumping detection
- Monitor LSASS process access events
- Implement privileged access workstations (PAW)
- Use Protected Users security group for admin accounts
- Regular credential rotation for all privileged accounts
- Implement tiered administration model
- Disable NTLM where possible, enforce Kerberos

- **Mitre attack**: T1003.001 - OS Credential Dumping: LSASS Memory
- **Severity**: critical

## Data Exfiltration via DNS Tunneling
- **How to attack**: Encode data in DNS queries using base32/base64 encoding. Use long subdomains to carry data. Tools: Iodine, DNScat2, Cobalt Strike DNS beacon. Bypass firewalls that allow DNS traffic.
- **How to detect**: Monitor for unusually long DNS queries (>50 characters). Watch for high DNS query volume from single hosts. Detect base64 patterns in subdomains. Monitor for TXT record queries.

### Log analysis

- **Dns logs**: awk 'length($0) > 100' dns.log. Look for queries to single domain with random subdomains. Monitor TXT record queries. Check query frequency per host.
- **Network logs**: Monitor DNS traffic volume. Look for DNS packets larger than normal (>512 bytes). Watch for DNS queries to unusual resolvers.
- **Siem query**: index=dns | eval query_len=len(query) | where query_len > 50 | stats count by src_ip, query | where count > 100

### Detection rules

**Sigma**

```yaml
title: DNS Tunneling Detection
detection:
  selection:
    EventID: 22
    QueryName|re: '.*[A-Za-z0-9+/=]{30,}.*'
  condition: selection
```

- **Splunk**: index=dns | eval query_len=len(query) | where query_len > 50 | stats count by src_ip, query_domain | where count > 50

**Zeek**

```
event dns_request(c: connection, msg: dns_msg, query: string, qtype: count, qclass: count) {
  if (|query| > 50) {
    NOTICE([$note=DNS::Long_Query, $msg=fmt("Long DNS query: %s", query), $conn=c]);
  }
}
```

- **Snort**: alert udp any any -> any 53 (msg:"DNS Tunnel - Long Query"; dsize:>100; sid:1000003;)

### Defense steps

- Implement DNS query length limits
- Deploy DNS security solutions (Cisco Umbrella, Infoblox)
- Monitor DNS query patterns and anomalies
- Block DNS to unauthorized resolvers
- Implement DNS response policy zones (RPZ)
- Use DNS-over-HTTPS for internal resolution
- Analyze DNS query entropy
- Implement data loss prevention (DLP)
- Monitor for DNS beaconing patterns
- Restrict TXT record queries where possible

- **Mitre attack**: T1071.004 - Application Layer Protocol: DNS
- **Severity**: high

## Privilege Escalation via Windows Service Exploitation
- **How to attack**: Find services with weak permissions (unquoted service paths, writable service binaries, DLL hijacking). Use accesschk.exe to enumerate permissions. Modify service binary or create malicious DLL. Restart service for SYSTEM access.
- **How to detect**: Monitor for service configuration changes. Watch for Event ID 7045 (new service) and 7040 (service start type changed). Detect binary modification in service paths. Monitor for DLL creation in service directories.

### Log analysis

- **Windows event logs**: Event ID 7045 (service installed) - New service creation. Event ID 7040 (service start type changed). Event ID 4657 (registry value modification) for service keys. Sysmon Event ID 11 (file creation) in service directories.
- **File integrity**: Monitor Program Files and System32 for new files. Watch for DLL creation in service directories. Detect binary modifications to service executables.
- **Siem query**: index=windows (EventCode=7045 OR EventCode=7040) | stats count by ComputerName, ServiceName, ImagePath

### Detection rules

**Sigma**

```yaml
title: Suspicious Service Creation
detection:
  selection:
    EventID: 7045
  filter:
    ServiceName|contains:
      - 'Windows'
      - 'Microsoft'
  condition: selection and not filter
```

- **Splunk**: index=windows EventCode=7045 | where NOT match(ServiceName, "(?i)(windows|microsoft|sql|vmware)") | stats count by Computer, ServiceName, ImagePath

### Defense steps

- Audit service permissions with accesschk.exe
- Fix unquoted service paths
- Restrict write permissions on service directories
- Implement service hardening via Group Policy
- Monitor for service configuration changes
- Deploy file integrity monitoring (FIM)
- Use Windows Service Hardening
- Implement application allowlisting
- Regular privilege escalation audits
- Use least privilege for service accounts

- **Mitre attack**: T1543.003 - Create or Modify System Process: Windows Service
- **Severity**: high

## Cross-Site Scripting (XSS) Attack
- **How to attack**: Inject JavaScript into web application input fields. Reflected: payload in URL/request. Stored: payload saved to database. DOM-based: payload in client-side code. Goal: steal cookies, redirect users, keylogging.
- **How to detect**: Monitor WAF logs for XSS payloads. Watch for script tags in HTTP requests. Detect onerror/onload handlers in input. Monitor CSP violation reports.

### Log analysis

- **Waf logs**: grep -iE '(<script|onerror|onload|javascript:|alert\()' waf.log. Monitor blocked XSS attempts. Track source IPs.
- **Web logs**: grep -iE '(<script|onerror|onload)' access.log. Look for encoded XSS payloads. Monitor 403/406 responses from WAF.
- **Csp reports**: Monitor Content-Security-Policy-Report-Only headers. Collect CSP violation reports. Analyze blocked script sources.
- **Siem query**: index=web (uri=*<script>* OR uri=*onerror=* OR uri=*javascript:*) | stats count by src_ip, uri

### Detection rules

**Sigma**

```yaml
title: XSS Attack Detection
detection:
  selection:
    EventID: 1
    CommandLine|contains:
      - '<script'
      - 'onerror'
      - 'javascript:'
  condition: selection
```

- **Snort**: alert tcp any any -> $HOME_NET 80 (msg:"XSS Attempt"; content:"<script"; nocase; http_uri; sid:1000004;)
- **Splunk**: index=web (uri=*<script>* OR uri=*onerror=* OR uri=*alert\(*) | stats count by src_ip, uri

### Defense steps

- Implement output encoding for ALL user-generated content
- Deploy Content Security Policy (CSP) headers
- Use HTTPOnly and Secure flags on cookies
- Implement input validation on server side
- Use frameworks with built-in XSS protection (React, Angular)
- Deploy WAF with XSS rules
- Enable X-XSS-Protection header
- Regular security testing with XSStrike, Burp Suite
- Implement Trusted Types API
- Sanitize HTML with DOMPurify library

- **Mitre attack**: T1189 - Drive-by Compromise
- **Severity**: high

## Command Injection Attack
- **How to attack**: Inject OS commands through application input. Use shell metacharacters (; | & ` $()). Chain commands to execute arbitrary code. Target: web forms, API endpoints, file upload functions.
- **How to detect**: Monitor for shell command patterns in HTTP requests. Watch for semicolons, pipes, backticks in input. Detect system commands (cat, ls, whoami, ping) in request parameters.

### Log analysis

- **Web logs**: grep -iE '(;|\||`|\$\(|whoami|cat /etc|/bin/sh|cmd.exe|powershell)' access.log. Monitor for encoded command injection payloads.
- **Waf logs**: grep 'Command Injection' waf.log. Track blocked requests with shell metacharacters.
- **Siem query**: index=web (uri=*;* OR uri=*|* OR uri=*`* OR uri=*whoami*) | stats count by src_ip, uri

### Detection rules

**Sigma**

```yaml
title: Command Injection Detection
detection:
  selection:
    CommandLine|contains:
      - ';'
      - '|'
      - '&&'
      - 'whoami'
      - '/etc/passwd'
  condition: selection
```

- **Snort**: alert tcp any any -> $HOME_NET 80 (msg:"Command Injection"; content:"|"; http_uri; content:"whoami"; sid:1000005;)
- **Splunk**: index=web (uri=*;cat* OR uri=*|ls* OR uri=*whoami* OR uri=*/) | stats count by src_ip, uri

### Defense steps

- Never pass user input to system commands
- Use language-specific APIs instead of shell commands
- Implement strict input validation and whitelisting
- Deploy WAF with command injection rules
- Use sandboxing for command execution
- Apply principle of least privilege to web application
- Disable unnecessary system utilities
- Regular security testing for command injection
- Implement application-level firewalls
- Use parameterized APIs for all system interactions

- **Mitre attack**: T1059 - Command and Scripting Interpreter
- **Severity**: critical

## Network Scanning and Reconnaissance
- **How to attack**: Use Nmap for port scanning (-sS, -sT, -sU). Service version detection (-sV). OS detection (-O). Script scanning (--script). Use slow scan to evade IDS. Target: identify open ports, services, vulnerabilities.
- **How to detect**: Monitor for connection attempts to multiple ports from single IP. Watch for SYN scans (half-open connections). Detect service enumeration probes. Monitor for unusual ICMP traffic.

### Log analysis

- **Firewall logs**: grep 'SYN' firewall.log | awk '{print $3}' | sort | uniq -c | sort -rn. Monitor for sequential port access. Watch for connections to unusual ports.
- **Ids logs**: grep 'SCAN' ids.log. Monitor for Nmap signatures. Watch for OS detection probes.
- **Network logs**: Monitor for connection rate per source IP. Watch for SYN without completion. Detect service banner requests.
- **Siem query**: index=network action=blocked | stats dc(dest_port) as ports_scanned by src_ip | where ports_scanned > 50

### Detection rules

**Sigma**

```yaml
title: Network Scanning Detection
detection:
  selection:
    EventID: 5156
    DestPort|contains: 'multiple'
  condition: selection | count by SourceAddress > 50
```

- **Snort**: alert tcp any any -> $HOME_NET any (msg:"Port Scan Detected"; flags:S; threshold:type both, track by_src, count 50, seconds 60; sid:1000006;)
- **Splunk**: index=network action=allowed | stats dc(dest_port) as ports by src_ip | where ports > 100 | sort -ports

### Defense steps

- Deploy network intrusion detection system (IDS/IPS)
- Implement rate limiting on firewall
- Use port knocking for sensitive services
- Deploy honeypots to detect scanning
- Implement network segmentation
- Block unused ports and services
- Monitor for scanning patterns
- Use fail2ban for repeated connection attempts
- Implement geo-blocking for unexpected regions
- Regular review of firewall rules

- **Mitre attack**: T1046 - Network Service Discovery
- **Severity**: medium
