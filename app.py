# app.py
import streamlit as st
from predictor import predict_text

# Enhanced page configuration
st.set_page_config(
    page_title="AI vs Human Text Detector",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for stunning dark theme with black, gold, and white
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    /* Global Reset and Base Styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%);
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
        color: #ffffff;
    }
    
    /* Remove Streamlit default styling */
    #MainMenu, .stDeployButton, footer, header, .stDecoration {
        visibility: hidden !important;
        height: 0px !important;
    }
    
    .block-container {
        padding: 2rem 1rem !important;
        max-width: 1200px !important;
    }
    
    /* Main Header Section */
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        background: radial-gradient(ellipse at center, rgba(212, 175, 55, 0.1) 0%, transparent 70%);
        border-radius: 20px;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 48%, rgba(212, 175, 55, 0.03) 49%, rgba(212, 175, 55, 0.03) 51%, transparent 52%);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 700;
        color: #d4af37 !important;
        margin-bottom: 1.5rem;
        text-shadow: 0 4px 8px rgba(212, 175, 55, 0.3);
        position: relative;
        z-index: 1;
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    .subtitle {
        font-size: 1.4rem;
        color: rgba(255, 255, 255, 0.8);
        max-width: 600px;
        margin: 0 auto 2rem;
        line-height: 1.6;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    /* Feature Cards Grid */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
        padding: 0 1rem;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.9) 0%, rgba(18, 18, 18, 0.9) 100%);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent 0%, rgba(212, 175, 55, 0.1) 50%, transparent 100%);
        transition: left 0.6s;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(212, 175, 55, 0.5);
        box-shadow: 0 20px 40px rgba(212, 175, 55, 0.2);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.3));
    }
    
    .feature-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #d4af37;
        margin-bottom: 1rem;
        font-family: 'Playfair Display', serif;
    }
    
    .feature-description {
        color: rgba(255, 255, 255, 0.7);
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Input Section */
    .input-section {
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.95) 0%, rgba(18, 18, 18, 0.95) 100%);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 20px;
        padding: 3rem 2.5rem;
        margin: 3rem 0;
        backdrop-filter: blur(15px);
        position: relative;
    }
    
    .input-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #d4af37;
        margin-bottom: 2rem;
        font-family: 'Playfair Display', serif;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Enhanced Text Area */
    .stTextArea > div > div > textarea {
        background: linear-gradient(145deg, rgba(10, 10, 10, 0.9) 0%, rgba(20, 20, 20, 0.9) 100%) !important;
        border: 2px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        line-height: 1.7 !important;
        color: #ffffff !important;
        transition: all 0.3s ease !important;
        min-height: 200px !important;
        resize: vertical !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #d4af37 !important;
        box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.2), 0 8px 25px rgba(0, 0, 0, 0.3) !important;
        outline: none !important;
        background: linear-gradient(145deg, rgba(15, 15, 15, 0.95) 0%, rgba(25, 25, 25, 0.95) 100%) !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Custom Button */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #b8860b 100%) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 1rem 3rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.3) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        width: 100% !important;
        max-width: 300px !important;
        margin: 2rem auto !important;
        display: block !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(212, 175, 55, 0.4) !important;
        background: linear-gradient(135deg, #ffd700 0%, #d4af37 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Result Cards */
    .result-card {
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.95) 0%, rgba(18, 18, 18, 0.95) 100%);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        backdrop-filter: blur(15px);
        animation: slideUpFade 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    @keyframes slideUpFade {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .ai-result {
        border: 1px solid rgba(255, 165, 0, 0.3);
        box-shadow: 0 0 30px rgba(255, 165, 0, 0.1);
    }
    
    .human-result {
        border: 1px solid rgba(212, 175, 55, 0.3);
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.1);
    }
    
    .result-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
        font-family: 'Playfair Display', serif;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    
    .ai-result .result-title {
        color: #ffa500;
    }
    
    .human-result .result-title {
        color: #d4af37;
    }
    
    .confidence-text {
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Confidence Progress Bar */
    .confidence-container {
        margin: 1.5rem 0;
    }
    
    .confidence-bar {
        width: 100%;
        height: 12px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 6px;
        overflow: hidden;
        position: relative;
    }
    
    .confidence-fill {
        height: 100%;
        border-radius: 6px;
        position: relative;
        transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1);
        animation: glowPulse 2s infinite alternate;
    }
    
    @keyframes glowPulse {
        0% { box-shadow: 0 0 5px currentColor; }
        100% { box-shadow: 0 0 20px currentColor; }
    }
    
    .ai-confidence {
        background: linear-gradient(90deg, #ff8c00, #ffa500);
        color: #ffa500;
    }
    
    .human-confidence {
        background: linear-gradient(90deg, #b8860b, #d4af37);
        color: #d4af37;
    }
    
    .result-description {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1rem;
        line-height: 1.6;
        margin-top: 1.5rem;
    }
    
    /* Warning Card */
    .warning-card {
        background: linear-gradient(135deg, rgba(139, 69, 19, 0.2) 0%, rgba(160, 82, 45, 0.2) 100%);
        border: 1px solid rgba(205, 92, 92, 0.5);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        color: #ff6b6b;
        font-weight: 500;
        text-align: center;
        animation: warningPulse 1s ease-in-out;
    }
    
    @keyframes warningPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    /* Metrics Section */
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.8) 0%, rgba(18, 18, 18, 0.8) 100%);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: rgba(212, 175, 55, 0.4);
        transform: translateY(-2px);
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #d4af37;
        font-family: 'Playfair Display', serif;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.7);
        margin-top: 0.5rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 2rem;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.9rem;
        border-top: 1px solid rgba(212, 175, 55, 0.1);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
        }
        
        .subtitle {
            font-size: 1.1rem;
        }
        
        .hero-section {
            padding: 2.5rem 1.5rem;
        }
        
        .input-section {
            padding: 2rem 1.5rem;
        }
        
        .features-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .feature-card {
            padding: 2rem 1.5rem;
        }
        
        .result-card {
            padding: 2rem 1.5rem;
        }
        
        .stButton > button {
            padding: 0.8rem 2rem !important;
            font-size: 1rem !important;
        }
    }
    
    @media (max-width: 480px) {
        .main-title {
            font-size: 2rem;
        }
        
        .hero-section {
            padding: 2rem 1rem;
        }
        
        .input-section {
            padding: 1.5rem 1rem;
        }
        
        .feature-card {
            padding: 1.5rem 1rem;
        }
        
        .result-card {
            padding: 1.5rem 1rem;
        }
    }
    
    /* Touch-friendly hover states for mobile */
    @media (hover: none) and (pointer: coarse) {
        .feature-card:hover {
            transform: none;
        }
        
        .feature-card:active {
            transform: scale(0.98);
            transition: transform 0.1s;
        }
        
        .stButton > button:hover {
            transform: none !important;
        }
        
        .stButton > button:active {
            transform: scale(0.98) !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section with Streamlit fallback
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">🤖 AI vs Human Detector</h1>
        <p class="subtitle">Unveil the origin of any text with precision. Advanced AI technology meets elegant design to deliver instant, accurate analysis of whether content was crafted by artificial intelligence or human creativity.</p>
    </div>
    """, unsafe_allow_html=True)

# Emergency fallback if CSS fails on HuggingFace
if 'title_shown' not in st.session_state:
    st.session_state.title_shown = True
    # This will show if CSS fails
    st.markdown("""
    <script>
    setTimeout(function() {
        var title = document.querySelector('.main-title');
        if (!title || window.getComputedStyle(title).opacity === '0' || window.getComputedStyle(title).visibility === 'hidden') {
            document.querySelector('.backup-title').style.display = 'block';
        }
    }, 100);
    </script>
    """, unsafe_allow_html=True)

# Feature Cards
st.markdown("""
<div class="features-grid">
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Lightning Analysis</div>
        <div class="feature-description">Instant results powered by state-of-the-art machine learning algorithms trained on millions of text samples.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Precision Accuracy</div>
        <div class="feature-description">Advanced neural networks deliver industry-leading accuracy in distinguishing AI from human-generated content.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <div class="feature-title">Privacy Assured</div>
        <div class="feature-description">Your text is processed securely with zero data retention. Complete privacy and confidentiality guaranteed.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Section
st.markdown("""
<div class="input-section">
    <div class="input-title">📝 Text Analysis</div>
""", unsafe_allow_html=True)

text_input = st.text_area(
    "Text Input",
    height=200,
    placeholder="Paste your text here for AI detection analysis. Longer texts provide more accurate results. Whether it's an article, essay, or any written content, our advanced algorithms will analyze the linguistic patterns and provide instant results...",
    help="Enter the text you want to analyze. The system works best with at least 50 words.",
    key="text_input",
    label_visibility="hidden"
)

# Predict Button
if st.button("🔍 Analyze Text", key="predict", type="primary"):
    if text_input.strip() == "":
        st.markdown("""
        <div class="warning-card">
            ⚠️ <strong>Please Enter Text</strong><br>
            Add some text in the input field above to begin the analysis.
        </div>
        """, unsafe_allow_html=True)
    else:
        # Loading animation
        with st.spinner('🧠 Analyzing linguistic patterns and AI signatures...'):
            prediction, confidence = predict_text(text_input)
        
        # Display Results
        if prediction == 1:
            confidence_percent = confidence * 100
            st.markdown(f"""
            <div class="result-card ai-result">
                <div class="result-title">🤖 AI-Generated Content</div>
                <div class="confidence-text">Detection Confidence: {confidence_percent:.1f}%</div>
                <div class="confidence-container">
                    <div class="confidence-bar">
                        <div class="confidence-fill ai-confidence" style="width: {confidence_percent}%;"></div>
                    </div>
                </div>
                <div class="result-description">
                    This text exhibits characteristics commonly found in AI-generated content, including consistent linguistic patterns, uniform sentence structure, and computational writing markers that suggest machine generation.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            confidence_percent = (1 - confidence) * 100
            st.markdown(f"""
            <div class="result-card human-result">
                <div class="result-title">🧠 Human-Written Content</div>
                <div class="confidence-text">Detection Confidence: {confidence_percent:.1f}%</div>
                <div class="confidence-container">
                    <div class="confidence-bar">
                        <div class="confidence-fill human-confidence" style="width: {confidence_percent}%;"></div>
                    </div>
                </div>
                <div class="result-description">
                    This text displays natural human writing characteristics, including varied sentence structures, personal voice, authentic linguistic nuances, and the creative inconsistencies typical of human authors.
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Analysis Metrics
        st.markdown("### 📊 Detailed Analysis")
        
        col1, col2, col3 = st.columns(3)
        
        word_count = len(text_input.split())
        char_count = len(text_input)
        sentences = text_input.count('.') + text_input.count('!') + text_input.count('?')
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{word_count}</div>
                <div class="metric-label">Words Analyzed</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{"AI" if prediction == 1 else "Human"}</div>
                <div class="metric-label">Classification</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            complexity = len(set(text_input.lower().split())) / word_count if word_count > 0 else 0
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{complexity:.2f}</div>
                <div class="metric-label">Vocabulary Diversity</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>🔬 Powered by Advanced Machine Learning • 🛡️ Privacy-First Design • ⚡ Real-Time Analysis</p>
    <p>Sophisticated AI detection technology for the modern digital age</p>
</div>
""", unsafe_allow_html=True)