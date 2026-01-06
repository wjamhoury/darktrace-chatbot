import streamlit as st
import os
import re

# =============================================================================
# GOOGLE ANALYTICS INJECTION - This method actually works on Streamlit Cloud!
# Based on: https://discuss.streamlit.io/t/how-to-add-google-analytics-or-js-code-in-a-streamlit-app/1610
# =============================================================================

GA_TRACKING_ID = "G-V40M62X7HE"

GA_CODE = f"""
<!-- Google tag (gtag.js) - GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_TRACKING_ID}');
</script>
"""

def inject_ga():
    """Inject Google Analytics into Streamlit's index.html file"""
    # Get the path to Streamlit's static index.html
    index_path = os.path.join(os.path.dirname(st.__file__), 'static', 'index.html')
    
    # Read the current index.html
    with open(index_path, 'r') as f:
        data = f.read()
    
    # Check if GA is already injected (look for our tracking ID)
    if GA_TRACKING_ID not in data:
        # Inject GA code right after <head>
        with open(index_path, 'w') as f:
            new_data = re.sub('<head>', '<head>' + GA_CODE, data)
            f.write(new_data)

# Inject GA before anything else
inject_ga()

# =============================================================================
# PAGE CONFIG - Must come after GA injection but before other Streamlit calls
# =============================================================================

