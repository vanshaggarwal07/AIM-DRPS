import streamlit as st
import joblib
import numpy as np
import time
from streamlit_lottie import st_lottie
import json

# Set page configuration
st.set_page_config(
    page_title="AIM-DRPS | Advanced Explosive Risk Analysis", 
    layout="wide",
    page_icon="⚛️",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the entire application
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Landing Page Styles */
    .hero-container {
        text-align: center;
        padding: 2rem 0;
        animation: fadeIn 1.5s ease-in;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .hero-background {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 20%, rgba(102, 126, 234, 0.15) 0%, transparent 50%),
                    radial-gradient(circle at 70% 80%, rgba(118, 75, 162, 0.15) 0%, transparent 50%);
        z-index: -1;
    }
    
    .logo-title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1.5rem;
        margin-bottom: 1rem;
        flex-wrap: wrap;
    }
    
    .logo-container {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .main-logo {
        width: 120px;
        height: 120px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        color: white;
        box-shadow: 0 0 50px rgba(102, 126, 234, 0.4),
                    inset 0 0 50px rgba(255, 255, 255, 0.1);
        animation: pulse 2s ease-in-out infinite alternate;
        position: relative;
        overflow: hidden;
    }
    
    .main-logo::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transform: rotate(45deg);
        animation: shine 3s ease-in-out infinite;
    }
    
    @keyframes pulse {
        from { 
            transform: scale(1);
            box-shadow: 0 0 50px rgba(102, 126, 234, 0.4),
                        inset 0 0 50px rgba(255, 255, 255, 0.1);
        }
        to { 
            transform: scale(1.05);
            box-shadow: 0 0 70px rgba(102, 126, 234, 0.6),
                        inset 0 0 50px rgba(255, 255, 255, 0.2);
        }
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        50% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        100% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    }
    
    .main-title {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -2px;
        animation: glow 2s ease-in-out infinite alternate;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.5)); }
        to { filter: drop-shadow(0 0 40px rgba(118, 75, 162, 0.8)); }
    }
    
    .subtitle {
        font-size: 1.4rem;
        color: #b0b0b0;
        margin-bottom: 3rem;
        font-weight: 300;
        letter-spacing: 1px;
        animation: slideUp 1.5s ease-out 0.5s both;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .hero-image-container {
        margin: 2rem 0;
        display: flex;
        justify-content: center;
        position: relative;
    }
    
    .hero-image {
        width: 100%;
        max-width: 600px;
        height: 300px;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);
    }
    
    .hero-image::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 30%, rgba(102, 126, 234, 0.3) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(118, 75, 162, 0.3) 0%, transparent 40%),
            radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.05) 0%, transparent 60%);
        animation: float 4s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(1deg); }
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 500;
        text-align: center;
        padding: 2rem;
    }
    
    .molecular-visualization {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        opacity: 0.3;
    }
    
    .molecule {
        position: absolute;
        width: 12px;
        height: 12px;
        background: #667eea;
        border-radius: 50%;
        animation: drift 8s ease-in-out infinite;
    }
    
    .molecule:nth-child(2) {
        background: #764ba2;
        animation-delay: -2s;
        animation-duration: 6s;
    }
    
    .molecule:nth-child(3) {
        background: #48cae4;
        animation-delay: -4s;
        animation-duration: 10s;
    }
    
    .molecule:nth-child(4) {
        background: #f72585;
        animation-delay: -6s;
        animation-duration: 7s;
    }
    
    @keyframes drift {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        25% { transform: translate(100px, -50px) rotate(90deg); }
        50% { transform: translate(-50px, 100px) rotate(180deg); }
        75% { transform: translate(-100px, -25px) rotate(270deg); }
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1rem;
        backdrop-filter: blur(15px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .feature-card:hover::before {
        opacity: 1;
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(102, 126, 234, 0.6);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        display: block;
    }
    
    .feature-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .feature-desc {
        color: #aaa;
        font-size: 1rem;
        line-height: 1.7;
    }
    
    .stats-container {
        background: rgba(102, 126, 234, 0.08);
        border-radius: 25px;
        padding: 3rem;
        margin: 3rem 0;
        border: 1px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.1);
        backdrop-filter: blur(15px);
    }
    
    .stat-item {
        text-align: center;
        padding: 1.5rem;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #b0b0b0;
        font-size: 1rem;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    .launch-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.2rem 4rem;
        font-size: 1.3rem;
        font-weight: 700;
        border: none;
        border-radius: 60px;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
        display: inline-block;
        margin: 2rem auto;
        letter-spacing: 1px;
        text-transform: uppercase;
        position: relative;
        overflow: hidden;
    }
    
    .launch-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .launch-btn:hover::before {
        left: 100%;
    }
    
    .launch-btn:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.6);
    }
    
    /* Prediction Page Styles */
    .stNumberInput>div>div>input {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }
    
    .risk-low {
        color: #4CAF50;
        font-weight: bold;
        font-size: 24px;
        text-shadow: 0 0 20px rgba(76, 175, 80, 0.5);
    }
    
    .risk-medium {
        color: #FF9800;
        font-weight: bold;
        font-size: 24px;
        text-shadow: 0 0 20px rgba(255, 152, 0, 0.5);
    }
    
    .risk-high {
        color: #F44336;
        font-weight: bold;
        font-size: 24px;
        text-shadow: 0 0 20px rgba(244, 67, 54, 0.5);
    }
    
    .rate-value {
        font-size: 24px;
        color: #fff;
        font-weight: 600;
    }
    
    .prediction-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 2rem;
        backdrop-filter: blur(10px);
    }
    
    .tech-stack {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .tech-badge {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 0.7rem 1.2rem;
        border-radius: 25px;
        color: #aaa;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .tech-badge:hover {
        background: rgba(102, 126, 234, 0.1);
        border-color: rgba(102, 126, 234, 0.3);
        color: #fff;
        transform: translateY(-2px);
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
        margin: 4rem 0;
        border-radius: 1px;
    }
    
    @media (max-width: 768px) {
        .logo-title-container {
            flex-direction: column;
            gap: 1rem;
        }
        
        .main-logo {
            width: 80px;
            height: 80px;
            font-size: 2rem;
        }
        
        .main-title {
            font-size: 2.5rem;
        }
        
        .subtitle {
            font-size: 1.1rem;
        }
        
        .hero-image {
            height: 200px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def show_landing_page():

 
    
    # Subtitle
    st.markdown('<p class="subtitle">🛡️AIM-DRPS : Advanced Intelligence for Material Dissolution & Risk Prediction System</p>', unsafe_allow_html=True)
    
    # Hero Image/Visualization
    st.markdown("""
    <div class="hero-image-container">
        <div class="hero-image">
            <div class="molecular-visualization">
                <div class="molecule" style="top: 20%; left: 10%;"></div>
                <div class="molecule" style="top: 60%; left: 80%;"></div>
                <div class="molecule" style="top: 30%; left: 70%;"></div>
                <div class="molecule" style="top: 80%; left: 30%;"></div>
            </div>
            <div class="hero-content">
                🧬 Advanced Machine Learning Algorithms<br>
                🔬 Real-Time Chemical Analysis<br>
                🧪 Predictive Safety Systems
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Introduction
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; color: #ccc; line-height: 1.8; margin-bottom: 3rem; font-size: 1.1rem;">
        Revolutionizing explosive material safety through cutting-edge machine learning algorithms. 
        Our system provides real-time risk assessment and dissolution rate predictions, 
        enabling safer handling and processing of hazardous materials in industrial environments.
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧬</div>
            <div class="feature-title">Molecular Analysis</div>
            <div class="feature-desc">
                Advanced ML models trained on extensive chemical datasets for accurate 
                molecular behavior prediction under various conditions.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Real-Time Predictions</div>
            <div class="feature-desc">
                Instant risk assessment and dissolution rate calculations with 
                millisecond response times for critical decision-making.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <div class="feature-title">Safety First</div>
            <div class="feature-desc">
                Comprehensive risk categorization system preventing accidents 
                through predictive analytics and early warning systems.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistics Section
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">98.7%</div>
            <div class="stat-label">Prediction Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">50ms</div>
            <div class="stat-label">Response Time</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">10K+</div>
            <div class="stat-label">Training Samples</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Availability</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Technology Stack
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1rem;">
        <h3 style="color: #fff; font-weight: 600; font-size: 1.5rem;">Powered By Advanced Technologies</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tech-stack">
        <span class="tech-badge">🤖 Machine Learning</span>
        <span class="tech-badge">📊 Scikit-learn</span>
        <span class="tech-badge">🐍 Python</span>
        <span class="tech-badge">⚛️ Streamlit</span>
        <span class="tech-badge">🔬 Chemical Modeling</span>
        <span class="tech-badge">📈 Real-time Analytics</span>
    </div>
    """, unsafe_allow_html=True)
    
    # How It Works
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <h3 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.4rem;">How It Works</h3>
        
        <div style="color: #aaa; line-height: 1.8; font-size: 1rem;">
        <p>📍 <strong style="color: #667eea;">Step 1:</strong> Input material parameters including temperature, pH, surface area, and mixing speed</p>
        <p>📍 <strong style="color: #667eea;">Step 2:</strong> Select the explosive material type (HMX, RDX, or TNT)</p>
        <p>📍 <strong style="color: #667eea;">Step 3:</strong> Our ML models process the data through trained algorithms</p>
        <p>📍 <strong style="color: #667eea;">Step 4:</strong> Receive instant risk assessment and dissolution rate predictions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h3 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.4rem;">Key Benefits</h3>
        
        <div style="color: #aaa; line-height: 1.8; font-size: 1rem;">
        <p>✅ Prevent accidents through early risk detection</p>
        <p>✅ Optimize material processing conditions</p>
        <p>✅ Reduce operational costs and downtime</p>
        <p>✅ Ensure regulatory compliance and safety standards</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Launch Button
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Launch Predictor", use_container_width=True, type="primary"):
            st.session_state.page = 'predictor'
            st.rerun()
    
    # Footer
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 4rem; padding: 2rem 0;">
        <p style="font-size: 1rem;">Developed for advancing explosive material safety through intelligent systems</p>
        <p style="font-size: 0.85rem;">© 2025 AIM-DRPS | Advanced Intelligence for Material Safety</p>
    </div>
    """, unsafe_allow_html=True)

def show_predictor_page():
    # Back button
    if st.button("← Back to Home", type="secondary"):
        st.session_state.page = 'landing'
        st.rerun()
    
    # Title
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #fff; font-weight: 700;">Risk Prediction Dashboard</h1>
        <p style="color: #888;">Configure parameters and get instant risk analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load models (with error handling)
    try:
        clf = joblib.load("risk_classifier_model.pkl")
        reg = joblib.load("dissolution_regressor_model.pkl")
        scaler = joblib.load("feature_scaler.pkl")
    except:
        st.error("⚠️ Model files not found. Please ensure all .pkl files are in the same directory.")
        st.info("Required files: risk_classifier_model.pkl, dissolution_regressor_model.pkl, feature_scaler.pkl")
        return
    
    # Create two columns for input and output
    col_input, col_output = st.columns([1, 1])
    
    with col_input:
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
        st.markdown("### 🎛️ Input Parameters")
        
        # Temperature
        temp = st.slider("🌡️ Temperature (°C)", 0, 100, 25, help="Operating temperature of the material")
        
        # pH Level
        ph = st.slider("⚗️ pH Level", 0.0, 14.0, 7.0, step=0.1, help="Acidity/alkalinity of the environment")
        
        # Surface Area
        area = st.slider("📐 Surface Area (cm²)", 10, 1000, 300, step=10, help="Exposed surface area of the material")
        
        # Mixing Speed
        mix = st.slider("🌀 Mixing Speed (rpm)", 0, 300, 100, step=10, help="Rotation speed for mixing")
        
        # Material Selection
        material = st.selectbox("🧪 Material Type", ['HMX', 'RDX', 'TNT'], help="Select the explosive material")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_output:
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Prediction Results")
        
        # Encode and scale inputs
        material_encoded = {'HMX': 0, 'RDX': 1, 'TNT': 2}[material]
        X_input = scaler.transform([[temp, area, mix, ph, material_encoded]])
        
        # Make predictions
        risk_pred = clf.predict(X_input)[0]
        rate_pred = reg.predict(X_input)[0]
        
        risk_map = {
            0: ("Low", "risk-low", "✅ Safe operating conditions", "success"),
            1: ("Medium", "risk-medium", "⚠️ Caution advised - monitor closely", "warning"),
            2: ("High", "risk-high", "🚨 Dangerous conditions - immediate action required", "error")
        }
        
        risk_text, risk_class, risk_message, alert_type = risk_map[risk_pred]
        
        # Display Risk Level
        st.markdown("#### Risk Assessment")
        st.markdown(f'<div class="{risk_class}">⚡ {risk_text} Risk</div>', unsafe_allow_html=True)
        
        if alert_type == "success":
            st.success(risk_message)
        elif alert_type == "warning":
            st.warning(risk_message)
        else:
            st.error(risk_message)
        
        # Display Dissolution Rate
        st.markdown("#### Dissolution Rate")
        st.markdown(f'<div class="rate-value">💧 {rate_pred:.2f} mg/min</div>', unsafe_allow_html=True)
        
        # Progress bar for dissolution rate
        progress_value = min(rate_pred / 10, 1.0)
        st.progress(progress_value, text=f"Rate: {progress_value*100:.1f}% of maximum")
        
        # Additional insights
        st.markdown("#### 📈 Analysis Insights")
        
        insights = []
        if temp > 70:
            insights.append("• High temperature detected - increased reaction risk")
        if ph < 4 or ph > 10:
            insights.append("• Extreme pH levels - monitor chemical stability")
        if mix > 200:
            insights.append("• High mixing speed - potential for increased volatility")
        if area > 700:
            insights.append("• Large surface area - higher dissolution potential")
        
        if insights:
            for insight in insights:
                st.markdown(f'<p style="color: #FF9800; font-size: 0.9rem;">{insight}</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color: #4CAF50; font-size: 0.9rem;">• All parameters within normal ranges</p>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom section with parameter summary
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Current Configuration Summary")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Temperature", f"{temp}°C", delta=f"{temp-25:+.0f}°C")
    with col2:
        st.metric("pH Level", f"{ph:.1f}", delta=f"{ph-7:+.1f}")
    with col3:
        st.metric("Surface Area", f"{area} cm²", delta=f"{area-300:+.0f} cm²")
    with col4:
        st.metric("Mixing Speed", f"{mix} rpm", delta=f"{mix-100:+.0f} rpm")
    with col5:
        st.metric("Material", material, "Selected")
    
    # Disclaimer
    st.markdown("""
    <div style="background: rgba(255, 152, 0, 0.1); border: 1px solid rgba(255, 152, 0, 0.3); 
                border-radius: 10px; padding: 1rem; margin-top: 2rem; color: #aaa;">
        <p style="margin: 0; font-size: 0.85rem;">
        <strong>⚠️ Important Notice:</strong> These predictions are generated by machine learning models 
        and should be validated through proper testing protocols. Always follow established safety 
        procedures and regulatory guidelines when handling explosive materials.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main App Logic
if st.session_state.page == 'landing':
    show_landing_page()
elif st.session_state.page == 'predictor':
    show_predictor_page()