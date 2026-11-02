# Threat Hunting Queries (Splunk / Sigma / KQL)

> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Contents

- Suspicious PowerShell Execution
- Lateral Movement Detection
- Persistence Mechanism Detection
- Credential Access Detection
- Defense Evasion Detection
- Exfiltration Detection

## Suspicious PowerShell Execution
- **Hypothesis**: Adversaries may use PowerShell for execution, lateral movement, and defense evasion.

### Hunt queries

- **Splunk**: index=windows EventCode=4104 (ScriptBlockText=*-enc* OR ScriptBlockText=*bypass* OR ScriptBlockText=*downloadstring* OR ScriptBlockText=*invoke-expression* OR ScriptBlockText=*IEX*) | stats count by ComputerName, ScriptBlockText, UserName

**Sigma**

```yaml
title: Suspicious PowerShell
detection:
  selection:
    EventID: 4104
    ScriptBlockText|contains:
      - '-enc'
      - 'bypass'
      - 'downloadstring'
      - 'IEX'
      - 'invoke-expression'
  condition: selection
```

**Kusto**

```
DeviceProcessEvents
| where FileName == "powershell.exe"
| where ProcessCommandLine contains "-enc" or ProcessCommandLine contains "bypass"
| project Timestamp, DeviceName, ProcessCommandLine, AccountName
```

- **Elk**: event.code:"4104" AND (winlog.event_data.ScriptBlockText:*-enc* OR winlog.event_data.ScriptBlockText:*bypass*)

### What to look for

- Encoded PowerShell commands (-enc, -EncodedCommand)
- Execution policy bypass (-ep bypass, -ExecutionPolicy Bypass)
- Download cradles (DownloadString, DownloadFile, Net.WebClient)
- Invoke-Expression (IEX) usage
- Base64 encoded payloads
- PowerShell spawned by unusual parents (Word, Excel, Outlook)

- **Mitre attack**: T1059.001 - PowerShell

## Lateral Movement Detection
- **Hypothesis**: Adversaries may move laterally using stolen credentials and remote access tools.

### Hunt queries

- **Splunk**: index=windows EventCode=4624 LogonType=3 | stats count by TargetUserName, IpAddress, ComputerName | where count > 10

**Sigma**

```yaml
title: Lateral Movement
detection:
  selection:
    EventID: 4624
    LogonType: 3
  condition: selection | count by TargetUserName, IpAddress > 10
```

**Kusto**

```
SecurityEvent
| where EventID == 4624 and LogonType == 3
| summarize count() by TargetUserName, IpAddress, Computer
| where count_ > 10
```

- **Elk**: event.code:"4624" AND winlog.event_data.LogonType:"3" | groupby user.name, source.ip | having count > 10

### What to look for

- Network logons (Type 3) to multiple systems from single source
- PsExec service creation (Event ID 7045)
- WMI process creation (wmiprvse.exe spawning cmd.exe)
- RDP connections to servers from workstations
- SMB connections to admin shares (C$, ADMIN$)
- WinRM connections from unusual sources

- **Mitre attack**: T1021 - Remote Services

## Persistence Mechanism Detection
- **Hypothesis**: Adversaries may establish persistence through scheduled tasks, services, or registry modifications.

### Hunt queries

- **Splunk**: index=windows (EventCode=7045 OR EventCode=4698 OR EventID=13) | stats count by ComputerName, TaskName, ServiceName

**Sigma**

```yaml
title: Persistence Detection
detection:
  selection1:
    EventID: 7045
  selection2:
    EventID: 4698
  selection3:
    EventID: 13
    TargetObject|contains: 'Run'
  condition: selection1 or selection2 or selection3
```

**Kusto**

```
SecurityEvent
| where EventID in (7045, 4698, 13)
| project TimeGenerated, Computer, EventID, TaskName, ServiceName
```

- **Elk**: event.code:("7045" OR "4698" OR "13") | groupby host.name, event.code

### What to look for

