# Containers, Kubernetes, DevSecOps and Supply Chain

> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Contents

- How to perform security assessment of Docker containers?
- How to perform Kubernetes security assessment?
- How to implement DevSecOps in a CI/CD pipeline?
- How to assess supply chain security for software dependencies?

## How to perform security assessment of Docker containers?

#### Docker Security Assessment

##### Image Security
```bash
# Scan image for vulnerabilities
trivy image nginx:latest
grype nginx:latest

# Check image history
docker history nginx:latest

# Analyze image layers
dive nginx:latest

# Check for secrets in image
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy image nginx:latest
```

##### Container Configuration
```bash
# Check running containers
docker ps --format "{{.ID}} {{.Image}} {{.Command}}"

# Inspect container
docker inspect <container_id>

# Check for privileged containers
docker ps --filter "label=com.docker.compose.project" --format "{{.ID}}" | \
    xargs -I {} docker inspect {} --format '{{.HostConfig.Privileged}}'

# Check for root containers
docker ps --format "{{.ID}}" | \
    xargs -I {} docker inspect {} --format '{{.Config.User}}'
```

##### Network Security
```bash
# Check network configuration
docker network ls
docker network inspect <network>

# Check exposed ports
docker port <container_id>

# Check for host network mode
docker inspect <container_id> --format '{{.HostConfig.NetworkMode}}'
```

##### Runtime Security
```bash
# Check capabilities
docker inspect <container_id> --format '{{.HostConfig.CapAdd}}'

# Check resource limits
docker inspect <container_id> --format '{{.HostConfig.Memory}}'
docker inspect <container_id> --format '{{.HostConfig.CpuShares}}'

# Check read-only filesystem
docker inspect <container_id> --format '{{.HostConfig.ReadonlyRootfs}}'
```

##### Docker Bench Security
```bash
# Run Docker Bench for Security
docker run --rm --net host --pid host --userns host --cap-add audit_control \
    -v /etc:/etc:ro \
    -v /var/lib:/var/lib:ro \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    docker/docker-bench-security
```

##### Best Practices
- Use minimal base images
- Don't run as root
- Use read-only filesystems
- Limit resources
- Scan images regularly
- Use secrets management
- Enable logging
- Use network policies

##### Tools
- Trivy
- Grype
- Dive
- Docker Bench
- Clair
- Anchore

## How to perform Kubernetes security assessment?

#### Kubernetes Security Assessment

##### Cluster Enumeration
```bash
# Get cluster info
kubectl cluster-info
kubectl get nodes
kubectl get namespaces

# List all resources
kubectl get all --all-namespaces

# Check RBAC
kubectl get clusterroles
kubectl get clusterrolebindings
kubectl get roles --all-namespaces
kubectl get rolebindings --all-namespaces
```

##### Pod Security
```bash
# Check pod security contexts
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.securityContext}{"\n"}{end}'

# Check for privileged pods
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.containers[*].securityContext.privileged}{"\n"}{end}'

# Check for host network
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.hostNetwork}{"\n"}{end}'

# Check for host PID
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.hostPID}{"\n"}{end}'
```

##### Secret Management
```bash
# List secrets
kubectl get secrets --all-namespaces

# Check for exposed secrets
kubectl get secrets -o yaml

# Check environment variables
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.containers[*].env[*].name}{"\n"}{end}'
```

##### Network Policies
```bash
# Check network policies
kubectl get networkpolicies --all-namespaces

# Check ingress/egress rules
kubectl get networkpolicies -o yaml

# Test network connectivity
kubectl run -it --rm debug --image=busybox --restart=Never -- wget -qO- http://service-name
```

##### RBAC Assessment
```bash
# Check for overly permissive roles
kubectl get clusterroles -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.rules[*].resources}{"\n"}{end}'

# Check for cluster-admin bindings
kubectl get clusterrolebindings -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.roleRef.name}{"\t"}{.subjects[*].name}{"\n"}{end}'

# Test permissions
kubectl auth can-i --list
kubectl auth can-i create pods --as=system:serviceaccount:default:mysa
```

##### Tools
- kube-bench
- kube-hunter
- kubeaudit
- kubesec
- Polaris
- Falco

## How to implement DevSecOps in a CI/CD pipeline?

#### DevSecOps Implementation Guide

##### Pipeline Security Stages
```yaml
# GitHub Actions Example
name: Security Pipeline
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      # SAST - Static Application Security Testing
      - name: CodeQL Analysis
        uses: github/codeql-action/analyze@v2
      
      # SCA - Software Composition Analysis
      - name: Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
      
      # Secrets Detection
      - name: TruffleHog
        uses: trufflesecurity/trufflehog@main
      
      # Container Scanning
      - name: Trivy
        uses: aquasecurity/trivy-action@master
      
      # DAST - Dynamic Application Security Testing
      - name: OWASP ZAP
        uses: zaproxy/action-baseline@v0.7.0
      
      # IaC Scanning
      - name: Checkov
        uses: bridgecrewio/checkov-action@v12
```

##### SAST Tools
```bash
# SonarQube
sonar-scanner -Dsonar.projectKey=my-project

# Semgrep
semgrep --config=p/security-audit .

# Bandit (Python)
bandit -r .

# ESLint Security
eslint --ext .js,.jsx,.ts,.tsx .
```

##### Secrets Detection
```bash
# TruffleHog
trufflehog filesystem .

# GitLeaks
gitleaks detect

# detect-secrets
detect-secrets scan
```

##### Container Security
```bash
# Dockerfile linting
hadolint Dockerfile

# Image scanning
trivy image myapp:latest

# Runtime security
falco
```

##### Infrastructure as Code
```bash
# Terraform scanning
terraform plan
terraform validate
checkov -d .

# Kubernetes scanning
kube-score score *.yaml
polaris audit --audit-path .
```

##### Best Practices
```
1. Shift left - integrate security early
2. Automate security testing
3. Fail fast on critical vulnerabilities
4. Security gates in pipeline
5. Regular security training
6. Security champions program
```

##### Tools
- SonarQube
- Semgrep
- Trivy
- Checkov
- OWASP ZAP
- GitLeaks

## How to assess supply chain security for software dependencies?

#### Supply Chain Security Assessment

##### Dependency Scanning
```bash
# npm (Node.js)
npm audit
npm audit fix

# pip (Python)
pip-audit
safety check

# Maven (Java)
own dependency:check

# Go
govulncheck ./...

# .NET
dotnet list package --vulnerable
```

##### SCA Tools
```bash
# Snyk
snyk test
snyk monitor

# OWASP Dependency-Check
dependency-check --project "My Project" --scan ./

# Trivy
trivy fs --security-checks vuln .

# Grype
grype dir:.
```

##### CI/CD Pipeline Security
```yaml
# GitHub Actions Security
- name: Security Scan
  uses: github/codeql-action/analyze@v2

# GitLab CI Security
sast:
  stage: test
  image: registry.gitlab.com/security-products/sast

# Jenkins Security
pipeline {
    stages {
        stage('Security') {
            steps {
                sh 'snyk test'
            }
        }
    }
}
```

##### Package Verification
```bash
# Verify package integrity
npm audit signatures
pip hash <package>

# Check for typosquatting
# Verify package names
# Check download counts
# Review package source
```

##### Best Practices
```
1. Pin dependency versions
2. Use lock files
3. Regular dependency updates
4. Vulnerability scanning in CI/CD
5. Private package registries
6. Code review for dependencies
7. SBOM (Software Bill of Materials)
```

##### Tools
- Snyk
- OWASP Dependency-Check
- Trivy
- Grype
- Dependabot
- Renovate
