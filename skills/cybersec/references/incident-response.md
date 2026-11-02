# Incident Response Playbooks

> Source: huggingface.co/datasets/Vyber07/cyber-security (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Ransomware Incident Response

### Detection signs

- Mass file encryption with new extensions (.encrypted, .locked, .crypto)
- Ransom note files (README_DECRYPT.txt, HOW_TO_DECRYPT.html)
- High CPU/disk usage on multiple systems
- Shadow copy deletion (vssadmin delete shadows)
- Windows Defender disabled
- Network shares becoming inaccessible

### Immediate actions

- ISOLATE infected systems from network immediately (do NOT power off)
- Disable network connections (unplug cables, disable WiFi)
- Preserve evidence (memory dumps, disk images)
- Notify incident response team and management
- Identify ransomware variant (ID Ransomware, No More Ransom)
- Check if decryption tools exist for the variant
- Do NOT pay ransom without management and legal approval

### Investigation steps

- Collect memory dumps from affected systems (WinPmem)
- Image affected disks for forensic analysis
- Review Windows Event Logs for suspicious activity
- Check for lateral movement (PsExec, WMI, RDP)
- Identify initial infection vector (phishing email, RDP, exploit)
- Map the attack timeline using log analysis
- Check for data exfiltration indicators
- Identify all affected systems and data

### Containment steps

- Block attacker C2 domains and IPs at firewall
- Disable compromised accounts
- Implement network segmentation
- Block SMB ports between workstations
- Disable unnecessary services
- Reset passwords for all potentially compromised accounts

### Eradication steps

- Remove malware from all affected systems
- Patch vulnerabilities exploited in attack
- Remove persistence mechanisms
- Rebuild systems from clean backups
- Verify backup integrity before restoration
- Rotate all credentials (especially admin)

### Recovery steps

- Restore data from verified clean backups
- Rebuild affected systems from known-good images
- Implement additional security controls
- Monitor for reinfection
- Conduct post-incident review
- Update incident response plan based on lessons learned

### Log sources

- Windows Event Logs (Security, System, PowerShell, Sysmon)
- Firewall logs (blocked connections, C2 traffic)
- Email gateway logs (phishing attachments)
- EDR logs (process creation, file modification)
- Network traffic captures (PCAP)
- Active Directory logs (authentication events)

### Detection queries

- **Splunk**: index=windows EventCode=4663 | bucket _time span=1m | stats dc(ObjectName) as files by ComputerName | where files > 100

**Sigma**

```yaml
title: Mass File Encryption
detection:
  selection:
    EventID: 4663
  condition: selection | count by ObjectName > 100
```

## Phishing Incident Response

### Detection signs

- User reports suspicious email
- Email gateway flags malicious attachment or URL
- Credential harvesting page detected
- Unusual login activity after email receipt
- Malware execution from email attachment
- Multiple users reporting same email

### Immediate actions

- Identify all recipients of the phishing email
- Delete email from all mailboxes (O365: New-ComplianceSearch)
- Block sender domain and IP at email gateway
- Block malicious URLs at web proxy
- Reset passwords for users who clicked links
- Scan endpoints of users who opened attachments

### Investigation steps

- Analyze email headers for true sender
- Sandbox suspicious attachments
- Check for credential harvesting (fake login pages)
- Review authentication logs for compromised accounts
- Check for lateral movement from compromised accounts
- Identify scope of data exposure
- Check for forwarded emails or rules created

### Containment steps

- Block sender at email gateway
- Quarantine similar emails
- Block malicious URLs and domains
- Disable compromised accounts temporarily
- Force password reset for affected users
- Revoke OAuth tokens if applicable

### Eradication steps

- Remove malware from affected endpoints
- Remove malicious email rules
- Block all identified IOCs
- Update email security rules
- Conduct user awareness training

### Recovery steps

- Restore any encrypted or deleted data
- Verify no persistence mechanisms
- Monitor for follow-up attacks
- Update phishing simulation campaigns
- Document lessons learned

### Log sources

- Email gateway logs (Proofpoint, Mimecast, O365)
- Web proxy logs (URL access)
- Authentication logs (Azure AD, Active Directory)
- Endpoint detection logs (EDR)
- DNS logs (domain resolution)

### Detection queries

- **Splunk**: index=email (subject=*urgent* OR subject=*password* OR subject=*account*) AND (attachment=*exe* OR attachment=*docm*) | stats count by sender, subject

**Sigma**

```yaml
title: Phishing Email Detection
detection:
  selection:
    EventID: 25
    Subject|contains:
      - 'urgent'
      - 'password'
      - 'account suspended'
  condition: selection
```

## Data Breach Incident Response

### Detection signs

- Unusual database query patterns
- Large data exfiltration detected
- Unauthorized access to sensitive data
- DLP alerts triggered
- Dark web monitoring flags exposed data
- Third party notification of exposed data

### Immediate actions

- Identify what data was accessed or exfiltrated
- Preserve all relevant logs and evidence
- Notify legal counsel and privacy officer
- Contain the breach (disable accounts, block IPs)
- Determine regulatory notification requirements
- Engage external forensics if needed

### Investigation steps

- Identify attack vector and timeline
- Determine scope of data accessed
- Review database audit logs
- Analyze network traffic for exfiltration
- Check for unauthorized account creation
- Review access control configurations
- Identify all affected data subjects

### Containment steps

- Disable compromised accounts
- Block attacker IP addresses
- Implement additional access controls
- Monitor for continued unauthorized access
- Rotate database credentials
- Review and tighten firewall rules

### Eradication steps

- Remove attacker access and persistence
- Patch exploited vulnerabilities
- Implement additional security controls
- Review and update access control policies
- Deploy additional monitoring

### Recovery steps

- Implement enhanced monitoring
- Conduct security awareness training
- Review and update security policies
- Prepare regulatory notifications
- Offer credit monitoring to affected individuals

### Log sources

- Database audit logs
- Network traffic logs
- Authentication logs
- DLP logs
- Web application logs
- Cloud service logs

### Detection queries

- **Splunk**: index=database (action=SELECT OR action=DUMP) | stats count by user, database, table | where count > 1000

**Sigma**

```yaml
title: Data Exfiltration
detection:
  selection:
    EventID: 5145
    AccessMask: '0x2'
  condition: selection | count by ObjectName > 100
```

## How to set up a Security Operations Center (SOC)?

#### SOC Setup Guide

##### Infrastructure Components
```
1. SIEM (Security Information and Event Management)
   - Splunk, Elastic SIEM, IBM QRadar
   - Log collection and correlation
   - Alert management

2. EDR (Endpoint Detection and Response)
   - CrowdStrike, Carbon Black, SentinelOne
   - Endpoint monitoring
   - Threat detection

3. NDR (Network Detection and Response)
   - Darktrace, Vectra, Cisco Stealthwatch
   - Network traffic analysis
   - Anomaly detection

4. SOAR (Security Orchestration, Automation, and Response)
   - Phantom, Demisto, Swimlane
   - Playbook automation
   - Incident response
```

##### Log Sources
```
- Firewall logs
- IDS/IPS logs
- Windows Event Logs
- Linux syslog
- Web server logs
- Database logs
- Application logs
- Cloud service logs
```

##### Detection Rules
```yaml
# Example: Brute Force Detection
rule:
  name: Brute Force Login
  condition:
    event.type: "authentication"
    event.outcome: "failure"
  threshold:
    count: 5
    time_window: 5m
  severity: high

# Example: Lateral Movement
rule:
  name: Lateral Movement
  condition:
    event.type: "authentication"
    source.ip: "10.0.0.0/8"
    destination.ip: "10.0.0.0/8"
  threshold:
    count: 10
    time_window: 10m
  severity: critical
```

##### Incident Response Playbooks
```
1. Phishing Response
   - Isolate affected mailbox
   - Block malicious URLs
   - Notify affected users
   - Scan endpoints

2. Malware Response
   - Isolate infected systems
   - Collect evidence
   - Remove malware
   - Restore from backup

3. Data Breach Response
   - Contain breach
   - Assess impact
   - Notify stakeholders
   - Remediate vulnerabilities
```

##### Metrics and KPIs
```
- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- False positive rate
- Alert volume
- Incident closure rate
```

##### Tools
- Splunk
- Elastic Stack
- CrowdStrike
- Darktrace
- Phantom
- TheHive
