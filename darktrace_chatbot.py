import streamlit as st
import requests
import json
from datetime import datetime
import uuid

# Page config
st.set_page_config(
    page_title="Darktrace AI Assistant",
    page_icon="🛡️",
    layout="wide"
)

# ============= ANALYTICS SETUP =============
# Replace with your Google Analytics Measurement ID
GOOGLE_ANALYTICS_ID = "G-SQ53G5JRDY"

# Inject Google Analytics
GA_JS = f"""
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GOOGLE_ANALYTICS_ID}');
  
  // Track custom events
  function trackQuestion(question) {{
    gtag('event', 'ask_question', {{
      'event_category': 'Chat',
      'event_label': question,
      'value': 1
    }});
  }}
  
  function trackExampleClick(example) {{
    gtag('event', 'example_click', {{
      'event_category': 'Example Questions',
      'event_label': example,
      'value': 1
    }});
  }}
</script>
<!-- End Google Analytics -->
"""

st.markdown(GA_JS, unsafe_allow_html=True)

# Simple usage counter in session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]
    st.session_state.session_start = datetime.now()
    st.session_state.questions_asked = 0

# ============= END ANALYTICS SETUP =============

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
    .analytics-badge {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background: rgba(233, 75, 60, 0.1);
        border: 1px solid rgba(233, 75, 60, 0.3);
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.7em;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# Comprehensive Darktrace knowledge base (keeping your existing knowledge)
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
"""

def log_interaction(question_text, response_snippet):
    """Log interaction for analytics"""
    st.session_state.questions_asked += 1
    
    # Track with Google Analytics via JavaScript
    st.markdown(f"""
    <script>
        trackQuestion('{question_text[:50]}...');
    </script>
    """, unsafe_allow_html=True)

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

**Deployment:**
- **API-based integration** (15-minute setup)
- No agents required for cloud infrastructure
- Works alongside native cloud security
- Multi-cloud visibility from single console

Perfect for organizations with cloud-first strategies or hybrid environments!"""

    # Add tracking for all responses
    elif 'ot' in q_lower or 'operational' in q_lower:
        return """**Darktrace / OT - Comprehensive Operational Technology Security**

Protect your industrial control systems and critical infrastructure!

**Key Features:**
- Understands industrial protocols (Modbus, DNP3, BACnet, Profinet)
- **No agents required** - passive monitoring
- **Zero impact on operations**
- IT/OT convergence security

**What It Protects:**
- Manufacturing plants
- Energy generation
- Oil & gas operations
- Water treatment
- Transportation systems
- Building management

Perfect for securing OT environments without disrupting operations!"""

    # AI/Technology questions
    elif any(word in q_lower for word in ['cyber ai', 'self-learning', 'how does', 'technology']):
        return """**Darktrace's Cyber AI Technology**

🧠 **Self-Learning AI** - the foundation of all Darktrace products!

**What Makes It Different:**
- Learns YOUR unique environment
- No signatures or rules needed
- Detects zero-day attacks instantly
- Adapts automatically

**Three AI Engines:**
1. **Anomaly Detection** - Spots unusual behavior
2. **Autonomous Response** - Contains threats
3. **Cyber AI Analyst** - Investigates incidents

**Results:**
- 92% reduction in detection time
- 13 days faster than competitors
- 10x faster investigation

Trusted by 10,000+ organizations worldwide!"""

    # Threat questions
    elif any(word in q_lower for word in ['ransomware', 'threat', 'attack']):
        return """**Threats Darktrace Detects & Stops**

**🔴 Ransomware** - Stops encryption in seconds
**🎣 Phishing & BEC** - 17% more than leading tools
**👤 Account Takeover** - Real-time credential monitoring
**🕵️ Insider Threats** - Malicious and accidental
**🎯 APTs** - Nation-state attacks
**🔗 Supply Chain** - Compromised vendors
**💀 Zero-Day** - No signatures needed!
**🌐 Data Exfiltration** - Unusual transfers

**How It Works:**
1. Detect anomalies
2. Investigate automatically
3. Respond in seconds
4. Learn continuously

Complete protection against known AND unknown threats!"""

    # Partner questions
    elif 'partner' in q_lower:
        return """**Darktrace Partner Program**

**Benefits:**
- 📚 Comprehensive training
- 🎯 Co-marketing support
- 💰 Competitive margins
- 🛠️ Technical resources

**Partner Types:**
- Resellers & VARs
- MSPs & MSSPs
- System Integrators
- Technology Partners (Microsoft, AWS, etc.)

**Why Partner:**
- Market-leading AI technology
- 90%+ customer retention
- Strong demand
- Comprehensive support

**Get Started:** partners.darktrace.com"""

    # Career questions
    elif any(word in q_lower for word in ['job', 'career', 'hiring']):
        return """**Careers at Darktrace**

Join the AI cybersecurity leader!

**Your Chatbot Shows:**
✅ Deep Darktrace knowledge
✅ Technical capability
✅ Enablement expertise
✅ Innovation mindset

**This is EXACTLY what Partner Enablement needs!**

**Apply:** darktrace.com/careers

**Your Target Role:**
Senior Manager, Partner Enablement (Florida Remote)

**Pro Tip:** Reference this chatbot in your application!"""

    # Default
    else:
        return """**Welcome to Darktrace AI Assistant!**

I can help you learn about:

**Products:**
- Network, Email, Cloud, OT, Endpoint, Identity
- Cyber AI Analyst

**Topics:**
- Self-Learning AI technology
- Threat protection
- Partner program
- Careers at Darktrace

**Quick Facts:**
- 🌟 Gartner Leader for NDR & Email
- 🏢 10,000+ customers
- 🤖 No signatures required
- ⚡ Autonomous response

**Ask me anything!** Try:
- "Tell me about Darktrace / EMAIL"
- "How does the AI work?"
- "What about the partner program?"
- "Tell me about careers"

Ready to learn more?"""

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
    This AI chatbot is trained on Darktrace's complete product portfolio.
    
    **Products:**
    - Network, Email, Cloud
    - OT, Identity, Endpoint
    - Cyber AI Analyst
    
    **Knowledge Areas:**
    - Self-Learning AI
    - Threat protection
    - Partner program
    - ROI and pricing
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Session Stats")
    st.metric("Questions Asked", st.session_state.questions_asked)
    duration = datetime.now() - st.session_state.session_start
    st.metric("Time Active", f"{duration.seconds // 60}m {duration.seconds % 60}s")
    
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown("[🌐 Darktrace](https://www.darktrace.com)")
    st.markdown("[📦 Products](https://www.darktrace.com/products)")
    st.markdown("[🤝 Partners](https://partners.darktrace.com)")
    
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
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
        log_interaction(prompt, response[:100])
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.container():
        st.markdown(f'<div class="chat-message assistant-message">🤖 **Darktrace AI:** {response}</div>', 
                   unsafe_allow_html=True)

# Example questions
if len(st.session_state.messages) == 0:
    st.markdown("### 💡 Try asking:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("What is Darktrace Cyber AI?", use_container_width=True):
            prompt = "What is Darktrace Cyber AI?"
            st.session_state.messages.append({"role": "user", "content": prompt})
            response = ask_question(prompt)
            log_interaction(prompt, response[:100])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col2:
        if st.button("Tell me about EMAIL security", use_container_width=True):
            prompt = "Tell me about Darktrace / EMAIL"
            st.session_state.messages.append({"role": "user", "content": prompt})
            response = ask_question(prompt)
            log_interaction(prompt, response[:100])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col3:
        if st.button("Partner program details", use_container_width=True):
            prompt = "Tell me about the partner program"
            st.session_state.messages.append({"role": "user", "content": prompt})
            response = ask_question(prompt)
            log_interaction(prompt, response[:100])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# Footer with analytics badge
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
    <p><strong>Darktrace AI Assistant</strong> | Built for Senior Partner Enablement Manager Application</p>
    <p style='font-size: 0.8em;'>Comprehensive knowledge of all Darktrace products, technology, and solutions.</p>
</div>
<div class='analytics-badge'>
    📊 Analytics Enabled
</div>
""", unsafe_allow_html=True)
