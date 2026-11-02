# Compliance (GDPR / HIPAA / PCI-DSS)

> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). Community-curated reference; verify commands and versions before use.

## How to assess GDPR compliance for a web application?

#### GDPR Compliance Assessment

##### Data Processing Inventory
```
1. Identify personal data collected
   - Name, email, phone
   - IP addresses
   - Cookies
   - Payment information
   - Location data

2. Document processing activities
   - Purpose of processing
   - Legal basis
   - Data retention period
   - Third-party sharing
```

##### Technical Measures
```bash
# Data Protection by Design
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.2+)
- Pseudonymization
- Access controls

# Data Subject Rights
- Right to access (data export)
- Right to erasure (data deletion)
- Right to rectification (data update)
- Right to portability (data transfer)
```

##### Privacy Controls
```html
<!-- Cookie Consent -->
<div id="cookie-consent">
    <p>We use cookies to improve your experience.</p>
    <button onclick="acceptAll()">Accept All</button>
    <button onclick="rejectAll()">Reject All</button>
    <button onclick="customize()">Customize</button>
</div>

<!-- Privacy Policy -->
<!-- Must include: -->
- Data controller information
- Processing purposes
- Legal basis
- Data retention
- Data subject rights
- Contact information
```

##### Security Measures
```
- Access controls (RBAC)
- Audit logging
- Data backup
- Incident response plan
- Data protection impact assessment
- Regular security testing
```

##### Documentation Required
```
- Data Processing Agreement (DPA)
- Privacy Impact Assessment (PIA)
- Record of Processing Activities (ROPA)
- Data breach notification procedures
- Consent management records
```

##### Tools
- OneTrust
- TrustArc
- Cookiebot
- PrivacyBadger

## How to assess HIPAA compliance for a healthcare application?

#### HIPAA Compliance Assessment

##### Protected Health Information (PHI)
```
1. Identify PHI collected
   - Patient names
   - Social Security numbers
   - Medical records
   - Insurance information
   - Contact information

2. PHI storage locations
   - Databases
   - File systems
   - Backups
   - Logs
```

##### Technical Safeguards
```bash
# Access Control
- Unique user identification
- Emergency access procedure
- Automatic logoff
- Encryption and decryption

# Audit Controls
- Activity logs
- Access logs
- Modification logs
- Audit trail review

# Integrity Controls
- Data validation
- Checksum verification
- Backup verification

# Transmission Security
- TLS 1.2+ for data in transit
- VPN for remote access
- Secure file transfer
```

##### Physical Safeguards
```
- Facility access controls
- Workstation security
- Device and media controls
- Disposal procedures
```

##### Administrative Safeguards
```
- Security management process
- Assigned security responsibility
- Workforce security
- Information access management
- Security awareness training
- Security incident procedures
- Contingency plan
- Business associate contracts
```

##### Documentation Required
```
- Security policies and procedures
- Risk assessment
- Business Associate Agreement (BAA)
- Incident response plan
- Training records
- Audit logs
```

##### Tools
- Vanta
- Drata
- Tugboat Logic
- HIPAA One
