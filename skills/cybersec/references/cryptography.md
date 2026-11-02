# Cryptography and PKI

> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). Community-curated reference; verify commands and versions before use.

## Provide a comprehensive guide to cryptography, including algorithms, attacks, and best practices.

#### Comprehensive Cryptography Guide

##### Cryptographic Algorithms

###### 1. Symmetric Encryption

**AES (Advanced Encryption Standard):**
- Block size: 128 bits
- Key sizes: 128, 192, 256 bits
- Modes: ECB, CBC, CTR, GCM
- Security: Secure when used correctly

**ChaCha20:**
- Stream cipher
- Key size: 256 bits
- Nonce: 96 bits
- Security: Secure, fast in software

**3DES (Triple DES):**
- Block size: 64 bits
- Key size: 168 bits (effective 112)
- Security: Deprecated, slow

**Blowfish/Twofish:**
- Block size: 64/128 bits
- Key size: Up to 448/256 bits
- Security: Blowfish deprecated, Twofish secure

###### 2. Asymmetric Encryption

**RSA:**
- Key sizes: 2048, 3072, 4096 bits
- Security: Secure with proper padding
- Use: Key exchange, digital signatures

**ECC (Elliptic Curve Cryptography):**
- Curves: P-256, P-384, P-521, Curve25519
- Security: Equivalent security with smaller keys
- Use: Key exchange, digital signatures

**DSA/ECDSA:**
- Digital signature algorithm
- Security: Secure with proper implementation
- Use: Digital signatures

**EdDSA (Ed25519):**
- Digital signature algorithm
- Security: Secure, fast
- Use: Digital signatures

###### 3. Hash Functions

**SHA-2 Family:**
- SHA-224, SHA-256, SHA-384, SHA-512
- Security: Secure
- Use: Data integrity, digital signatures

**SHA-3:**
- Keccak-based
- Security: Secure
- Use: Data integrity, digital signatures

**BLAKE2/BLAKE3:**
- Fast hash functions
- Security: Secure
- Use: Data integrity, passwords

**MD5/SHA-1:**
- Security: Broken, deprecated
- Use: Legacy systems only

###### 4. Key Derivation Functions

**PBKDF2:**
- Password-based key derivation
- Iterations: 100,000+
- Security: Secure with sufficient iterations

**bcrypt:**
- Password hashing
- Cost factor: 10+
- Security: Secure

**Argon2:**
- Password hashing
- Memory-hard
- Security: Secure, recommended

**scrypt:**
- Password hashing
- Memory-hard
- Security: Secure

##### Cryptographic Attacks

###### 1. Brute Force Attacks

**Description:**
- Try all possible keys
- Time-consuming
- Ineffective against strong keys

**Mitigation:**
- Use strong keys
- Key size >= 128 bits
- Rate limiting
- Account lockout

###### 2. Dictionary Attacks

**Description:**
- Try common passwords
- Wordlist-based
- Faster than brute force

**Mitigation:**
- Strong passwords
- Password policies
- Key derivation functions
- Account lockout

###### 3. Rainbow Table Attacks

**Description:**
- Precomputed hash tables
- Fast lookup
- Trade space for time

**Mitigation:**
- Salting
- Key derivation functions
- Unique salts per password
- Strong algorithms

###### 4. Side-Channel Attacks

**Description:**
- Exploit implementation flaws
- Timing attacks
- Power analysis
- Electromagnetic analysis

**Mitigation:**
- Constant-time algorithms
- Secure implementations
- Hardware protections
- Regular updates

###### 5. Padding Oracle Attacks

**Description:**
- Exploit padding validation
- CBC mode vulnerability
- Decrypt without key

**Mitigation:**
- Use authenticated encryption
- GCM mode
- Proper error handling
- Constant-time comparison

###### 6. Key Reuse Attacks

**Description:**
- Reuse keys/nonces
- Break encryption
- Recover plaintext

**Mitigation:**
- Unique keys/nonces
- Key rotation
- Proper key management
- Random generation

##### Key Management

###### 1. Key Generation

**Best Practices:**
- Cryptographically secure random
- Sufficient key size
- Proper algorithm selection
- Regular rotation

**Tools:**
- OpenSSL
- GnuPG
- Key management systems
- Hardware security modules

###### 2. Key Storage

**Methods:**
- Hardware security modules
- Key management services
- Encrypted storage
- Secure enclaves

**Best Practices:**
- Access control
- Encryption at rest
- Regular backups
- Audit logging

###### 3. Key Rotation

**Process:**
- Generate new key
- Re-encrypt data
- Archive old key
- Update references

