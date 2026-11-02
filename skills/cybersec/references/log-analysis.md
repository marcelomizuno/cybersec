# Log Analysis Guide

> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Windows Security Event Log Analysis

### Key events

#### Authentication

- **4624**: Successful logon - Monitor for unusual logon types (Type 3=Network, Type 10=RemoteInteractive)
- **4625**: Failed logon - Brute force detection, count by source IP
- **4634**: Logoff - Session duration analysis
- **4648**: Explicit credential logon - Pass-the-hash detection
- **4672**: Special privileges assigned - Admin logon detection
- **4771**: Kerberos pre-auth failed - Kerberoasting detection
- **4776**: NTLM authentication - NTLM relay detection

#### Account management

- **4720**: User account created - Unauthorized account detection
- **4722**: User account enabled - Dormant account activation
- **4724**: Password reset attempt - Account takeover detection
- **4728**: Member added to security group - Privilege escalation
- **4732**: Member added to local group - Local admin addition
- **4756**: Member added to universal group - Domain admin escalation

#### Policy changes

- **4719**: Audit policy changed - Defense evasion detection
- **4739**: Domain policy changed - Security policy modification
- **4946**: Firewall rule changed - Network security modification

#### Process execution

- **4688**: Process created - Suspicious process detection
- **4689**: Process exited - Process lifetime analysis

### Analysis queries

- **Brute force detection**: index=windows EventCode=4625 | stats count by IpAddress, TargetUserName | where count > 10 | sort -count
- **Admin logon tracking**: index=windows EventCode=4672 | stats count by SubjectUserName, ComputerName | sort -count
- **New account detection**: index=windows EventCode=4720 | table _time, ComputerName, SubjectUserName, TargetUserName
- **Privilege escalation**: index=windows (EventCode=4728 OR EventCode=4732 OR EventCode=4756) | table _time, ComputerName, MemberName, GroupName
- **Policy change detection**: index=windows (EventCode=4719 OR EventCode=4739) | table _time, ComputerName, SubjectUserName

## Linux Authentication Log Analysis

### Key events

#### Authentication

- **Accepted publickey**: Successful SSH key authentication - Monitor source IPs
- **Accepted password**: Successful password authentication - Should be minimal
- **Failed password**: Failed password attempt - Brute force detection
- **Invalid user**: Invalid username attempt - Username enumeration
- **Session opened**: User session started - Login tracking
- **Session closed**: User session ended - Session duration

#### Sudo activity

- **Command**: Sudo command execution - Privileged command tracking
- **Authentication failure**: Sudo auth failure - Unauthorized escalation
- **User start**: Sudo session started - Privilege use
- **User end**: Sudo session ended - Privilege use duration

### Analysis commands

- **Failed logins**: grep 'Failed password' /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn | head -20
- **Successful logins**: grep 'Accepted' /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn
- **Sudo commands**: grep 'COMMAND' /var/log/auth.log | awk -F'COMMAND=' '{print $2}' | sort | uniq -c | sort -rn
- **Invalid users**: grep 'Invalid user' /var/log/auth.log | awk '{print $8}' | sort | uniq -c | sort -rn
- **Root logins**: grep 'Accepted.*root' /var/log/auth.log
- **Login timeline**: grep -E '(Accepted|Failed)' /var/log/auth.log | awk '{print $1,$2,$3}' | uniq -c

## Web Server Log Analysis

### Key events

#### Access patterns

- **200**: Successful request - Normal operation
- **301/302**: Redirect - May indicate path enumeration
- **400**: Bad request - Malformed input detection
- **401**: Unauthorized - Authentication failure
- **403**: Forbidden - Access attempt to restricted resource
- **404**: Not found - Directory/file enumeration
- **500**: Server error - Potential vulnerability exploitation

#### Attack indicators

- **Sqli**: Look for: union, select, insert, update, delete, drop, --, '
- **Xss**: Look for: <script, onerror, onload, javascript:
- **Command injection**: Look for: ;, |, &, `, $, whoami, cat, ls
- **Path traversal**: Look for: ../, ..\, %2e%2e
- **Scanner**: Look for: nikto, sqlmap, nmap, burp in User-Agent

### Analysis commands

- **Top ips**: awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -20
- **Error 404**: awk '$9 == 404 {print $7}' access.log | sort | uniq -c | sort -rn | head -20
- **Sql injection**: grep -iE '(union|select|insert|update|delete|drop|--|)' access.log
- **Xss attempts**: grep -iE '(<script|onerror|onload|javascript:)' access.log
- **Scanner detection**: grep -iE '(nikto|sqlmap|nmap|burp)' access.log
- **Large responses**: awk '$10 > 1000000 {print $1,$7,$10}' access.log | sort -k3 -rn

## Firewall Log Analysis

### Key events

#### Connection events

- **Allow**: Permitted connection - Baseline for normal traffic
- **Deny**: Blocked connection - May indicate attack or misconfiguration
- **Drop**: Silently dropped - Stealth blocking

#### Attack indicators

- **Port scan**: Multiple connection attempts to different ports from same IP
- **Brute force**: Repeated connections to same port (22, 3389, 80, 443)
- **Ddos**: High volume connections from multiple IPs to same target
- **Data exfiltration**: Large outbound data transfers to unusual destinations
- **C2 communication**: Regular beaconing patterns to external IPs

### Analysis commands

- **Blocked ips**: grep 'DENY' firewall.log | awk '{print $3}' | sort | uniq -c | sort -rn | head -20
- **Top blocked ports**: grep 'DENY' firewall.log | awk '{print $5}' | sort | uniq -c | sort -rn | head -20
- **Port scan detection**: grep 'DENY' firewall.log | awk '{print $3}' | sort | uniq -c | awk '$1 > 50' | sort -rn
- **Large transfers**: awk '$NF > 1000000 {print $0}' firewall.log
- **Beaconing detection**: grep 'ALLOW' firewall.log | awk '{print $3,$5}' | sort | uniq -c | sort -rn | head -20
