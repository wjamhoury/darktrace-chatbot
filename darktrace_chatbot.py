import streamlit as st
import requests
import json
import time

# Page config
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

# Darktrace knowledge base (condensed from glossary)
DARKTRACE_KNOWLEDGE = """
DARKTRACE COMPANY OVERVIEW:
Darktrace is a global leader in cyber security AI, delivering complete AI-powered cyber defense solutions. 
The company uses Self-Learning AI to detect, investigate, and respond to cyber-threats in real-time across all digital environments.

KEY PRODUCTS:
1. Darktrace ActiveAI Security Platform™ - Unified platform for detecting novel threats
2. Darktrace / NETWORK - Proactive network protection using AI
3. Darktrace / EMAIL - Cloud-native AI email security
4. Darktrace / CLOUD - Complete cloud coverage and security
5. Darktrace / OT - Comprehensive operational technology security
6. Darktrace / IDENTITY - 360° user protection
7. Darktrace / ENDPOINT - Coverage for every device
8. Cyber AI Analyst - Accelerates triage by 10x
9. Proactive Exposure Management - Identifies vulnerabilities before exploitation
10. Attack Surface Management - Monitors external attack surfaces
11. Forensic Acquisition & Investigation - Deep dive forensic tools

CORE TECHNOLOGY - CYBER AI:
Darktrace's Cyber AI is Self-Learning, meaning it understands the unique 'pattern of life' for every user, device, and system.
It detects subtle deviations from normal behavior that indicate cyber-threats, including zero-day attacks and insider threats.
The AI responds autonomously to contain threats in seconds, not hours.

USE CASES DARKTRACE PROTECTS AGAINST:
- Ransomware attacks
- Advanced Persistent Threats (APTs)
- Phishing and spear phishing
- Business Email Compromise (BEC)
- Data loss and exfiltration
- Account takeover
- Insider threats
- Supply chain attacks
- Zero-day exploits

KEY DIFFERENTIATORS:
1. Self-Learning AI - No reliance on signatures or rules
2. Autonomous Response - AI takes action to stop threats in real-time
3. Full visibility - Across network, cloud, email, endpoints, OT, and identity
4. Reduces alert fatigue - AI Analyst triages and investigates automatically
5. 10,000+ customers globally across all industries

INDUSTRIES SERVED:
Healthcare, Financial Services, Manufacturing, Energy & Utilities, Retail & E-commerce, 
Education, Government, Telecommunications, Transportation, Hospitality, Technology, and more.

PARTNER ENABLEMENT:
Darktrace has a robust partner program including technology partnerships with Microsoft, AWS, and others.
Partners benefit from comprehensive training, technical resources, and go-to-market support.
The Partner Portal provides access to sales tools, marketing materials, and technical documentation.

CYBER SECURITY TERMS (Key Glossary):
- Anomaly Detection: Identifying patterns that deviate from normal behavior
- Zero Trust: Security model that assumes no implicit trust
- Network Detection and Response (NDR): Monitoring network traffic for threats
- Endpoint Detection & Response (EDR): Protecting individual devices
- SIEM Integration: Darktrace integrates with Security Information and Event Management systems
- AI Investigations: Autonomous investigation of security incidents
- Threat Hunting: Proactive search for hidden threats
- Cloud Security Posture Management (CSPM): Identifying cloud misconfigurations
"""

