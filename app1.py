import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import json
import time
import os

# ==========================================
# 🚀 ULTIMATE PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Neural Genesis | Activation Universe",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 🎨 ULTRA-PREMIUM "SOTA" CSS (v4.0)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Grotesk:wght@300;400;600&family=Rajdhani:wght@300;400;700&display=swap');
    
    :root {
        --neon-blue: #00f2ff;
        --neon-purple: #bc13fe;
        --neon-pink: #ff00bd;
        --bg-dark: #010103;
        --glass-bg: rgba(10, 10, 20, 0.75);
    }

    * { font-family: 'Space Grotesk', sans-serif; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; letter-spacing: 3px; }

    .stApp {
        background-color: var(--bg-dark);
        background-image: 
            radial-gradient(circle at 20% 20%, rgba(0, 242, 255, 0.1) 0%, transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(188, 19, 254, 0.1) 0%, transparent 40%);
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple), var(--neon-pink), var(--neon-blue));
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-flow 5s linear infinite;
        margin-bottom: 0.2rem;
    }

    @keyframes gradient-flow { to { background-position: 200% center; } }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 242, 255, 0.15) !important;
        border-radius: 20px !important;
        padding: 25px !important;
        transition: all 0.4s ease-in-out !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        border-color: var(--neon-blue) !important;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.2) !important;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple)) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.8rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        transition: 0.3s !important;
    }

    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px var(--neon-blue) !important; }
    [data-testid="stMetricValue"] { color: var(--neon-blue) !important; font-family: 'Orbitron', sans-serif; }
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🧠 ASSETS & FUNCTIONS
# ==========================================
@st.cache_data(show_spinner=False)
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_ai = load_lottieurl("https://lottie.host/8b46617a-c603-4b05-9275-f5e2d1a3c6f2/9p0e9R8pQ2.json")

# Relative paths for Cloud deployment
IMG_HOME = "assets/ai_brain_intro_1778668766101.png"
IMG_DIVE = "assets/neural_microscope_v2_1778668825969.png"
IMG_GRADIENT = "assets/digital_waterfall_v2_1778668948806.png"

def safe_image(path, **kwargs):
    if os.path.exists(path):
        st.image(path, **kwargs)
    else:
        st.warning(f"⚠️ Media Asset Missing: {path}. Please ensure the 'assets' folder is uploaded to GitHub.")

def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)
def leaky_relu(x, alpha=0.1): return np.where(x > 0, x, alpha * x)
def tanh(x): return np.tanh(x)
def softmax(x): 
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
def swish(x): return x * sigmoid(x)

functions_meta = {
    "Sigmoid": {"formula": r"f(x) = \frac{1}{1 + e^{-x}}", "def": "Probability mapper (0, 1).", "hinglish": "0 aur 1 ke beech data compress karta hai.", "analogy": "Dimmer Switch", "range": "(0, 1)", "pros": ["Probabilistic", "Smooth"], "cons": ["Vanishing Gradient"], "use": "Binary Classify", "func": sigmoid},
    "ReLU": {"formula": r"f(x) = \max(0, x)", "def": "Default for hidden layers.", "hinglish": "Negative ko block aur positive ko allow karta hai.", "analogy": "One-way Valve", "range": r"[0, \infty)", "pros": ["Fast", "Sparse"], "cons": ["Dying ReLU"], "use": "CNNs", "func": relu},
    "Tanh": {"formula": r"f(x) = \tanh(x)", "def": "Zero-centered alternative.", "hinglish": "Sigmoid jaisa par balanced range (-1 to 1).", "analogy": "Pendulum", "range": "(-1, 1)", "pros": ["Zero-centered"], "cons": ["Saturation"], "use": "RNNs", "func": tanh},
    "Leaky ReLU": {"formula": r"f(x) = \max(0.1x, x)", "def": "Fixes dead neurons.", "hinglish": "Negative data ko thoda sa leak karta hai.", "analogy": "Leaky Pipe", "range": r"(-\infty, \infty)", "pros": ["No Dying ReLU"], "cons": ["Extra param"], "use": "GANs", "func": leaky_relu},
    "Softmax": {"formula": r"f(x_i) = \frac{e^{x_i}}{\sum e^{x_j}}", "def": "Multi-class probability distribution.", "hinglish": "Sare options ka probability batata hai.", "analogy": "Pizza Slices", "range": "[0, 1]", "pros": ["Mutually Exclusive"], "cons": ["Noise Sensitive"], "use": "Object Detection", "func": softmax},
    "Swish": {"formula": r"f(x) = x \cdot \sigma(x)", "def": "Modern smooth kernel by Google.", "hinglish": "ReLU se smoother, deep models me best chalta hai.", "analogy": "Flexible Gate", "range": r"(-0.278, \infty)", "pros": ["State of the Art"], "cons": ["Compute Cost"], "use": "EfficientNets", "func": swish}
}

# ==========================================
# 🛰️ COMMAND HUB
# ==========================================
with st.sidebar:
    if lottie_ai: st_lottie(lottie_ai, height=140, key="side_ai")
    st.markdown("<h2 style='text-align: center; color: var(--neon-blue);'>COMMAND HUB</h2>", unsafe_allow_html=True)
    page = st.radio("GO TO MODULE", ["🛸 Mission Control", "🧠 Neural Archive", "🧪 Synaptic Lab", "🤖 Neural Map", "📊 Matrix View", "📉 Gradient Flow"])