**Frequency:**
- Based on risk
- Regulatory requirements
- Key usage
- Time-based

###### 4. Key Destruction

**Process:**
- Secure deletion
- Overwriting
- Cryptographic erasure
- Documentation

**Best Practices:**
- Verify destruction
- Document process
- Audit trail
- Compliance

##### TLS/SSL

###### 1. TLS Versions

**TLS 1.0/1.1:**
- Security: Deprecated
- Use: None

**TLS 1.2:**
- Security: Secure with proper configuration
- Use: Widely supported

**TLS 1.3:**
- Security: Most secure
- Use: Recommended

###### 2. Cipher Suites

**Recommended:**
- TLS_AES_256_GCM_SHA384
- TLS_CHACHA20_POLY1305_SHA256
- TLS_AES_128_GCM_SHA256

**Avoid:**
- RC4
- DES/3DES
- MD5
- NULL ciphers

###### 3. Certificate Management

**Best Practices:**
- Use trusted CAs
- Regular renewal
- Proper key protection
- Certificate transparency

**Tools:**
- Let's Encrypt
- OpenSSL
- Certbot
- Certificate management platforms

##### Cryptographic Best Practices

###### 1. Algorithm Selection

**Symmetric:**
- AES-256-GCM
- ChaCha20-Poly1305

**Asymmetric:**
- RSA-2048+
- ECC P-256+
- Ed25519

**Hashing:**
- SHA-256+
- SHA-3
- BLAKE2

**Key Derivation:**
- Argon2
- bcrypt
- PBKDF2

###### 2. Implementation

**Do:**
- Use established libraries
- Follow standards
- Regular updates
- Security testing

**Don't:**
- Roll your own crypto
- Use deprecated algorithms
- Hardcode keys
- Ignore side channels

###### 3. Key Management

**Do:**
- Use HSMs
- Regular rotation
- Access control
- Audit logging

**Don't:**
- Store keys in code
- Share keys insecurely
- Reuse keys
- Ignore key lifecycle

##### Cryptographic Tools

###### 1. OpenSSL
```bash
# Generate RSA key
openssl genrsa -aes256 4096 > private.key

# Generate CSR
openssl req -new -key private.key -out request.csr

# Self-signed certificate
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

# Encrypt file
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc

# Decrypt file
openssl enc -aes-256-cbc -d -in file.enc -out file.txt
```

###### 2. GnuPG
```bash
# Generate key pair
gpg --gen-key

# Encrypt file
gpg -e -r recipient file.txt

# Decrypt file
gpg -d file.txt.gpg

# Sign file
gpg -s file.txt

# Verify signature
gpg --verify file.txt.sig
```

###### 3. Key Derivation
```python
# PBKDF2
import hashlib
import os

salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

# Argon2
from argon2 import PasswordHasher

ph = PasswordHasher()
hash = ph.hash(password)
```

##### Cryptographic Standards

###### 1. NIST Standards
- FIPS 197: AES
- FIPS 186-5: DSA
- FIPS 180-4: SHA
- SP 800-132: Key Derivation

###### 2. Industry Standards
- PCI DSS: Payment security
- HIPAA: Healthcare security
- GDPR: Data protection
- ISO 27001: Information security

###### 3. Protocol Standards
- TLS 1.3: Transport security
- IPsec: Network security
- S/MIME: Email security
- PGP: Email security

##### Cryptographic Challenges

###### 1. Quantum Computing

**Threats:**
- Shor's algorithm
- Breaks RSA/ECC
- Harvest now, decrypt later

**Mitigation:**
- Post-quantum cryptography
- Lattice-based algorithms
- Hash-based signatures
- Hybrid approaches

###### 2. Key Management

**Challenges:**
- Key distribution
- Key storage
- Key rotation
- Key recovery

**Solutions:**
- Key management systems
- Hardware security modules
- Automated processes
- Cloud services

###### 3. Implementation Security

**Challenges:**
- Side channels
- Random number generation
- Error handling
- Backward compatibility

**Solutions:**
- Secure libraries
- Regular updates
- Security testing
- Best practices

## How do I implement secure encryption in applications?

#### Secure Encryption Implementation Guide

##### 1. Data at Rest Encryption

###### 1.1 File Encryption

**Python Example:**
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def encrypt_file(password, input_file, output_file):
    # Generate salt
    salt = os.urandom(16)
    
    # Derive key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    # Encrypt file
    f = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    
    # Write salt and encrypted data
    with open(output_file, 'wb') as file:
        file.write(salt + encrypted_data)

