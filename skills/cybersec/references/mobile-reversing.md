# Mobile Security and Reverse Engineering

> Source: huggingface.co/datasets/Vyber07/cyber-security (Apache-2.0). Community-curated reference; verify commands and versions before use.

## How to perform security testing on an Android application?

#### Android Application Security Testing

##### Phase 1: Static Analysis
```bash
# Decompile APK
apktool d app.apk -o decompiled/
jadx -d output/ app.apk

# Check AndroidManifest.xml
- Permissions (dangerous vs normal)
- Exported components
- Debuggable flag
- Backup allowed
- Network security config

# Search for hardcoded secrets
grep -r 'api_key\|password\|secret\|token' smali/
grep -r 'http://\|https://' smali/
```

##### Phase 2: Dynamic Analysis
```bash
# Install on emulator
adb install app.apk

# SSL Pinning Bypass (Frida)
frida -U -f com.app.package -l ssl-bypass.js --no-pause

# Root Detection Bypass
frida -U -f com.app.package -l root-bypass.js --no-pause

# Monitor HTTP traffic
mitmproxy -p 8080
```

##### Phase 3: Common Vulnerabilities

###### 1. Insecure Data Storage
```bash
# Check SharedPreferences
adb shell cat /data/data/<package>/shared_prefs/*.xml

# Check SQLite databases
adb shell sqlite3 /data/data/<package>/databases/*.db

# Check external storage
adb shell ls /sdcard/Android/data/<package>/
```

###### 2. Insecure Communication
```bash
# Check network security config
# Look for:
- cleartext traffic allowed
- Missing certificate pinning
- Custom trust managers
```

###### 3. Insecure Authentication
```bash
# Test biometric bypass
# Test session management
# Test token storage
```

###### 4. Code Injection
```bash
# Test WebView vulnerabilities
- JavaScript interface
- File access
- Intent scheme handling
```

##### Tools
- MobSF
- Frida
- Objection
- APKTool
- jadx
- mitmproxy
- Drozer

## How to analyze Android APK permissions and manifest?

#### Android Manifest Deep Analysis

##### Extract Manifest
```bash
# Using aapt2
aapt2 dump xmltree app.apk --file AndroidManifest.xml

# Using apktool
apktool d app.apk
cat app/AndroidManifest.xml
```

##### Permission Analysis
```xml
<!-- Dangerous Permissions -->
<uses-permission android:name="android.permission.READ_SMS"/>
<uses-permission android:name="android.permission.SEND_SMS"/>
<uses-permission android:name="android.permission.READ_CONTACTS"/>
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

##### Component Security
```xml
<!-- Exported Activities -->
<activity android:name=".LoginActivity" android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
    </intent-filter>
</activity>

<!-- Exported Services -->
<service android:name=".MyService" android:exported="true"/>

<!-- Exported Receivers -->
<receiver android:name=".MyReceiver" android:exported="true"/>

<!-- Exported Providers -->
<provider android:name=".MyProvider" android:exported="true"/>
```

##### Security Flags
```xml
<!-- Debuggable -->
<application android:debuggable="true">  <!-- RISK! -->

<!-- Backup Allowed -->
<application android:allowBackup="true">  <!-- RISK! -->

<!-- Network Security Config -->
<application android:networkSecurityConfig="@xml/network_security_config">
```

##### Risk Scoring
```python
risk_factors = {
    'debuggable': 10,
    'allowBackup': 7,
    'exported_components': 5,
    'dangerous_permissions': 3,
    'cleartext_traffic': 8,
    'custom_permissions': 4
}

total_risk = sum(risk_factors[f] for f in found_issues)
```

##### Tools
- aapt/aapt2
- APKTool
- APK Analyzer
- MobSF
- AndroBugs

## How to perform iOS application security testing?

#### iOS Application Security Testing

##### Prerequisites
- Jailbroken device
- Frida installed
- Burp Suite configured

##### Static Analysis
```bash
# Extract IPA
unzip app.ipa -d extracted/

# Analyze binary
class-dump -H extracted/Payload/App.app/App

# Check Info.plist
plutil -p extracted/Payload/App.app/Info.plist

# Search for secrets
strings extracted/Payload/App.app/App | grep -i 'api\|key\|secret\|token'
```

##### Dynamic Analysis
```bash
# SSL Pinning Bypass
frida -U -f com.app.bundle -l ios-ssl-bypass.js