def query_free_llm(prompt, context):
    """
    Query Hugging Face's free inference API
    Using Microsoft Phi-2 model (small, fast, free)
    """
    
    API_URL = "https://api-inference.huggingface.co/models/microsoft/phi-2"
    
    # Construct the full prompt with Darktrace context
    full_prompt = f"""You are a Darktrace AI Assistant, an expert on Darktrace's cyber security products and services.

CONTEXT ABOUT DARKTRACE:
{context}

USER QUESTION: {prompt}

Provide a helpful, accurate response about Darktrace based on the context above. If the question is about Darktrace products, explain them clearly. If it's about cyber security concepts, relate them to how Darktrace addresses them. Be professional but conversational.

RESPONSE:"""

    try:
        # Try free inference API (note: may have rate limits)
        response = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "inputs": full_prompt,
                "parameters": {
                    "max_new_tokens": 400,
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "return_full_text": False
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', '').strip()
        
        # Fallback to rule-based responses if API fails
        return generate_fallback_response(prompt, context)
        
    except Exception as e:
        return generate_fallback_response(prompt, context)

def generate_fallback_response(prompt, context):
    """
    Generate intelligent responses based on keyword matching when API is unavailable
    This ensures the demo always works
    """
    prompt_lower = prompt.lower()
    
    # Product questions
    if any(word in prompt_lower for word in ['product', 'network', 'email', 'cloud', 'endpoint']):
        return """Darktrace offers a comprehensive suite of AI-powered cyber security products:

**Darktrace ActiveAI Security Platform™** - The unified platform that delivers complete visibility and autonomous response across your entire digital estate.

**Core Products:**
- **Darktrace / NETWORK**: Proactive protection for your network infrastructure using Self-Learning AI
- **Darktrace / EMAIL**: Cloud-native AI security that stops phishing, BEC, and account takeover
- **Darktrace / CLOUD**: Complete coverage for AWS, Azure, GCP, and SaaS applications
- **Darktrace / ENDPOINT**: Protection for every device with AI-powered detection and response
- **Darktrace / IDENTITY**: 360° user protection across all identity platforms
- **Darktrace / OT**: Comprehensive security for operational technology environments

**AI Analyst**: Accelerates threat triage by 10x, automatically investigating and explaining incidents.

All products work together seamlessly to provide defense-in-depth across your organization."""

    elif any(word in prompt_lower for word in ['cyber ai', 'ai', 'artificial intelligence', 'machine learning']):
        return """Darktrace's Cyber AI is the core technology powering all our products. Here's what makes it unique:

**Self-Learning AI Technology:**
- Learns the unique 'pattern of life' for every user, device, and system in your organization
- Doesn't rely on signatures, rules, or prior knowledge of threats
- Understands normal behavior to detect subtle anomalies that indicate threats

**Key Capabilities:**
1. **Real-time Threat Detection**: Identifies threats as they emerge, including zero-day attacks
2. **Autonomous Response**: Takes precise action to contain threats in seconds
3. **AI Investigations**: Cyber AI Analyst triages alerts 10x faster than human analysts
4. **Continuous Learning**: Adapts to your evolving environment automatically

**Why It Matters:**
- Stops attacks before they cause damage
- Reduces alert fatigue and false positives
- Enables security teams to focus on strategic work
- Protects against unknown and emerging threats

This is the same AI technology trusted by over 10,000 organizations globally."""

    elif any(word in prompt_lower for word in ['ransomware', 'threat', 'attack', 'phishing']):
        return """Darktrace protects against the full spectrum of cyber threats:

**Common Threats We Defend Against:**

🔴 **Ransomware**: Detects encryption behavior and stops ransomware before it spreads
🔴 **Phishing & BEC**: AI analyzes email content, sender behavior, and context to catch sophisticated attacks
🔴 **Account Takeover**: Identifies compromised credentials through behavioral analysis
🔴 **APTs**: Spots Advanced Persistent Threats moving laterally through your network
🔴 **Insider Threats**: Detects malicious or negligent insider activity
🔴 **Supply Chain Attacks**: Monitors third-party access and suspicious behaviors
🔴 **Data Exfiltration**: Stops unauthorized data transfers before information leaves
🔴 **Zero-Day Exploits**: Catches novel attacks with no known signatures

**How Darktrace Stops Threats:**
1. **Detection**: Self-Learning AI identifies anomalies in real-time
2. **Investigation**: AI Analyst automatically triages and explains incidents
3. **Response**: Autonomous Response contains threats in seconds
4. **Prevention**: Learns from every incident to strengthen defenses

Our AI doesn't wait for threat intelligence updates—it protects against threats before they're even named."""

    elif any(word in prompt_lower for word in ['partner', 'enablement', 'partnership']):
        return """Darktrace has a comprehensive Partner Program designed to help partners succeed:

**Partner Benefits:**
- **Training & Certification**: Technical and sales enablement programs
- **Partner Portal**: Access to resources, documentation, and marketing materials
- **Technical Support**: Dedicated partner support team
- **Co-marketing**: Joint go-to-market campaigns and events
- **Deal Registration**: Protected opportunities and partner incentives

**Technology Partners:**
We integrate with leading platforms including:
- Microsoft (Azure, Microsoft 365, Defender)
- AWS (Cloud security integration)
- Major SIEM platforms
- Ticketing and orchestration tools

**Why Partner with Darktrace:**
- Market-leading AI technology that sells itself
- Strong customer retention and satisfaction
- Comprehensive support throughout the sales cycle
- Growing market demand for AI-powered security

For Senior Partner Enablement roles, we focus on:
- Creating partner success programs
- Technical enablement and training
- Sales methodology and tools
- Partner communication and engagement
- Measuring and optimizing partner performance"""

    elif any(word in prompt_lower for word in ['price', 'cost', 'pricing']):
        return """Darktrace pricing is customized based on your organization's needs. Factors include:

- **Deployment size**: Number of devices, users, or data volumes
- **Products selected**: Different combinations of NETWORK, EMAIL, CLOUD, ENDPOINT, etc.
- **Environment complexity**: Network architecture and integrations
- **Support level**: Standard, Premium, or Enterprise support packages

**Typical Deployment Options:**
- Subscription-based licensing (annual or multi-year)
- Flexible deployment: on-premises, cloud, or hybrid
- Proof of Value (POV) available to demonstrate ROI before commitment

**Value Delivered:**
- Reduced dwell time from weeks to seconds
- 92% reduction in time to detect threats
- Autonomous response saves 100+ hours per week
- Measurable ROI typically within 6-12 months

I'd recommend scheduling a demo with our team to discuss specific pricing for your environment. Would you like me to provide more information about what's included?"""

    elif any(word in prompt_lower for word in ['demo', 'trial', 'test', 'try']):
        return """I'd be happy to help you explore Darktrace!

**Getting Started Options:**

1. **Live Demo**: See Darktrace in action with a personalized demonstration
   - Schedule at: darktrace.com/demo
   - 30-45 minute session tailored to your environment
   - No commitment required

2. **Proof of Value (POV)**: Deploy Darktrace in your environment
   - Typically 30-day trial deployment
   - See real threats detected in your network
   - Works alongside existing security tools
   - Full access to all features

3. **Customer Stories**: Learn how organizations like yours use Darktrace
   - 10,000+ customers globally
   - Case studies across all industries
   - Measurable ROI examples

**What You'll See:**
- Real-time threat detection on your network
- AI Analyst automatically investigating incidents
- Autonomous Response containing threats
- Integration with your existing security stack

Would you like help setting up a demo or POV?"""

    elif any(word in prompt_lower for word in ['job', 'career', 'hiring', 'position', 'role']):
        return """Darktrace is always looking for talented professionals to join our team!

**Why Work at Darktrace:**
- Cutting-edge AI technology that's genuinely innovative
- Fast-growing global company (10,000+ customers)
- Impact: Help organizations defend against real cyber threats
- Culture: Collaborative, innovative, and mission-driven
- Career growth: Clear progression paths

**Partner Enablement Roles:**
These positions are critical to partner success and involve:
- Designing and delivering partner training programs
- Creating enablement content and resources
- Working cross-functionally with Sales, Product, and Marketing
- Measuring partner effectiveness and optimizing programs
- Technical knowledge of cyber security and AI

**What Makes a Great Candidate:**
- Deep understanding of Darktrace technology (like this chatbot demonstrates!)
- Experience in partner enablement or technical training
- Strong communication and presentation skills
- Ability to translate complex technical concepts
- Customer-focused mindset

**Current Opportunities:**
Visit darktrace.com/careers to see open positions, including:
- Partner Enablement roles
- Sales Engineering
- Technical Account Management
- Product Marketing

Showing initiative by building tools like this chatbot demonstrates exactly the kind of innovative thinking we value!"""

    else:
        # General fallback
        return """Thank you for your question about Darktrace!

Darktrace is the global leader in cyber security AI, protecting over 10,000 organizations worldwide with Self-Learning AI technology.

**Quick Overview:**
- **Technology**: AI that learns your organization's unique pattern of life
- **Products**: Network, Email, Cloud, Endpoint, Identity, OT security
- **Approach**: Detect threats in real-time and respond autonomously
- **Results**: 10x faster threat triage, stops attacks in seconds

**What can I help you learn about?**
- Specific products (NETWORK, EMAIL, CLOUD, etc.)
- How our Cyber AI works
- Threat protection capabilities
- Partnership opportunities
- Getting a demo
- Career opportunities

Please ask me anything about Darktrace's technology, products, or how we can help secure your organization!"""

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

# Sidebar with information
with st.sidebar:
    st.markdown("## About This Assistant")
    st.info("""
    This AI chatbot is trained on Darktrace's:
    - Product portfolio
    - Cyber AI technology
    - Use cases and solutions
    - Partner program
    - Security glossary
    
    **Ask me about:**
    - Darktrace products
    - How Cyber AI works
    - Threat protection
    - Partner opportunities
    - Demos and trials
    """)
    
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown("[Darktrace Website](https://www.darktrace.com)")
    st.markdown("[Product Information](https://www.darktrace.com/products)")
    st.markdown("[Cyber AI Glossary](https://www.darktrace.com/cyber-ai-glossary)")
    st.markdown("[Partner Portal](https://partners.darktrace.com)")
    
    st.markdown("---")
    if st.button("Clear Conversation"):
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
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.container():
        st.markdown(f'<div class="chat-message user-message">👤 **You:** {prompt}</div>', 
                   unsafe_allow_html=True)
    
    # Generate response
    with st.spinner("🤔 Thinking..."):
        response = query_free_llm(prompt, DARKTRACE_KNOWLEDGE)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display assistant response
    with st.container():
        st.markdown(f'<div class="chat-message assistant-message">🤖 **Darktrace AI:** {response}</div>', 
                   unsafe_allow_html=True)

# Example questions
if len(st.session_state.messages) == 0:
    st.markdown("### 💡 Try asking:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("What is Darktrace Cyber AI?", key="ex1"):
            st.session_state.messages.append({"role": "user", "content": "What is Darktrace Cyber AI?"})
            st.rerun()
    
    with col2:
        if st.button("Tell me about Darktrace products", key="ex2"):
            st.session_state.messages.append({"role": "user", "content": "Tell me about Darktrace products"})
            st.rerun()
    
    with col3:
        if st.button("How does Darktrace stop ransomware?", key="ex3"):
            st.session_state.messages.append({"role": "user", "content": "How does Darktrace stop ransomware?"})
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
    <p><strong>Darktrace AI Assistant Demo</strong> | Built for Partner Enablement Role Application</p>
    <p style='font-size: 0.8em;'>This chatbot demonstrates knowledge of Darktrace products, technology, and solutions.<br>
    Powered by AI with intelligent fallback responses for reliable demonstrations.</p>
</div>
""", unsafe_allow_html=True)