def decrypt_file(password, input_file, output_file):
    # Read salt and encrypted data
    with open(input_file, 'rb') as file:
        salt = file.read(16)
        encrypted_data = file.read()
    
    # Derive key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    # Decrypt file
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
```

**Java Example:**
```java
import javax.crypto.Cipher;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;

public class FileEncryption {
    private static final int GCM_TAG_LENGTH = 128;
    private static final int GCM_IV_LENGTH = 12;
    
    public static byte[] encrypt(byte[] key, byte[] data) throws Exception {
        // Generate IV
        byte[] iv = new byte[GCM_IV_LENGTH];
        SecureRandom random = new SecureRandom();
        random.nextBytes(iv);
        
        // Initialize cipher
        SecretKeySpec keySpec = new SecretKeySpec(key, "AES");
        GCMParameterSpec gcmSpec = new GCMParameterSpec(GCM_TAG_LENGTH, iv);
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, gcmSpec);
        
        // Encrypt data
        byte[] encrypted = cipher.doFinal(data);
        
        // Combine IV and encrypted data
        byte[] result = new byte[iv.length + encrypted.length];
        System.arraycopy(iv, 0, result, 0, iv.length);
        System.arraycopy(encrypted, 0, result, iv.length, encrypted.length);
        
        return result;
    }
}
```

###### 1.2 Database Encryption

**Transparent Data Encryption (TDE):**
- Encrypts entire database
- No application changes
- Key management required

**Column-level Encryption:**
- Encrypt specific columns
- Application-level encryption
- More granular control

**Application-level Encryption:**
- Encrypt before storage
- Full control
- Key management required

##### 2. Data in Transit Encryption

###### 2.1 TLS Configuration

**Nginx Configuration:**
```nginx
server {
    listen 443 ssl http2;
    
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;
    
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:50m;
    ssl_session_tickets off;
    
    # HSTS
    add_header Strict-Transport-Security "max-age=63072000" always;
}
```

**Apache Configuration:**
```apache
<VirtualHost *:443>
    SSLEngine on
    SSLCertificateFile /etc/apache2/ssl/cert.pem
    SSLCertificateKeyFile /etc/apache2/ssl/key.pem
    
    SSLProtocol -all +TLSv1.2 +TLSv1.3
    SSLCipherSuite ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256
    SSLHonorCipherOrder off
    
    Header always set Strict-Transport-Security "max-age=63072000"
</VirtualHost>
```

###### 2.2 Certificate Management

**Let's Encrypt:**
```bash
# Install Certbot
apt install certbot python3-certbot-nginx

# Generate certificate
certbot certonly --nginx -d example.com

# Auto-renewal
certbot renew --dry-run
```

##### 3. Password Hashing

###### 3.1 Argon2

**Python Example:**
```python
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

def hash_password(password):
    ph = PasswordHasher(
        time_cost=3,
        memory_cost=65536,
        parallelism=4
    )
    return ph.hash(password)

def verify_password(hash, password):
    ph = PasswordHasher()
    try:
        return ph.verify(hash, password)
    except VerifyMismatchError:
        return False
```

**Java Example:**
```java
import de.mkammerer.argon2.Argon2;
import de.mkammerer.argon2.Argon2Factory;

public class PasswordHashing {
    private static final Argon2 argon2 = Argon2Factory.create();
    
    public static String hashPassword(char[] password) {
        return argon2.hash(10, 65536, 1, password);
    }
    
    public static boolean verifyPassword(String hash, char[] password) {
        return argon2.verify(hash, password);
    }
}
```

##### 4. Key Management

###### 4.1 Key Generation

**Python Example:**
```python
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_symmetric_key():
    return os.urandom(32)

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem, public_pem
```

###### 4.2 Key Storage

**AWS KMS Example:**
```python
import boto3

def encrypt_with_kms(key_id, plaintext):
    kms = boto3.client('kms')
    response = kms.encrypt(
        KeyId=key_id,
        Plaintext=plaintext
    )
    return response['CiphertextBlob']

def decrypt_with_kms(ciphertext):
    kms = boto3.client('kms')
    response = kms.decrypt(
        CiphertextBlob=ciphertext
    )
    return response['Plaintext']
```

##### 5. Secure Random Number Generation

**Python Example:**
```python
import os
import secrets

# Generate random bytes
random_bytes = os.urandom(32)

# Generate random string
random_string = secrets.token_hex(32)

# Generate random URL-safe string
random_url = secrets.token_urlsafe(32)

# Generate random integer
random_int = secrets.randbelow(1000000)
```

##### 6. Digital Signatures

**Python Example:**
```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