# Jailbreak Detection Bypass
frida -U -f com.app.bundle -l ios-jailbreak-bypass.js

# Keychain Dump
frida -U -f com.app.bundle -l ios-keychain-dump.js

# Method Swizzling
frida -U -f com.app.bundle -l ios-swizzle.js
```

##### Common Vulnerabilities

###### 1. Insecure Data Storage
```bash
# Check Keychain
frida -U com.app.bundle -l keychain_dump.js

# Check local storage
ls /var/mobile/Containers/Data/Application/<UUID>/Documents/
ls /var/mobile/Containers/Data/Application/<UUID>/Library/

# Check SQLite
sqlite3 /var/mobile/Containers/Data/Application/<UUID>/Documents/*.db
```

###### 2. Insecure Communication
```bash
# Check ATS settings
# App Transport Security in Info.plist
# NSAllowsArbitraryLoads

# Test with Burp Suite
# Configure proxy on device
```

###### 3. Insecure Authentication
```bash
# Test biometric bypass
# Test session management
# Test token storage
```

###### 4. Reverse Engineering
```bash
# Decrypt App Store apps
frida -U -f com.app.bundle -l decrypt.js

# Dump decrypted IPA
class-dump -H decrypted.app/App
```

##### Tools
- Frida
- Objection
- class-dump
- Burp Suite
- Cycript
- Needle

## Explain the complete process of reverse engineering an Android APK file.

#### Android APK Reverse Engineering

##### Step 1: APK Extraction
```bash
# Get APK from device
adb shell pm list packages | grep <app>
adb pull /data/app/<package>/base.apk
```

##### Step 2: Decompilation
```bash
# Using apktool
apktool d base.apk -o decompiled/

# Using jadx for Java source
jadx -d output/ base.apk

# Using dex2jar
d2j-dex2jar base.apk -o app.jar
```

##### Step 3: Manifest Analysis
```xml
<!-- AndroidManifest.xml -->
<!-- Check: -->
- Permissions requested
- Exported components
- Intent filters
- Backup settings
- Debuggable flag
- Network security config
```

##### Step 4: Static Analysis
```bash
# Search for hardcoded secrets
grep -r 'api_key\|password\|secret' smali/
grep -r 'http://\|https://' smali/

# Check for dangerous permissions
- READ_SMS, SEND_SMS
- READ_CONTACTS
- ACCESS_FINE_LOCATION
- CAMERA, RECORD_AUDIO
- READ_PHONE_STATE
```

##### Step 5: Dynamic Analysis
```bash
# Install on emulator
adb install base.apk

# Monitor with Frida
frida -U -f <package> -l hook.js

# Network monitoring
mitmproxy -p 8080
```

##### Step 6: Smali Code Analysis
```smali
# Look for:
- API calls to suspicious domains
- Data exfiltration methods
- Root detection bypass
- SSL pinning bypass
- Dynamic code loading
```

##### Tools Required
- apktool, jadx, dex2jar
- Frida, Objection
- mitmproxy, Burp Suite
- JD-GUI, Bytecode Viewer
- ADB, Android Studio emulator

## How to analyze Android APK permissions and identify security risks?

#### Android APK Permission Analysis

##### Extract Permissions
```bash
# Using aapt
aapt dump permissions base.apk

# Using apktool
apktool d base.apk
# Check AndroidManifest.xml
```

##### Permission Categories

###### Dangerous Permissions (Require User Grant)
- `READ_CALENDAR` - Calendar access
- `CAMERA` - Camera access
- `READ_CONTACTS` - Contact list
- `ACCESS_FINE_LOCATION` - GPS location
- `RECORD_AUDIO` - Microphone
- `READ_PHONE_STATE` - Phone info
- `READ_SMS` - SMS messages
- `WRITE_EXTERNAL_STORAGE` - File access

###### Normal Permissions (Auto-granted)
- `INTERNET` - Network access
- `ACCESS_NETWORK_STATE` - Network status
- `VIBRATE` - Vibration
- `WAKE_LOCK` - Prevent sleep

##### Risk Assessment
```python
# Risk scoring
dangerous_perms = {
    'READ_SMS': 8,
    'RECORD_AUDIO': 9,
    'CAMERA': 7,
    'ACCESS_FINE_LOCATION': 8,
    'READ_CONTACTS': 6,
    'READ_PHONE_STATE': 5
}

# Calculate risk score
risk_score = sum(dangerous_perms.get(p, 0) for p in permissions)
```

##### Red Flags
- Excessive permissions for app functionality
- Dangerous permissions without clear need
- Custom permissions with signature protection
- Permissions declared but not used
- Runtime permission requests for sensitive data

##### Tools
- APK Analyzer (Android Studio)
- MobSF (Mobile Security Framework)
- AndroBugs
- QARK
- Exodus Privacy

## Explain how to reverse engineer an EXE executable file.

#### Windows EXE Reverse Engineering

##### Step 1: Static Analysis
```bash
# File info
file suspicious.exe
strings suspicious.exe | grep -i 'http\|cmd\|powershell\|registry'

# PE analysis
pefile suspicious.exe
pestudio suspicious.exe
```

##### Step 2: Disassembly
```bash
# Using IDA Pro
ida64 suspicious.exe

# Using Ghidra
ghidraRun suspicious.exe

# Using Radare2
r2 -A suspicious.exe
```

##### Step 3: Dynamic Analysis
```bash
# Run in sandbox
cuckoo submit suspicious.exe

# Monitor with Process Monitor
procmon.exe

# Monitor with API Monitor
apimonitor.exe
```

##### Step 4: Code Analysis

###### Look for:
- Anti-debugging techniques
- Anti-VM detection
- String obfuscation
- API hooking
- Registry modifications
- Network communications
- File system operations
- Process injection

##### Step 5: Unpacking
```bash
# Identify packer
peid suspicious.exe

# Generic unpacking
# Set breakpoint on OEP
# Dump memory at OEP
# Fix imports with Import Reconstructor
```

##### Step 6: Behavioral Analysis
- Monitor file system changes
- Track registry modifications
- Capture network traffic
- Analyze process tree
- Check for persistence mechanisms

##### Tools
- IDA Pro, Ghidra, Radare2
- x64dbg, OllyDbg
- PEiD, PEStudio
- Cuckoo Sandbox
- Process Monitor, API Monitor
- Wireshark, Fiddler

## How to reverse engineer firmware from embedded devices?

#### Firmware Reverse Engineering

##### Step 1: Firmware Acquisition
```bash
# Download from vendor
# Extract from device
# Flash dump
flashrom -p internal -r firmware.bin

# UART/JTAG access
minicom -D /dev/ttyUSB0
```

##### Step 2: Firmware Analysis
```bash
# File type identification
binwalk firmware.bin

# Extract filesystem
binwalk -e firmware.bin

# Entropy analysis
binwalk -E firmware.bin
```

##### Step 3: Filesystem Analysis
```bash
# Mount filesystem
mount -o loop rootfs.squashfs /mnt/firmware

# Search for credentials
grep -r 'password\|admin\|root' /mnt/firmware

# Check for hardcoded keys
find /mnt/firmware -name '*.pem\|*.key\|*.crt'
```

##### Step 4: Binary Analysis
```bash
# Identify architecture
file bin/busybox

# Disassemble
ghidra bin/busybox

# Check for vulnerabilities
- Buffer overflows
- Command injection
- Default credentials
- Weak encryption
```

##### Step 5: Network Analysis
```bash
# Monitor traffic
tcpdump -i eth0 -w capture.pcap

# Analyze protocols
wireshark capture.pcap
```

##### Common Vulnerabilities
- Default credentials
- Hardcoded API keys
- Command injection in web interface
- Buffer overflows in network services
- Weak/wifi password storage
- Missing authentication on debug interfaces

##### Tools
- Binwalk, Firmware Mod Kit
- Ghidra, IDA Pro
- QEMU (emulation)
- FirmWalker, FirmAE
- UART/JTAG adapters

## Explain how to decompile and analyze Android APK manifest files.

#### Android Manifest Analysis

##### Extract Manifest
```bash
# Using apktool
apktool d base.apk -o decompiled/
cat decompiled/AndroidManifest.xml

# Using aapt
aapt dump xmltree base.apk AndroidManifest.xml
```

##### Key Manifest Elements

###### 1. Permissions
```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.READ_SMS"/>
<uses-permission android:name="android.permission.CAMERA"/>
```

###### 2. Components
```xml
<!-- Activities -->
<activity android:name=".MainActivity" android:exported="true">

<!-- Services -->
<service android:name=".BackgroundService" android:exported="false">

<!-- Receivers -->
<receiver android:name=".BootReceiver" android:exported="true">

<!-- Providers -->
<provider android:name=".DataProvider" android:exported="true">
```

###### 3. Security Flags
```xml
android:debuggable="true"  <!-- Risk! -->
android:allowBackup="true"  <!-- Risk! -->
android:networkSecurityConfig="@xml/network_security_config"
```

###### 4. Intent Filters
```xml
<intent-filter>
    <action android:name="android.intent.action.MAIN"/>
    <category android:name="android.intent.category.LAUNCHER"/>
</intent-filter>
```

##### Security Checks
1. **Exported Components**: Can be accessed by other apps
2. **Debuggable Flag**: Allows debugging in production
3. **Backup Flag**: Allows data backup
4. **Network Security Config**: TLS/SSL settings
5. **Permission Protection Levels**: normal, dangerous, signature

##### Tools
- APK Analyzer (Android Studio)
- apktool
- aapt/aapt2
- Manifest Explorer
- MobSF

## How to use Frida for dynamic instrumentation on Android?

#### Frida Dynamic Instrumentation

##### Setup
```bash
# Install Frida
pip install frida-tools

# Push server to device
adb push frida-server /data/local/tmp/
adb shell chmod 755 /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &
```

##### Basic Hooking
```javascript
// hook.js
Java.perform(function() {
    // Hook a class method
    var MainActivity = Java.use('com.example.app.MainActivity');
    MainActivity.onCreate.implementation = function(savedInstanceState) {
        console.log('onCreate called!');
        this.onCreate(savedInstanceState);
    };
});
```

##### SSL Pinning Bypass
```javascript
Java.perform(function() {
    var TrustManager = Java.use('javax.net.ssl.X509TrustManager');
    var SSLContext = Java.use('javax.net.ssl.SSLContext');
    
    // Create custom TrustManager
    var TrustManagerImpl = Java.registerClass({
        name: 'com.custom.TrustManager',
        implements: [TrustManager],
        methods: {
            checkClientTrusted: function(chain, authType) {},
            checkServerTrusted: function(chain, authType) {},
            getAcceptedIssuers: function() { return []; }
        }
    });
});
```

##### Root Detection Bypass
```javascript
Java.perform(function() {
    var RootDetection = Java.use('com.example.app.RootDetection');
    RootDetection.isRooted.implementation = function() {
        return false;
    };
});
```

##### Common Hooks
```javascript
// Monitor HTTP requests
var URL = Java.use('java.net.URL');
URL.$init.overload('java.lang.String').implementation = function(url) {
    console.log('URL: ' + url);
    return this.$init(url);
};

// Monitor file operations
var File = Java.use('java.io.File');
File.$init.overload('java.lang.String').implementation = function(path) {
    console.log('File access: ' + path);
    return this.$init(path);
};
```

##### Running Scripts
```bash
# Spawn app
frida -U -f com.example.app -l hook.js --no-pause

# Attach to running app
frida -U com.example.app -l hook.js
```

## How to perform malware analysis on a suspicious file?

#### Malware Analysis Methodology

##### Phase 1: Static Analysis
```bash
# File info
file suspicious.exe
md5sum suspicious.exe
sha256sum suspicious.exe

# String analysis
strings suspicious.exe | head -100
strings suspicious.exe | grep -i 'http\|cmd\|powershell'

# PE analysis
pefile suspicious.exe
pestudio suspicious.exe
```

##### Phase 2: Automated Analysis
```bash
# VirusTotal check
# Upload hash to virustotal.com

# Sandbox analysis
cuckoo submit suspicious.exe

# Hybrid Analysis
# Submit to hybrid-analysis.com
```

##### Phase 3: Dynamic Analysis
```bash
# Run in isolated environment
# Monitor with Process Monitor
procmon.exe

# Monitor network
wireshark

# Monitor registry
regshot
```

##### Phase 4: Code Analysis
```bash
# Disassemble
ghidra suspicious.exe

# Look for:
- Anti-debugging techniques
- String obfuscation
- API hooking
- Process injection
- Persistence mechanisms
- C2 communication
- Data exfiltration
```

##### Phase 5: IOC Extraction
```
# Indicators of Compromise
- File hashes (MD5, SHA256)
- Network indicators (IPs, domains, URLs)
- Registry keys
- File paths
- Mutex names
- API calls
```

##### Tools
- IDA Pro, Ghidra
- x64dbg, OllyDbg
- PEiD, PEStudio
- Cuckoo Sandbox
- Process Monitor
- Wireshark
- YARA rules
- VirusTotal