# ==========================================
# 🛸 MODULE: MISSION CONTROL
# ==========================================
if page == "🛸 Mission Control":
    st.markdown('<h1 class="hero-title">Activation Visualizer</h1>', unsafe_allow_html=True)
    safe_image(IMG_HOME, use_container_width=True)
    col1, col2 = st.columns([1, 1.2])
    with col1:
        with st.container(border=True):
            st.subheader("The Non-Linear Edge")
            st.write("Activation functions enable neural networks to learn complex non-linear patterns.")
    with col2:
        with st.container(border=True):
            st.subheader("🚀 Strategic Intel")
            st.markdown("- **Hidden Layers:** ReLU / Swish\n- **Output:** Sigmoid / Softmax")

# ==========================================
# 🧠 MODULE: NEURAL ARCHIVE
# ==========================================
elif page == "🧠 Neural Archive":
    st.title("Neural Archive Dive")
    safe_image(IMG_DIVE, width=450)
    with st.container(border=True):
        st.write("**Neural Archive Dive** focuses on exploring and understanding deep neural network knowledge and archived insights.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.markdown("### ✅ Advantages\n- Fast Exploration\n- Interactive Visuals\n- Debugs Black-Box Models")
    with c2:
        with st.container(border=True):
            st.markdown("### ❌ Disadvantages\n- Compute Intensive\n- Scaling Latency\n- Memory Overhead")
    with c3:
        with st.container(border=True):
            st.markdown("### 🚀 Use Cases\n- AI EdTech\n- Medical Diagnostics\n- Satellite Tracking")

    target = st.selectbox("Select Function", list(functions_meta.keys()))
    meta = functions_meta[target]
    col_l, col_r = st.columns([1, 1.4])
    with col_l:
        with st.container(border=True):
            st.markdown(f"## {target}")
            st.latex(meta['formula'])
            st.info(meta['hinglish'])
    with col_r:
        with st.container(border=True):
            x = np.linspace(-10, 10, 400); y = meta['func'](x)
            fig = go.Figure(); fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#00f2ff', width=5)))
            fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, width="stretch")

# ==========================================
# 🧪 MODULE: SYNAPTIC LAB
# ==========================================
elif page == "🧪 Synaptic Lab":
    st.title("🧪 Live Synaptic Lab")
    cl, cr = st.columns([1, 1.5])
    with cl:
        with st.container(border=True):
            st.subheader("Controls")
            x = st.slider("Input (x)", -10.0, 10.0, 2.0)
            w = st.slider("Weight (w)", -5.0, 5.0, 1.0)
            b = st.slider("Bias (b)", -5.0, 5.0, 0.0)
            fn = st.selectbox("Activation", list(functions_meta.keys()))
            z = (x * w) + b
            out = functions_meta[fn]['func'](z)
            st.metric("Output", f"{out:.4f}")
    with cr:
        with st.container(border=True):
            xr = np.linspace(-10, 10, 500); yr = functions_meta[fn]['func'](xr)
            fig = go.Figure(); fig.add_trace(go.Scatter(x=xr, y=yr, mode='lines', line=dict(color='#00f2ff')))
            fig.add_trace(go.Scatter(x=[z], y=[out], mode='markers', marker=dict(size=15, color='white')))
            fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, width="stretch")

# ==========================================
# 🤖 MODULE: NEURAL MAP
# ==========================================
elif page == "🤖 Neural Map":
    st.title("🤖 Data Architecture Flow")
    with st.container(border=True):
        st.write("**Data Architect Flow** manages how data moves through systems in AI platforms.")
    with st.container(border=True):
        st.subheader("Synaptic Pulse Visualization")
        def create_map():
            layers = [3, 4, 2]
            fig = go.Figure()
            for i in range(len(layers)-1):
                for j in range(layers[i]):
                    for k in range(layers[i+1]):
                        fig.add_trace(go.Scatter(x=[i, i+1], y=[j-layers[i]/2, k-layers[i+1]/2], mode='lines', line=dict(width=1, color='rgba(0,242,255,0.2)')))
            for i, n in enumerate(layers):
                for j in range(n):
                    fig.add_trace(go.Scatter(x=[i], y=[j-n/2], mode='markers', marker=dict(size=25, color='#00f2ff')))
            fig.update_layout(showlegend=False, template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=450)
            return fig
        st.plotly_chart(create_map(), width="stretch")

# ==========================================
# 📊 MODULE: MATRIX VIEW
# ==========================================
elif page == "📊 Matrix View":
    st.title("📊 Topology Matrix")
    cols = st.columns(3)
    for i, (name, meta) in enumerate(functions_meta.items()):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"<h3 style='color: var(--neon-blue);'>{name}</h3>", unsafe_allow_html=True)
                st.markdown(f"**Range:** `{meta['range']}`")
                st.markdown(f"**Use Case:** `{meta['use']}`")
                st.divider()
                st.latex(meta['formula'])

# ==========================================
# 📉 MODULE: GRADIENT FLOW
# ==========================================
elif page == "📉 Gradient Flow":
    st.title("📉 Gradient Flow Analytics")
    with st.container(border=True):
        st.write("**Gradient Flow** is the movement of gradients during backpropagation.")
    safe_image(IMG_GRADIENT, use_container_width=True)
    with st.container(border=True):
        st.subheader("Vanishing Gradient vs ReLU")
        cv1, cv2 = st.columns(2)
        with cv1:
            st.markdown("### ⚠️ Vanishing Gradient")
            st.write("Gradients become extremely small in Sigmoid and Tanh.")
            st.latex(r"\sigma(x) = \frac{1}{1 + e^{-x}}")
        with cv2:
            st.markdown("### ✅ ReLU Solution")
            st.write("ReLU solves this by allowing positive signals to pass.")
            st.latex(r"f(x) = \max(0, x)")

st.markdown("<div style='text-align: center; color: #444; margin-top: 60px;'>© 2026 NEURAL GENESIS // FINAL v4.1</div>", unsafe_allow_html=True)