def sign_data(private_key, data):
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, data, signature):
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False
```

##### 7. Best Practices

###### 7.1 Algorithm Selection

**Do Use:**
- AES-256-GCM for symmetric encryption
- RSA-2048+ or ECC P-256+ for asymmetric
- SHA-256+ for hashing
- Argon2 for password hashing

**Don't Use:**
- DES/3DES
- RC4
- MD5/SHA-1
- ECB mode

###### 7.2 Key Management

**Do:**
- Use HSMs or KMS
- Rotate keys regularly
- Use strong key sizes
- Protect key material

**Don't:**
- Hardcode keys
- Share keys insecurely
- Reuse keys/IVs
- Use weak keys

###### 7.3 Implementation

**Do:**
- Use established libraries
- Follow standards
- Test thoroughly
- Update regularly

**Don't:**
- Roll your own crypto
- Use deprecated algorithms
- Ignore side channels
- Skip validation

##### 8. Security Testing

###### 8.1 Static Analysis
- Code review
- Dependency scanning
- Configuration review
- Key management review

###### 8.2 Dynamic Analysis
- Penetration testing
- Vulnerability scanning
- Configuration testing
- Performance testing

###### 8.3 Compliance Testing
- Regulatory requirements
- Industry standards
- Internal policies
- Best practices

## How to implement secure encryption for data at rest?

#### Secure Encryption Implementation

##### AES-256-GCM (Recommended)
```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt_data(key, plaintext, associated_data=None):
    """Encrypt data with AES-256-GCM"""
    nonce = os.urandom(12)  # 96-bit nonce
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), associated_data)
    return nonce + ciphertext

def decrypt_data(key, ciphertext, associated_data=None):
    """Decrypt data with AES-256-GCM"""
    nonce = ciphertext[:12]
    ciphertext = ciphertext[12:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, associated_data).decode()

# Generate key
key = AESGCM.generate_key(bit_length=256)
```

##### Key Management
```python
# Key derivation from password
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
    )
    return kdf.derive(password.encode())
```

##### Best Practices
- Use authenticated encryption (GCM, CCM)
- Never reuse nonces/IVs
- Use proper key derivation (PBKDF2, Argon2)
- Store keys separately from data
- Rotate keys regularly
- Use hardware security modules (HSM) for production

##### Common Mistakes
- Using ECB mode
- Hardcoded keys
- Weak key derivation
- Nonce reuse
- Missing integrity checks

##### Libraries
- Python: cryptography, PyCryptodome
- Node.js: crypto
- Java: JCA/JCE
- Go: crypto/aes

## How to analyze and test TLS/SSL configurations?

#### TLS/SSL Security Assessment

##### Testing with testssl.sh
```bash
# Full scan
testssl.sh https://example.com

# Specific tests
testssl.sh --protocols https://example.com
testssl.sh --ciphers https://example.com
testssl.sh --vulnerabilities https://example.com
```

##### Testing with SSLyze
```bash
# Full scan
sslyze --regular example.com

# Specific tests
sslyze --certinfo example.com
sslyze --heartbleed example.com
sslyze --openssl_ccs example.com
```

##### Testing with Nmap
```bash
# SSL enumeration
nmap --script ssl-enum-ciphers -p 443 example.com

# SSL vulnerabilities
nmap --script ssl-heartbleed -p 443 example.com
nmap --script ssl-poodle -p 443 example.com
```

##### Common Vulnerabilities

###### 1. Weak Cipher Suites
```
# Bad
RC4, DES, 3DES, NULL, EXPORT

# Good
AES-256-GCM, AES-128-GCM, ChaCha20
```

###### 2. Protocol Versions
```
# Bad
SSLv2, SSLv3, TLSv1.0, TLSv1.1

# Good
TLSv1.2, TLSv1.3
```

###### 3. Certificate Issues
```
# Check
- Expiration date
- Chain of trust
- Key strength (min 2048-bit RSA)
- Subject Alternative Names
- Revocation status
```

###### 4. Known Vulnerabilities
```
- Heartbleed (CVE-2014-0160)
- POODLE (CVE-2014-3566)
- BEAST (CVE-2011-3389)
- CRIME (CVE-2012-4929)
- BREACH (CVE-2013-3587)
- ROBOT (CVE-2017-13099)
```

##### Best Practices
- Use TLSv1.3 (or TLSv1.2 minimum)
- Strong cipher suites only
- Perfect Forward Secrecy (PFS)
- HSTS enabled
- Certificate transparency
- OCSP stapling

##### Tools
- testssl.sh
- SSLyze
- Nmap
- Qualys SSL Labs
- ssllabs-scan
