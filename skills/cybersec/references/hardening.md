# System Hardening Guides

> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Windows Server Hardening

### Hardening steps

#### Account policies

- Set minimum password length to 14+ characters
- Enforce password complexity requirements
- Set maximum password age to 90 days
- Set account lockout threshold to 5 attempts
- Set account lockout duration to 30 minutes
- Enable password history (24 passwords remembered)
- Disable guest account
- Rename default administrator account

#### Audit policies

- Enable audit: Logon/Logoff - Success and Failure
- Enable audit: Account Management - Success and Failure
- Enable audit: Policy Change - Success and Failure
- Enable audit: Privilege Use - Success and Failure
- Enable audit: Process Tracking - Success
- Enable audit: System - Success and Failure
- Enable PowerShell logging (Module, ScriptBlock, Transcription)
- Enable command line process auditing

#### Security options

- Disable anonymous enumeration of shares
- Restrict anonymous access to named pipes
- Enable UAC (User Account Control)
- Disable remote registry service
- Disable unnecessary services
- Enable Windows Firewall
- Configure Windows Defender
- Enable Secure Boot

#### Network security

- Disable SMBv1
- Enable SMB signing
- Disable LLMNR
- Disable NetBIOS over TCP/IP
- Enable LDAPS for Active Directory
- Configure IPSec for sensitive communications
- Disable unnecessary network protocols
- Enable DNSSEC

#### Powershell security

- Set PowerShell execution policy to RemoteSigned
- Enable PowerShell logging (Module Logging)
- Enable PowerShell Script Block Logging
- Enable PowerShell Transcription
- Constrain PowerShell language mode for non-admins
- Remove PowerShell v2
- Implement AppLocker/WDAC rules
- Monitor PowerShell execution with Sysmon

### Verification commands

- **Check password policy**: net accounts
- **Check audit policy**: auditpol /get /category:*
- **Check smbv1**: Get-SmbServerConfiguration | Select EnableSMB1Protocol
- **Check firewall**: Get-NetFirewallProfile | Select Name, Enabled
- **Check defender**: Get-MpComputerStatus | Select AMServiceEnabled, RealTimeProtectionEnabled
- **Check services**: Get-Service | Where-Object {$_.StartType -eq 'Disabled'}

## Linux Server Hardening

### Hardening steps

#### Ssh hardening

- Disable root login (PermitRootLogin no)
- Use SSH key-based authentication only
- Disable password authentication (PasswordAuthentication no)
- Change default SSH port
- Implement fail2ban for SSH
- Use SSH protocol 2 only
- Set login grace time to 60 seconds
- Limit MaxAuthTries to 3

#### File permissions

- Set /etc/passwd to 644
- Set /etc/shadow to 640
- Set /etc/ssh/sshd_config to 600
- Set /boot/grub/grub.cfg to 600
- Disable SUID binaries where not needed
- Implement file integrity monitoring (AIDE)
- Configure umask to 027
- Set proper permissions on cron directories

#### Service hardening

- Disable unnecessary services
- Enable automatic security updates
- Configure firewall (iptables/nftables)
- Disable USB storage if not needed
- Enable audit logging (auditd)
- Configure log rotation
- Implement resource limits
- Enable SELinux/AppArmor

#### Network security

- Configure iptables/nftables firewall
- Disable IP forwarding if not needed
- Enable TCP SYN cookies
- Disable ICMP redirects
- Implement rate limiting
- Configure network segmentation
- Enable logging for dropped packets
- Implement fail2ban

#### User management

- Implement password aging policies
- Set minimum password length to 14
- Configure account lockout
- Remove unnecessary user accounts
- Implement sudo with logging
- Use PAM for authentication
- Configure session timeouts
- Implement centralized authentication (LDAP/AD)

### Verification commands

- **Check ssh config**: sshd -T | grep -E 'permitrootlogin|passwordauthentication|protocol'
- **Check firewall**: iptables -L -n -v
- **Check services**: systemctl list-unit-files --state=enabled
- **Check open ports**: ss -tlnp
- **Check failed logins**: lastb | head -20
- **Check suid files**: find / -perm -4000 -type f 2>/dev/null

## Web Application Hardening

### Hardening steps

#### Security headers

- Implement Content-Security-Policy (CSP)
- Set X-Content-Type-Options: nosniff
- Set X-Frame-Options: DENY or SAMEORIGIN
- Set X-XSS-Protection: 1; mode=block
- Set Strict-Transport-Security (HSTS)
- Set Referrer-Policy: strict-origin-when-cross-origin
- Set Permissions-Policy for camera, microphone, geolocation
- Remove server version headers

#### Authentication

- Implement multi-factor authentication (MFA)
- Enforce strong password policies
- Implement account lockout after failed attempts
- Use bcrypt/scrypt/Argon2 for password hashing
- Implement session management (timeout, regeneration)
- Use secure cookie flags (HttpOnly, Secure, SameSite)
- Implement CAPTCHA for login forms
- Monitor for credential stuffing attacks

#### Input validation

- Validate all user input on server side
- Implement parameterized queries for database
- Use output encoding for all dynamic content
- Implement file upload restrictions
- Validate Content-Type headers
- Implement request size limits
- Use allowlists instead of blocklists
- Implement CSRF tokens for all forms

#### Api security

- Implement API authentication (OAuth2, JWT)
- Use rate limiting on all endpoints
- Implement input validation for all parameters
- Use HTTPS for all API communications
- Implement API versioning
- Use CORS policies
- Implement request/response logging
- Use API gateway for centralized security

#### Error handling

- Implement custom error pages
- Do not expose stack traces in production
- Log errors securely (no sensitive data)
- Implement centralized error logging
- Use generic error messages for users
- Monitor error rates for anomalies
- Implement health check endpoints
- Use structured logging format

### Verification tools

- **Header check**: curl -I https://example.com
- **Ssl check**: testssl.sh https://example.com
- **Security scanner**: nikto -h https://example.com
- **Waf test**: sqlmap -u 'https://example.com/search?q=test'
- **Xss test**: xssstrike -u 'https://example.com/search?q=test'
- **Csrf test**: burpsuite -> CSRF PoC generator