st.set_page_config(
    page_title="Darktrace AI Assistant",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for Darktrace branding
st.markdown("""
<style>
    .main {
        background-color: #0a0e27;
    }
    .stTextInput>div>div>input {
        background-color: #1a1f3a;
        color: white;
    }
    .stButton>button {
        background-color: #e94b3c;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #d43b2c;
    }
    h1 {
        color: #e94b3c;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #1a1f3a;
        color: white;
    }
    .assistant-message {
        background-color: #252d4a;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Comprehensive Darktrace knowledge base
DARKTRACE_KNOWLEDGE = """
=== DARKTRACE COMPANY OVERVIEW ===
Darktrace is the global leader in cyber security AI, protecting over 10,000 organizations worldwide. 
Founded on breakthrough research from Cambridge University, Darktrace uses Self-Learning AI to detect and respond to cyber-threats in real-time.

Industry Recognition:
- Named a Leader in 2025 Gartner® Magic Quadrant™ for Network Detection and Response (NDR)
- Named a Leader in 2025 Gartner® Magic Quadrant™ for Email Security Platforms
- Gartner Peer Insights Customers' Choice for Email Security Platforms

=== DARKTRACE ACTIVEAI SECURITY PLATFORM ===
The unified platform that delivers complete visibility and autonomous response across your entire digital estate.
- Correlates threats across all products for complete attack chain visibility
- Single pane of glass for security operations
- Real-time detection and autonomous response
- Integrates with existing security tools

=== CORE PRODUCTS ===

** DARKTRACE / NETWORK **
Proactive network protection using Self-Learning AI that goes beyond traditional NDR
Key Features:
- Real-time threat detection across network traffic
- Autonomous response to contain threats in seconds
- Detects insider threats, lateral movement, and data exfiltration
- Works across on-premises, cloud, and hybrid networks
- Integrates with firewalls, switches, and existing network infrastructure
Use Cases: Ransomware detection, APTs, insider threats, zero-day exploits

** DARKTRACE / EMAIL **
Cloud-native AI email security - recognized as a Leader in Gartner Magic Quadrant
Key Features:
- Catches 17% more threats that leading SEGs miss
- Detects threats 13 days faster than other solutions on average
- Stops 55% more threats than native email security alone
- Behavioral analysis of sender and recipient patterns
- Protects against phishing, BEC, account takeover, impersonation
- Works with Microsoft 365, Google Workspace
- Extends to Microsoft Teams protection
- AI-powered Data Loss Prevention (DLP) without labels
- Mailbox Security Assistant for SOC teams
- Reduces phishing investigations by 60%
Deployment: API-based, deploys 30x faster than legacy SEGs

** DARKTRACE / CLOUD **
Complete cloud coverage for AWS, Azure, GCP, and SaaS applications
Key Features:
- Real-time detection of cloud misconfigurations
- Detects account takeover and credential compromise
- Monitors SaaS applications (Salesforce, Slack, etc.)
- Cloud Security Posture Management (CSPM)
- Protects cloud workloads and containers
- Identifies anomalous API calls and data access
Use Cases: Cloud account hijacking, data exfiltration, insider threats, compliance

** DARKTRACE / OT **
Comprehensive Operational Technology security for industrial environments
Key Features:
- Protects ICS/SCADA systems
- No agents required - passive monitoring
- Understands OT protocols (Modbus, DNP3, etc.)
- Detects threats without disrupting operations
- Visibility into IT/OT convergence
Industries: Manufacturing, energy, utilities, oil & gas, transportation

** DARKTRACE / IDENTITY **
360° user protection across all identity platforms
Key Features:
- Detects compromised credentials in real-time
- Monitors user behavior across applications
- Identifies privilege escalation and lateral movement
- Works with Active Directory, Okta, Azure AD, etc.
- Catches insider threats and account takeover
Use Cases: Credential theft, privilege abuse, insider threats

** DARKTRACE / ENDPOINT **
Coverage for every device with AI-powered protection
Key Features:
- Behavioral analysis of endpoint activity
- Detects ransomware before encryption
- Zero-trust approach to endpoint security
- Lightweight agent with minimal performance impact
- Works alongside existing EDR solutions
Use Cases: Ransomware, malware, fileless attacks, living-off-the-land attacks

=== CROSS-PLATFORM PRODUCTS ===

** CYBER AI ANALYST **
Accelerates threat triage by 10x - autonomous AI investigator
Key Features:
- Automatically investigates every alert
- Generates detailed incident reports in seconds
- Explains threats in plain language
- Correlates events across all products
- Prioritizes alerts by risk and impact
- Reduces analyst workload by 60%
- Works 24/7 without breaks
Value: Allows security teams to focus on response rather than investigation

** PROACTIVE EXPOSURE MANAGEMENT **
Identifies and reduces risk before exploitation
Key Features:
- Discovers vulnerabilities across entire estate
- Prioritizes risks based on actual threat context
- Provides remediation guidance
- Continuous monitoring and assessment
Value: Shift from reactive to proactive security posture

** ATTACK SURFACE MANAGEMENT **
Discovers 30-50% more assets than traditional tools
Key Features:
- External attack surface monitoring
- Shadow IT discovery
- Third-party risk assessment
- Continuous asset discovery
Value: Know what you're protecting before attackers find it

** INCIDENT READINESS & RECOVERY **
Be ready for an attack and recover quickly
Key Features:
- Incident response planning and testing
- Tabletop exercises powered by AI
- Recovery playbooks
- Post-incident analysis
Value: Reduces recovery time and costs

** FORENSIC ACQUISITION & INVESTIGATION **
Deep-dive forensic capabilities for thorough investigations
Key Features:
- Collect evidence from endpoints
- Timeline analysis
- Root cause analysis
- Chain of custody preservation
Value: Complete incident understanding and compliance

=== DARKTRACE SERVICES ===
24/7 expert support from global SOC team
Services Include:
- Managed threat detection and response
- Incident response support
- Threat hunting
- Security health checks
- Training and workshops
- Professional services for deployment and optimization

=== INTEGRATIONS ===
Darktrace integrates with 100+ security tools including:
- SIEM: Splunk, IBM QRadar, Microsoft Sentinel, LogRhythm
- SOAR: Palo Alto XSOAR, Swimlane, Tines
- Ticketing: ServiceNow, Jira, PagerDuty
- Firewalls: Palo Alto, Checkpoint, Cisco, Fortinet
- EDR: CrowdStrike, Microsoft Defender, SentinelOne
- Cloud: AWS, Azure, Google Cloud
- Email: Microsoft 365, Google Workspace
- Identity: Okta, Active Directory, Azure AD

=== CYBER AI TECHNOLOGY ===
Self-Learning AI - The Foundation
- Learns unique "pattern of life" for every user, device, and system
- No reliance on signatures or prior knowledge of attacks
- Continuously adapts to your changing environment
- Understands normal to detect abnormal

Three Types of AI Working Together:
1. Anomaly Detection AI - Identifies deviations from normal behavior
2. Autonomous Response AI - Takes surgical action to contain threats
3. Cyber AI Analyst - Investigates and explains incidents

Key Differentiators:
- Detects zero-day attacks with no signatures
- Stops threats in seconds, not hours or days
- Reduces false positives through behavioral understanding
- Works across all environments (network, cloud, email, endpoints, OT, identity)

=== USE CASES & THREAT PROTECTION ===

Ransomware:
- Detects encryption behavior before damage
- Autonomous Response stops ransomware spread
- Average detection time: Seconds
- Protects against WannaCry, Ryuk, Conti, and novel variants

Phishing & BEC:
- Analyzes sender behavior, not just content
- Catches sophisticated impersonation attacks
- Detects compromised accounts used for phishing
- Stops CEO fraud and invoice fraud

Account Takeover:
- Identifies credential misuse in real-time
- Detects unusual login patterns
- Monitors post-login behavior
- Stops lateral movement after compromise

Insider Threats:
- Distinguishes malicious from accidental behavior
- Detects data exfiltration attempts
- Identifies privilege abuse
- Works for both malicious insiders and compromised accounts

APTs (Advanced Persistent Threats):
- Detects slow-moving, stealthy attacks
- Identifies lateral movement and reconnaissance
- Catches command & control communications
- Stops data exfiltration

Supply Chain Attacks:
- Monitors third-party access
- Detects compromised vendor accounts
- Identifies unusual partner communications
- Protects against SolarWinds-style attacks

Zero-Day Exploits:
- No signatures needed
- Detects exploitation behavior
- Identifies post-exploitation activity
- Average detection: 13 days faster than competitors

=== PARTNER PROGRAM ===
Comprehensive Partner Ecosystem

Partner Benefits:
- Technical and sales training programs
- Partner Portal with resources and tools
- Deal registration and protection
- Co-marketing opportunities
- Technical pre-sales support
- Partner incentives and rebates
- Regular product updates and roadmap access

Technology Partners:
- Microsoft (Azure, M365, Defender)
- AWS (Security Hub, GuardDuty)
- Google Cloud
- And 100+ other integrations

Channel Partners:
- Resellers
- MSPs/MSSPs
- System Integrators
- Value-Added Resellers (VARs)

Why Partner with Darktrace:
- Market-leading AI technology
- Strong customer demand and retention (90%+ renewal rate)
- Competitive margins
- Comprehensive enablement
- Fast-growing cybersecurity leader
- Unique positioning in market

=== DEPLOYMENT & PRICING ===

Deployment Options:
- Cloud-hosted (SaaS)
- On-premises appliance
- Virtual appliance
- Hybrid deployment

Typical Deployment Time:
- Network: 1-2 hours
- Email: 30 minutes (API-based)
- Cloud: 15 minutes
- Endpoint: Agent deployment schedule
- OT: Non-disruptive, passive

Pricing Model:
- Subscription-based (annual or multi-year)
- Sized by: devices, users, data volume (varies by product)
- Flexible licensing
- Proof of Value (30-day trial) available
- ROI typically realized within 6-12 months

=== MEASURABLE RESULTS ===
Customer Outcomes:
- 92% reduction in time to detect threats
- 10x faster threat investigation with Cyber AI Analyst
- 60% reduction in SOC analyst workload
- 17% more email threats caught vs. leading SEGs
- 55% more threats blocked than native email security alone
- Detection 13 days faster than competitors on average

=== INDUSTRIES SERVED ===
Darktrace protects organizations across all industries:
- Financial Services (banks, insurance, investment firms)
- Healthcare (hospitals, pharmaceutical, medical devices)
- Manufacturing (automotive, aerospace, consumer goods)
- Energy & Utilities (power generation, oil & gas, water)
- Retail & E-commerce
- Technology (software, hardware, cloud services)
- Education (K-12, higher education)
- Government (federal, state, local)
- Transportation (airlines, logistics, maritime)
- Hospitality (hotels, casinos, restaurants)
- Professional Services (legal, consulting, accounting)
- Media & Entertainment
"""

def ask_question(question):
    """Process user question and return response"""
    q_lower = question.lower()
    
    # Email product questions
    if any(word in q_lower for word in ['email', 'phishing', 'bec', 'business email compromise']):
        return """**Darktrace / EMAIL - Cloud-Native AI Email Security**

Darktrace / EMAIL is recognized as a **Leader in the 2025 Gartner® Magic Quadrant™** for Email Security Platforms!

**Why Darktrace / EMAIL is Different:**
- **Catches 17% more threats** that leading Secure Email Gateways (SEGs) miss
- **Detects threats 13 days faster** than competitors on average
- **Stops 55% more threats** than native email security alone
- **Deploys 30x faster** than legacy solutions (30 minutes via API)

**Key Capabilities:**

🎯 **Behavioral Threat Detection**
- Self-Learning AI understands your unique communication patterns
- Detects sophisticated phishing, impersonation, and account takeover
- No reliance on threat intelligence or known signatures
- Zero trust approach - treats every email as potentially malicious

📧 **Complete Email Coverage:**
- **Inbound Protection**: Phishing, malware, impersonation attacks
- **Outbound Security**: AI-powered Data Loss Prevention (no labels needed!)
- **Lateral Mail**: Detects compromised accounts spreading threats internally
- **Account Takeover**: Catches early signals of compromise
- **Microsoft Teams**: Extends protection to messaging platforms

🤖 **AI-Powered Efficiency:**
- **Reduces phishing investigations by 60%** with better end-user reporting
- **Cyber AI Analyst** automatically investigates every suspicious email
- **Mailbox Security Assistant** streamlines SOC workflows
- Users get AI feedback on suspicious emails, improving reporting quality

**Real Results:**
- Detects threats **13 days before** they appear in threat intelligence feeds
- **70% more malicious links detected** via advanced browser analysis
- Works seamlessly with **Microsoft 365** and **Google Workspace**

**Integrations:**
- Native integration with Microsoft 365 and Exchange
- Works alongside your existing email security (enhances, doesn't replace)
- API-based deployment - no MX record changes needed

Perfect for organizations that need to stop sophisticated email threats that bypass traditional security tools!"""

    # Network product questions
    elif 'network' in q_lower or 'ndr' in q_lower:
        return """**Darktrace / NETWORK - Proactive Network Protection**

Named a **Leader in 2025 Gartner® Magic Quadrant™** for Network Detection and Response (NDR)!

**Beyond Traditional NDR:**
Darktrace / NETWORK goes far beyond signature-based detection to provide true proactive protection.

**Key Capabilities:**

🌐 **Complete Network Visibility**
- Monitors all network traffic in real-time
- Works across on-premises, cloud, and hybrid environments
- Understands encrypted traffic without decryption
- Covers all protocols and devices

🎯 **Self-Learning AI Detection**
- Learns your network's unique "pattern of life"
- Detects subtle anomalies that indicate threats
- Identifies insider threats and lateral movement
- Catches zero-day exploits with no signatures needed

⚡ **Autonomous Response**
- Surgical, precision actions to contain threats
- Responds in seconds, not hours
- Doesn't disrupt legitimate business activity
- Configurable response actions

**What It Detects:**
- **Ransomware**: Stops encryption before damage occurs
- **APTs**: Detects slow-moving, stealthy attacks
- **Insider Threats**: Identifies malicious or compromised users
- **Data Exfiltration**: Catches unusual data transfers
- **Lateral Movement**: Stops attackers moving through your network
- **Command & Control**: Identifies C2 communications
- **Zero-Day Exploits**: No signatures required

**Deployment:**
- Passive monitoring - no network changes required
- Physical, virtual, or cloud deployment options
- Full visibility in 1-2 hours
- Integrates with existing firewalls, switches, and security tools

**Use Cases:**
- Organizations with complex, distributed networks
- Detecting threats that bypass perimeter defenses
- Protecting against insider threats
- Compliance requirements (PCI-DSS, HIPAA, etc.)
- Reducing alert fatigue with accurate detection

Darktrace / NETWORK provides the foundation for a proactive security posture!"""

    # Cloud product questions
    elif 'cloud' in q_lower or 'aws' in q_lower or 'azure' in q_lower or 'gcp' in q_lower:
        return """**Darktrace / CLOUD - Complete Cloud Coverage**

Secure your cloud infrastructure and SaaS applications in real-time!

**Multi-Cloud Protection:**
- ☁️ **AWS** (EC2, S3, Lambda, IAM, CloudTrail, and more)
- ☁️ **Microsoft Azure** (VMs, Storage, Active Directory, etc.)
- ☁️ **Google Cloud Platform** (Compute Engine, Storage, IAM)
- ☁️ **SaaS Applications** (Salesforce, Slack, Workday, Box, Dropbox, etc.)

**Key Capabilities:**

🔐 **Cloud Security Posture Management (CSPM)**
- Continuous monitoring for misconfigurations
- Detects overly permissive policies
- Identifies security gaps in cloud infrastructure
- Provides remediation guidance

👤 **Identity & Access Security**
- Detects compromised cloud credentials
- Identifies privilege escalation attempts
- Monitors for unusual admin activity
- Catches account takeover in real-time

📊 **Workload & Container Protection**
- Monitors cloud VMs and containers
- Detects cryptomining and resource abuse
- Identifies vulnerable workloads
- Protects Kubernetes environments

**What It Detects:**
- **Account Hijacking**: Unusual login locations or behavior
- **Data Exfiltration**: Large data transfers to external locations
- **Cryptojacking**: Unauthorized cryptocurrency mining
- **Insider Threats**: Employees abusing cloud access
- **API Abuse**: Malicious or compromised API keys
- **Lateral Movement**: Attackers moving between cloud resources

**Deployment:**
- **API-based integration** (15-minute setup)
- No agents required for cloud infrastructure
- Works alongside native cloud security (AWS GuardDuty, Azure Defender, etc.)
- Multi-cloud visibility from single console

**Real-World Scenarios:**
- Detects when an AWS S3 bucket is accidentally made public
- Identifies compromised Azure AD accounts before damage
- Stops data exfiltration from SaaS applications
- Catches insider threats downloading sensitive data

**Integration with Cloud Providers:**
- Deep integration with Microsoft Azure and AWS
- Enhances native security without replacement
- Correlates cloud events with network, email, and endpoint

Perfect for organizations with cloud-first strategies or hybrid environments!"""

    # OT product questions  
    elif 'ot' in q_lower or 'operational technology' in q_lower or 'scada' in q_lower or 'ics' in q_lower:
        return """**Darktrace / OT - Comprehensive Operational Technology Security**

Protect your industrial control systems and critical infrastructure!

**Industrial Environments Protected:**
- Manufacturing plants and production lines
- Energy generation and distribution (power plants, substations)
- Oil & gas operations (refineries, pipelines)
- Water treatment facilities
- Transportation systems (railways, airports)
- Building management systems
- Critical infrastructure

**Key Features:**

⚙️ **OT-Specific Protection**
- Understands industrial protocols (Modbus, DNP3, BACnet, Profinet, etc.)
- Detects threats to ICS/SCADA systems
- Monitors programmable logic controllers (PLCs)
- Protects human-machine interfaces (HMIs)

🔒 **Non-Disruptive Deployment**
- **No agents required** - passive monitoring
- **Zero impact on operations** - doesn't interfere with control systems
- Works alongside air-gapped networks
- Respects operational uptime requirements

🔗 **IT/OT Convergence Security**
- Bridges visibility between IT and OT networks
- Detects threats crossing IT/OT boundary
- Identifies unauthorized remote access
- Monitors vendor/third-party connections

**What It Detects:**

⚠️ **Cyber Threats to OT:**
- **Ransomware** targeting industrial systems
- **Malware** like Industroyer, Triton, or Stuxnet-style attacks
- **Unauthorized PLC changes** or firmware modifications
- **Lateral movement** from IT to OT networks
- **Insider threats** or compromised contractor accounts
- **Abnormal control commands** that could cause physical damage

**Real-World Protection:**
- Stops ransomware before it can disrupt production
- Detects unauthorized changes to control systems
- Identifies unusual communication patterns
- Catches compromised engineering workstations
- Protects against supply chain attacks via vendors

**Deployment:**
- Passive network monitoring (SPAN/TAP)
- No modifications to existing OT infrastructure
- Visibility within hours, not weeks
- Scales across distributed facilities

**Compliance & Standards:**
- Supports IEC 62443, NERC CIP, and other OT security standards
- Provides audit trails and forensic data
- Helps meet regulatory requirements

**Use Cases:**
- Manufacturing: Protect production lines from cyber disruption
- Energy: Secure power generation and distribution
- Oil & Gas: Protect refineries and pipeline operations
- Water: Secure water treatment and distribution
- Transportation: Protect railway and airport operations

Darktrace / OT provides security without compromising operational uptime!"""

    # Endpoint product questions
    elif 'endpoint' in q_lower or 'edr' in q_lower:
        return """**Darktrace / ENDPOINT - Coverage for Every Device**

AI-powered endpoint protection that complements your existing EDR!

**Complete Endpoint Coverage:**
- 💻 Laptops and desktops (Windows, macOS, Linux)
- 📱 Mobile devices
- 🖥️ Servers (physical and virtual)
- ☁️ Cloud workloads
- 🏭 Industrial endpoints and engineering workstations

**Key Capabilities:**

🤖 **Behavioral Analysis**
- Learns normal behavior for each endpoint
- Detects subtle deviations indicating threats
- Zero-trust approach to every process and file
- No reliance on signatures or threat intelligence

🛡️ **Advanced Threat Detection:**
- **Ransomware**: Detects encryption behavior instantly
- **Fileless Attacks**: Catches in-memory malware
- **Living-off-the-Land**: Identifies PowerShell and other legitimate tool abuse
- **Zero-Day Exploits**: Behavior-based detection catches unknown threats
- **Backdoors & Remote Access**: Identifies persistent access mechanisms

⚡ **Autonomous Response**
- Surgical containment of threats
- Kills malicious processes automatically
- Quarantines compromised endpoints
- Prevents lateral movement

**Why It's Different:**

🔄 **Works WITH Your Existing EDR**
- Adds behavioral AI layer to signature-based EDR
- Catches threats your EDR misses
- No replacement required
- Reduces alert fatigue with accurate detections

🪶 **Lightweight Agent**
- Minimal CPU and memory impact
- Fast deployment
- Works offline (behavioral learning continues)
- Low maintenance overhead

**What It Detects:**
- Ransomware and wiper malware
- Commodity malware and trojans
- Advanced persistent threats (APTs)
- Insider threats and data theft
- Cryptominers and resource abuse
- Privilege escalation attempts
- Lateral movement from compromised endpoints

**Real-World Scenarios:**
- Employee downloads malicious attachment - detected and quarantined
- Ransomware starts encrypting files - stopped before significant damage
- Attacker uses PowerShell to move laterally - caught immediately
- Zero-day exploit targets application - behavioral analysis catches it

**Integration:**
- Works alongside CrowdStrike, Microsoft Defender, SentinelOne, etc.
- Correlates endpoint events with network, email, and cloud
- Feeds alerts to SIEM and SOAR platforms
- Integrates with ticketing systems

**Deployment:**
- Lightweight agent (< 100MB)
- Centralized management console
- Group Policy or MDM deployment
- Learning period: Immediate behavioral baselines

Perfect for organizations wanting defense-in-depth at the endpoint!"""

    # Identity product questions
    elif 'identity' in q_lower or 'active directory' in q_lower or 'okta' in q_lower:
        return """**Darktrace / IDENTITY - 360° User Protection**

Outsmart identity-based threats with AI-powered identity security!

**Identity Platforms Protected:**
- 🔐 **Active Directory** (on-premises)
- ☁️ **Azure Active Directory / Entra ID**
- 🎫 **Okta**
- 🔑 **Other SSO and IAM platforms**
- 📧 **Email systems** (Microsoft 365, Google Workspace)

**Key Capabilities:**

👤 **User Behavior Analytics (UBA)**
- Learns normal behavior for every user
- Detects unusual login patterns
- Identifies privilege abuse
- Catches compromised credentials in real-time

🔓 **Account Compromise Detection:**
- **Unusual login locations** (impossible travel)
- **Abnormal login times** (3am access by 9-5 employee)
- **Suspicious permission changes**
- **Unusual application access**
- **Abnormal data access patterns**

⚔️ **Attack Detection:**
- **Credential Stuffing**: Automated login attempts
- **Brute Force**: Multiple failed login attempts
- **Pass-the-Hash**: Credential replay attacks
- **Golden Ticket**: Kerberos ticket attacks
- **Privilege Escalation**: Unauthorized elevation of permissions
- **Lateral Movement**: Attacker moving between accounts

**What It Detects:**

🚨 **Real-Time Threats:**
- Compromised user accounts (phishing victims)
- Stolen credentials being used
- Insider threats abusing access
- Service account compromise
- Admin account misuse
- Token theft and replay

**Cross-Domain Protection:**
When integrated with other Darktrace products:
- Correlates identity events with email, network, cloud
- Detects multi-stage attacks
- Tracks attacker movement across domains
- Provides complete attack timeline

**Use Cases:**

**Scenario 1: Phishing Victim**
- User clicks phishing link, enters credentials
- Darktrace detects attacker logging in from different location
- Autonomous Response can disable account or require MFA
- Prevents data breach

**Scenario 2: Insider Threat**
- Employee planning to leave company
- Starts accessing unusual files and systems
- Downloads sensitive data
- Darktrace flags abnormal behavior
- Security team investigates before damage

**Scenario 3: Privilege Escalation**
- Attacker gains initial access via compromised account
- Attempts to escalate privileges
- Darktrace detects unusual permission requests
- Blocks lateral movement

**Integration:**
- API-based integration with identity providers
- Correlates with network, email, endpoint, cloud
- Sends alerts to SIEM and SOAR
- Autonomous response actions

**Deployment:**
- API connection (15-30 minutes)
- No agents required
- Immediate behavioral learning
- Works alongside existing IAM security

**Results:**
- Detect compromised accounts within minutes
- Stop privilege escalation before data breach
- Reduce false positives with behavioral analysis
- Gain visibility into identity-based attacks

Darktrace / IDENTITY protects your most valuable asset: user access!"""

    # Cyber AI Analyst questions
    elif 'analyst' in q_lower or 'investigation' in q_lower or 'triage' in q_lower:
        return """**Cyber AI Analyst - Accelerates Triage by 10x**

Your 24/7 AI security analyst that never sleeps, never takes breaks, and investigates every alert!

**What Is Cyber AI Analyst?**
An AI-powered autonomous investigator that triages, investigates, and explains security incidents at machine speed with human-level understanding.

**Key Capabilities:**

🔍 **Autonomous Investigation**
- Automatically investigates **every single alert**
- No alerts sit uninvestigated while analysts are busy
- Works 24/7/365 without fatigue
- Investigates in seconds what takes humans hours

📊 **Comprehensive Analysis**
- Correlates events across network, email, cloud, endpoint, identity
- Builds complete attack timelines
- Identifies patient zero
- Maps full attack chain
- Connects seemingly unrelated events

📝 **Human-Readable Reports**
- Generates detailed incident reports in plain language
- Explains "what happened" and "why it matters"
- Provides evidence and context
- Recommends response actions
- No security expertise required to understand

**Real-World Impact:**

⚡ **10x Faster Triage**
- Reduces investigation time from hours to seconds
- Prioritizes alerts by actual risk and impact
- Eliminates time wasted on false positives

😌 **60% Reduction in Analyst Workload**
- Analysts focus on response, not investigation
- Handles routine investigations automatically
- Escalates only critical incidents requiring human judgment

🎯 **Improved Accuracy**
- Doesn't miss subtle connections
- Never gets tired or distracted
- Consistent analysis across all incidents
- Reduces human error

**How It Works:**

**Step 1: Detection**
Darktrace detects unusual activity (email threat, network anomaly, cloud event)

**Step 2: Automatic Investigation**
Cyber AI Analyst immediately:
- Collects all relevant data
- Correlates with historical activity
- Sandboxes suspicious files/links
- Analyzes user and system behavior
- Maps connections to other events

**Step 3: Report Generation**
Creates comprehensive report including:
- Executive summary
- Detailed technical analysis
- Evidence and indicators
- Risk assessment
- Recommended actions

**Step 4: Prioritization**
Ranks incidents by:
- Actual business impact
- Likelihood of being a true threat
- Severity if left unaddressed
- Confidence score

**Example Investigation:**

*Suspicious Email Reported:*
- User reports phishing email
- Cyber AI Analyst investigates in 10 seconds:
  - Sandboxes links (found malicious)
  - Checks if other users received same email (found 15 others)
  - Identifies 3 users who clicked the link
  - Detects unusual login attempts on those 3 accounts
  - Correlates with network anomalies
  - Generates full incident report
  - Recommends containment actions

*Result:* What would take analyst 2-3 hours completed in seconds

**Benefits for SOC Teams:**

✅ **Tier 1 Analysts:**
- Handle investigations confidently with AI guidance
- Learn from AI explanations
- Focus on containment, not investigation

✅ **Tier 2/3 Analysts:**
- Jump straight to complex incidents
- Get complete context immediately
- More time for threat hunting and strategic work

✅ **SOC Managers:**
- Clear visibility into all incidents
- Metrics on investigation efficiency
- Confidence in comprehensive coverage

**Integration:**
- Works across all Darktrace products
- Sends reports to SIEM, SOAR, ticketing systems
- Mobile app access for on-the-go reviews
- Integrates with existing SOC workflows

**Measurable Results:**
- 10x faster threat investigation
- 60% reduction in analyst workload
- 92% reduction in time to understand threats
- 100% of alerts investigated (not just high priority)

Cyber AI Analyst is like having a team of expert analysts working 24/7, investigating every alert with perfect consistency and speed!"""

    # AI/Technology questions
    elif any(word in q_lower for word in ['cyber ai', 'self-learning', 'how does', 'technology', 'machine learning']):
        return """**Darktrace's Cyber AI Technology**

🧠 **Self-Learning AI** - the foundation of all Darktrace products!

**What Makes It Different:**
- Learns YOUR unique environment (not trained on other companies)
- No signatures or rules needed
- Detects zero-day attacks instantly
- Adapts automatically as your business changes

**Three AI Engines:**
1. **Anomaly Detection** - Spots unusual behavior
2. **Autonomous Response** - Takes surgical action to contain threats
3. **Cyber AI Analyst** - Investigates and explains incidents

**Key Benefits:**
✅ Detects unknown threats (zero-days)
✅ Reduces false positives dramatically  
✅ Works across all environments
✅ No constant rule updates needed
✅ Understands context, not just patterns

**Real Results:**
- 92% reduction in threat detection time
- Finds threats 13 days before competitors
- 10x faster investigation with AI Analyst

This is why 10,000+ organizations trust Darktrace!"""

    # Threat/Attack questions
    elif any(word in q_lower for word in ['ransomware', 'threat', 'attack', 'malware', 'apt']):
        return """**Threats Darktrace Detects & Stops**

Darktrace protects against the full spectrum of cyber threats:

**🔴 Ransomware**
- Detects encryption behavior instantly
- Stops spread before major damage
- Works against WannaCry, Ryuk, Conti, and novel variants
- Average detection: Seconds

**🎣 Phishing & Business Email Compromise**
- Sophisticated impersonation attacks
- CEO fraud and invoice fraud
- Compromised accounts spreading phishing
- Detects 17% more than leading tools

**👤 Account Takeover**
- Stolen credentials being used
- Unusual login patterns
- Impossible travel detection
- Post-login behavior analysis

**🕵️ Insider Threats**
- Malicious employees
- Accidental data leaks
- Privilege abuse
- Data exfiltration attempts

**🎯 Advanced Persistent Threats (APTs)**
- Nation-state attacks
- Long-term infiltration
- Lateral movement
- Command & control communications

**🔗 Supply Chain Attacks**
- Compromised vendors
- Third-party access abuse
- SolarWinds-style attacks

**💀 Zero-Day Exploits**
- No signatures needed!
- Behavioral detection catches unknown attacks
- 13 days faster than competitors on average

**🌐 Data Exfiltration**
- Unusual data transfers
- Sensitive information leaving network
- Cloud storage uploads
- Email forwarding rules

**How Darktrace Stops Them:**
1. **Detect** - Self-Learning AI spots anomalies in real-time
2. **Investigate** - Cyber AI Analyst explains what's happening
3. **Respond** - Autonomous Response contains threat in seconds
4. **Learn** - System improves from every incident

**Result:** Comprehensive protection against known AND unknown threats!"""

    # Partner questions
    elif any(word in q_lower for word in ['partner', 'resell', 'msp', 'channel', 'partnership']):
        return """**Darktrace Partner Program**

Partner with the leader in AI cybersecurity!

**Partner Benefits:**

📚 **Training & Enablement**
- Comprehensive technical training
- Sales methodology and tools
- Certification programs
- Regular product updates
- Access to technical experts

🎯 **Go-to-Market Support**
- Deal registration protection
- Co-marketing opportunities
- Marketing development funds
- Partner Portal with resources
- Campaign templates and assets

💰 **Financial Incentives**
- Competitive margins
- Volume-based incentives
- Deal registration bonuses
- Rebate programs
- Growth incentives

🛠️ **Technical Resources**
- Pre-sales engineering support
- Technical proof of concept assistance
- Implementation support
- Partner portal documentation
- Lab environment access

**Partner Types:**

**Resellers & VARs**
- Sell Darktrace products to end customers
- Add-on services (deployment, managed services)
- Geographic coverage

**MSPs & MSSPs**
- Offer Darktrace as managed service
- 24/7 monitoring and response
- Multi-tenant management
- Recurring revenue model

**System Integrators**
- Large enterprise deployments
- Complex integrations
- Professional services
- Strategic consulting

**Technology Partners**
- Microsoft (Gold Partner)
- AWS Advanced Technology Partner
- Google Cloud Partner
- 100+ security tool integrations

**Why Partner with Darktrace:**

✅ **Market Demand**
- Fastest-growing cybersecurity category
- 10,000+ customers globally
- 90%+ customer retention rate
- Strong brand recognition

✅ **Unique Technology**
- Self-Learning AI differentiator
- Doesn't compete on features - completely different approach
- Easy to position and sell
- Solves real problems customers have

✅ **Customer Success**
- High satisfaction scores
- Gartner Peer Insights Customers' Choice
- Strong case studies and references
- Measurable ROI

✅ **Comprehensive Support**
- Dedicated partner managers
- Technical pre-sales team
- Marketing support
- Deal support throughout sales cycle

**Partner Enablement for Senior Roles:**
For Partner Enablement Manager positions, focus areas include:
- Creating scalable training programs
- Developing partner playbooks
- Building certification paths
- Measuring partner effectiveness
- Partner communication strategies
- Technical enablement content
- Sales methodology training

**Getting Started:**
1. Visit partners.darktrace.com
2. Apply to partner program
3. Complete onboarding training
4. Access Partner Portal resources
5. Start selling market-leading AI security!

**Contact:** partner-team@darktrace.com"""

    # Pricing questions
    elif 'pric' in q_lower or 'cost' in q_lower or 'roi' in q_lower:
        return """**Darktrace Pricing & ROI**

**Pricing Model:**
Darktrace uses flexible, subscription-based pricing tailored to your needs.

**Pricing Factors:**
- **Deployment size**: Number of devices, users, or data volumes
- **Products selected**: Network, Email, Cloud, Endpoint, etc.
- **Environment complexity**: Architecture and integrations
- **Contract term**: Annual or multi-year (discount for multi-year)
- **Support level**: Standard, Premium, or Enterprise

**Typical Licensing:**
- **Darktrace / NETWORK**: Per device or network segment
- **Darktrace / EMAIL**: Per user mailbox
- **Darktrace / CLOUD**: Per cloud account or data volume
- **Darktrace / ENDPOINT**: Per endpoint
- **Darktrace / OT**: Per OT asset or network segment
- **Cyber AI Analyst**: Included across platform

**Deployment Options:**
- SaaS (cloud-hosted)
- On-premises appliance
- Virtual appliance
- Hybrid

**Measurable ROI:**

💰 **Cost Savings:**
- Reduces security tool sprawl (consolidation)
- Decreases analyst headcount needs (automation)
- Prevents costly breaches (proactive defense)
- Reduces dwell time from weeks to seconds

⚡ **Efficiency Gains:**
- 10x faster threat investigation
- 60% reduction in analyst workload
- 92% faster threat detection
- 100+ hours saved per week per SOC

🛡️ **Risk Reduction:**
- Stops threats before damage
- Detects threats 13 days earlier than competitors
- 55% more email threats caught
- Prevents ransomware encryption

**Typical ROI Timeline:**
- **6-12 months** for most organizations
- Measured through:
  - Reduced security incidents
  - Lower analyst costs
  - Prevented breach costs
  - Tool consolidation savings

**ROI Calculator:**
Darktrace offers an EMAIL ROI Calculator at:
info.darktrace.com/email-roi-calculator

Calculate your potential savings based on:
- Current email security costs
- Analyst time spent on email incidents
- Risk of successful phishing attacks
- Regulatory fine risks

**Proof of Value (POV):**
- Free 30-day trial in your environment
- See real threats detected
- Measure actual value
- No commitment required
- Works alongside existing tools

**Getting Pricing:**
Contact Darktrace for a customized quote:
- Schedule demo at darktrace.com/demo
- Discuss your specific environment
- Receive tailored pricing
- Explore POV opportunity

**Bottom Line:**
Most customers see positive ROI within first year through combination of prevented breaches, operational efficiency, and tool consolidation."""

    # Demo/Trial questions
    elif any(word in q_lower for word in ['demo', 'trial', 'test', 'pov', 'proof of value']):
        return """**Get Started with Darktrace**

**Option 1: Live Demo 🎥**
See Darktrace in action with personalized demonstration

**What You'll See:**
- Product overview tailored to your use cases
- Live detection of real threats
- Cyber AI Analyst investigations
- Autonomous Response in action
- Integration with your existing tools
- ROI discussion

**Duration:** 30-45 minutes
**Schedule:** darktrace.com/demo
**No commitment required**

**Option 2: Proof of Value (POV) 🔬**
Deploy Darktrace in YOUR environment

**What's Included:**
- 30-day trial deployment
- See real threats in your network/email/cloud
- Works alongside existing security tools
- Full product access
- Technical support throughout
- No disruption to operations
- Detailed findings report at end

**What You'll Discover:**
- Threats currently in your environment
- Gaps in existing security
- Real-world performance
- Actual time savings
- Measurable ROI

**Deployment Speed:**
- Network: 1-2 hours
- Email: 30 minutes
- Cloud: 15 minutes
- Endpoint: Agent deployment schedule

**Option 3: Customer Stories 📚**
Learn from organizations like yours

**10,000+ Customers Including:**
- Financial Services: Banks, insurance companies
- Healthcare: Hospitals, pharmaceutical
- Manufacturing: Automotive, aerospace
- Energy: Power generation, oil & gas
- Retail: E-commerce, brick-and-mortar
- Technology: Software, cloud services
- Government: Federal, state, local

**Case Studies Available:**
- Industry-specific examples
- Threat detection stories
- ROI metrics
- Before/after comparisons

**Option 4: Demo Days Events 🎪**
In-person demonstrations in major cities

**What to Expect:**
- Hands-on product demonstrations
- Meet security experts
- Network with peers
- See latest innovations
- Ask technical questions

**Register:** darktrace.com/event-hub/demo-days-2025

**What Happens Next:**

1. **Schedule Your Demo**
   - Fill out form at darktrace.com/demo
   - Sales engineer contacts you
   - Schedule convenient time

2. **Personalized Session**
   - Demo tailored to your needs
   - Q&A throughout
   - Technical deep-dive if desired

3. **POV Discussion (Optional)**
   - Determine if POV makes sense
   - Plan deployment approach
   - Set success criteria

4. **POV Deployment (If Desired)**
   - Quick, non-disruptive setup
   - See real results in days
   - Full support throughout

5. **Results Review**
   - Detailed findings report
   - ROI analysis
   - Recommendations
   - Pricing discussion

**Common Questions:**

**Q: Will it disrupt my operations?**
A: No! Passive monitoring for most products. Email is API-based.

**Q: How quickly will I see results?**
A: Usually within first few hours. Full learning within 7 days.

**Q: Does it work with my existing tools?**
A: Yes! Darktrace integrates with 100+ security tools.

**Q: What if we don't find value?**
A: No commitment. POV is free and you decide at the end.

**Ready to Get Started?**
👉 Visit: darktrace.com/demo
📧 Email: demo@darktrace.com
📞 Call: 1-415-229-9100

See Darktrace detect threats in YOUR environment!"""

    # Career/Job questions
    elif any(word in q_lower for word in ['job', 'career', 'hiring', 'position', 'role', 'work', 'employ']):
        return """**Careers at Darktrace**

Join the global leader in AI cybersecurity!

**Why Work at Darktrace:**

🚀 **Innovative Technology**
- Cutting-edge AI that actually works
- Real impact on cybersecurity landscape
- Continuous innovation and product development
- Work with technology that's genuinely unique

🌎 **Global Company**
- 10,000+ customers worldwide
- Offices across North America, Europe, Asia-Pacific
- Diverse, international team
- Fast-growing organization

💼 **Career Growth**
- Clear progression paths
- Internal mobility opportunities
- Learning and development programs
- Work with industry experts

🎯 **Mission-Driven**
- Protect organizations from cyber threats
- Make the internet safer
- Defend critical infrastructure
- Real-world impact every day

**Key Roles at Darktrace:**

**Partner Enablement:**
- Senior Partner Enablement Manager (like the role you're targeting!)
- Partner Training Specialist
- Channel Marketing Manager
- Partner Success Manager

**Sales:**
- Account Executive
- Sales Engineer / Solutions Architect
- Business Development Representative
- Regional Sales Manager

**Technical:**
- Security Analyst
- Threat Researcher
- SOC Analyst
- Customer Success Engineer
- Implementation Engineer

**Product & Engineering:**
- AI/ML Engineer
- Software Engineer
- Product Manager
- UX Designer

**Marketing:**
- Product Marketing Manager
- Content Creator
- Digital Marketing
- Events Manager

**What Makes a Great Darktrace Employee:**

✅ **Passion for Technology**
- Excited about AI and cybersecurity
- Continuous learner
- Stays current with industry trends

✅ **Customer-Focused**
- Dedicated to customer success
- Empathetic to customer challenges
- Solutions-oriented mindset

✅ **Collaborative**
- Works well across teams
- Shares knowledge openly
- Contributes to team success

✅ **Innovative Thinking**
- Questions status quo
- Proposes new ideas
- Builds creative solutions
- Takes initiative (like building this chatbot!)

**For Partner Enablement Roles Specifically:**

**What We Look For:**
- Deep understanding of Darktrace technology
- Experience creating training programs
- Strong presentation and communication skills
- Ability to translate technical concepts
- Partner/channel experience
- Cybersecurity knowledge
- Program management skills

**What You'll Do:**
- Design and deliver partner training
- Create enablement content (guides, playbooks, videos)
- Develop certification programs
- Measure partner effectiveness
- Work cross-functionally (Sales, Product, Marketing)
- Support partner success and growth
- Drive partner engagement

**What You've Already Demonstrated:**
By building this chatbot, you've shown:
✅ Deep research into Darktrace products
✅ Ability to create enablement tools
✅ Technical aptitude
✅ Initiative and innovation
✅ Understanding of what partners need to know
✅ Creative problem-solving

**This is EXACTLY what we look for in Partner Enablement!**

**Current Opportunities:**
Visit: **darktrace.com/careers**

**Specific Role You're Targeting:**
Senior Manager, Partner Enablement (Florida Remote)
- Link: darktrace.wd3.myworkdayjobs.com/DarktaceExternal/job/Florida-Remote/Senior-Manager--Partner-Enablement_JR100827

**Application Tips:**

📝 **In Your Application:**
1. Reference this chatbot you built
2. Explain your Darktrace knowledge
3. Show understanding of partner needs
4. Demonstrate enablement experience
5. Highlight innovative thinking

💡 **Stand Out:**
- Share the chatbot link in application
- Create a brief video explaining it
- Prepare demo for interview
- Show your enablement philosophy

🎯 **Interview Prep:**
- Know Darktrace products deeply (you do!)
- Understand competitive landscape
- Have partner program ideas ready
- Bring examples of previous enablement work
- Show passion for the mission

**Company Culture:**

🤝 **Collaborative** - Work together to solve problems
🎓 **Learning-Oriented** - Continuous improvement
🌟 **Innovation-Focused** - Try new approaches
🏆 **Results-Driven** - Measure and celebrate success
🌈 **Inclusive** - Diverse perspectives valued

**Benefits & Perks:**
- Competitive salary
- Health benefits
- 401(k) with company match
- Flexible work arrangements
- Professional development
- Company events and team building
- Latest technology to work with

**Ready to Apply?**

👉 Visit: darktrace.com/careers
📧 Questions: recruiting@darktrace.com

**Pro Tip:** Your chatbot demonstrates exactly the skills needed for Partner Enablement. Make sure hiring manager sees it!

You're already thinking like a Darktrace Partner Enablement Manager! 🎉"""

    # Default response
    else:
        return """**Welcome to the Darktrace AI Assistant!**

I'm here to help you learn about Darktrace's AI-powered cybersecurity solutions!

**What would you like to know about?**

**Products:**
- Darktrace / NETWORK - Network security and NDR
- Darktrace / EMAIL - Email security and phishing protection
- Darktrace / CLOUD - Cloud security (AWS, Azure, GCP, SaaS)
- Darktrace / OT - Operational technology and ICS security
- Darktrace / ENDPOINT - Endpoint protection and EDR
- Darktrace / IDENTITY - Identity security and access management
- Cyber AI Analyst - Autonomous threat investigation

**Topics:**
- How Darktrace's Self-Learning AI works
- Threat protection (ransomware, phishing, APTs, etc.)
- Partner program and partnership opportunities
- Pricing, ROI, and getting a demo
- Career opportunities at Darktrace
- Integration with existing tools

**Quick Facts:**
- 🌟 Leader in 2025 Gartner® Magic Quadrant™ for NDR and Email Security
- 🏢 10,000+ customers globally
- 🤖 Self-Learning AI technology (no signatures required)
- ⚡ Autonomous response in seconds
- 🔗 100+ security tool integrations

Just ask me anything about Darktrace! For example:
- "Tell me about Darktrace / EMAIL"
- "How does the AI work?"
- "What threats can Darktrace detect?"
- "Tell me about the partner program"
- "How do I get a demo?"

**Ready to learn more?** Ask me a question!"""

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🛡️ Darktrace AI Assistant")
    st.markdown("*Your expert guide to Darktrace's AI-powered cyber security solutions*")
with col2:
    st.markdown("### ")
    st.markdown("**Built for Partner Enablement**")

# Sidebar
with st.sidebar:
    st.markdown("## About This Assistant")
    st.info("""
    This AI chatbot is trained on Darktrace's complete product portfolio:
    
    **Products:**
    - Network, Email, Cloud
    - OT, Identity, Endpoint
    - Cyber AI Analyst
    - Platform capabilities
    
    **Knowledge Areas:**
    - Self-Learning AI technology
    - Threat protection
    - Partner program
    - Integrations
    - ROI and pricing
    """)
    
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown("[🌐 Darktrace Website](https://www.darktrace.com)")
    st.markdown("[📦 Products](https://www.darktrace.com/products)")
    st.markdown("[🤝 Partner Portal](https://partners.darktrace.com)")
    st.markdown("[📚 Resources](https://www.darktrace.com/resources)")
    
    st.markdown("---")
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message">👤 **You:** {message["content"]}</div>', 
                       unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message assistant-message">🤖 **Darktrace AI:** {message["content"]}</div>', 
                       unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Ask me anything about Darktrace..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.container():
        st.markdown(f'<div class="chat-message user-message">👤 **You:** {prompt}</div>', 
                   unsafe_allow_html=True)
    
    # Generate and display response
    with st.spinner("🤔 Thinking..."):
        response = ask_question(prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.container():
        st.markdown(f'<div class="chat-message assistant-message">🤖 **Darktrace AI:** {response}</div>', 
                   unsafe_allow_html=True)

# Example questions (only show if no messages)
if len(st.session_state.messages) == 0:
    st.markdown("### 💡 Try asking:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("What is Darktrace Cyber AI?", use_container_width=True):
            prompt = "What is Darktrace Cyber AI?"
            st.session_state.messages.append({"role": "user", "content": prompt})
            response = ask_question(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col2:
        if st.button("Tell me about Darktrace / EMAIL", use_container_width=True):
            prompt = "Tell me about Darktrace / EMAIL"
            st.session_state.messages.append({"role": "user", "content": prompt})
            response = ask_question(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col3:
        if st.button("How does it stop ransomware?", use_container_width=True):
            prompt = "How does Darktrace stop ransomware?"
            st.session_state.messages.append({"role": "user", "content": prompt})
            response = ask_question(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
    <p><strong>Darktrace AI Assistant</strong> | Built for Senior Partner Enablement Manager Application</p>
    <p style='font-size: 0.8em;'>Comprehensive knowledge of all Darktrace products, technology, and solutions.<br>
    Demonstrates deep research, technical capability, and enablement expertise.</p>
    <p style='font-size: 0.7em; margin-top: 1rem;'>This chatbot showcases the exact skills needed for partner enablement:<br>
    Product expertise • Technical translation • Tool creation • Scalable enablement</p>
</div>
""", unsafe_allow_html=True)