- New service creation (Event ID 7045)
- Scheduled task creation (Event ID 4698)
- Registry Run key modifications (Event ID 13)
- Startup folder file creation
- WMI event subscriptions
- DLL side-loading in application directories

- **Mitre attack**: T1053 - Scheduled Task/Job

## Credential Access Detection
- **Hypothesis**: Adversaries may attempt to dump credentials from memory or crack password hashes.

### Hunt queries

- **Splunk**: index=sysmon EventCode=10 TargetImage=*lsass.exe | stats count by SourceImage, GrantedAccess | where GrantedAccess="0x1010" OR GrantedAccess="0x1038"

**Sigma**

```yaml
title: Credential Access
detection:
  selection:
    EventID: 10
    TargetImage|endswith: '\lsass.exe'
    GrantedAccess|contains: '0x10'
  condition: selection
```

**Kusto**

```
DeviceProcessEvents
| where ActionType == 'OpenProcessApiCall'
| where TargetProcessFileName == 'lsass.exe'
| project Timestamp, DeviceName, InitiatingProcessFileName, TargetProcessFileName
```

- **Elk**: event.code:"10" AND winlog.event_data.TargetImage:*lsass.exe

### What to look for

- LSASS process access (Event ID 10)
- Mimikatz execution indicators
- SAM database access attempts
- Kerberoasting activity (TGS requests)
- AS-REP roasting attempts
- DCSync replication requests

- **Mitre attack**: T1003 - OS Credential Dumping

## Defense Evasion Detection
- **Hypothesis**: Adversaries may attempt to disable security tools and clear event logs.

### Hunt queries

- **Splunk**: index=windows (EventCode=1100 OR EventCode=1102 OR (EventCode=4688 AND (CommandLine=*wevtutil* OR CommandLine=*Clear-EventLog*))) | stats count by ComputerName, CommandLine

**Sigma**

```yaml
title: Defense Evasion
detection:
  selection1:
    EventID: 1102
  selection2:
    EventID: 4688
    CommandLine|contains:
      - 'wevtutil'
      - 'Clear-EventLog'
      - 'Stop-Service WinDefend'
  condition: selection1 or selection2
```

**Kusto**

```
SecurityEvent
| where EventID in (1100, 1102) or (EventID == 4688 and CommandLine has_any ('wevtutil', 'Clear-EventLog'))
| project TimeGenerated, Computer, EventID, CommandLine
```

- **Elk**: event.code:("1100" OR "1102") OR (event.code:"4688" AND process.command_line:(*wevtutil* OR *Clear-EventLog*))

### What to look for

- Event log clearing (Event ID 1100, 1102)
- Windows Defender service stop
- AMSI bypass attempts
- ETW patching
- Process hollowing indicators
- Timestomping of files

- **Mitre attack**: T1070 - Indicator Removal

## Exfiltration Detection
- **Hypothesis**: Adversaries may exfiltrate data through DNS tunneling, HTTP/HTTPS, or cloud services.

### Hunt queries

- **Splunk**: index=network bytes_out > 10000000 | stats sum(bytes_out) as total_out by dest_ip, dest_port | where total_out > 100000000 | sort -total_out

**Sigma**

```yaml
title: Data Exfiltration
detection:
  selection:
    EventID: 5145
    AccessMask: '0x2'
  timeframe: 1h
  condition: selection | count by ObjectName > 500
```

**Kusto**

```
NetworkCommunicationEvents
| summarize TotalBytes = sum(BytesSent) by RemoteIp, RemotePort
| where TotalBytes > 100000000
| sort by TotalBytes desc
```

- **Elk**: destination.bytes > 10000000 | groupby destination.ip, destination.port | having sum(destination.bytes) > 100000000

### What to look for

- Large outbound data transfers (>100MB)
- DNS queries with long subdomains (tunneling)
- Data transfers to unusual destinations
- Cloud storage uploads (Mega, Dropbox, Google Drive)
- FTP transfers to external servers
- Unusual HTTPS traffic patterns

- **Mitre attack**: T1048 - Exfiltration Over Alternative Protocol
