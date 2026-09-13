<div align="center">

# 🧠 Neural Genesis
### Activation Universe

**An AI-powered, multi-module neural network education platform.**

Explore activation functions, live neuron simulations, and gradient flow analytics through an immersive, dark-themed Command Hub — built with modern web technologies and AI-assisted tooling.

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Launch_App-00FFFF?style=for-the-badge&labelColor=1a1a2e)](https://activation-model-83tbjhtkdhhnpbry53kwxi.streamlit.app/)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![KaTeX](https://img.shields.io/badge/KaTeX-Math_Rendering-A855F7?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Module Navigation](#️-module-navigation)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#️-getting-started)
- [Key Concepts Covered](#-key-concepts-covered)
- [Built With AI Tools](#️-built-with-ai-tools)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Credits](#-credits)

---

## 🎯 Overview

**Neural Genesis** is a dark-themed, interactive learning platform designed to visualize and explain the core concepts behind neural networks and deep learning.

Activation functions are the mathematical heart of every neural network — they introduce non-linearity, decide which neurons fire, and directly shape a model's ability to learn complex patterns in tasks like image recognition, NLP, and chatbots.

Through six focused modules, Neural Genesis turns that theory into live simulations, interactive charts, and data-rich visualizations — all accessible from a sleek sidebar **Command Hub**.

---

## 🌐 Live Demo

<div align="center">

### 👉 [**Launch Neural Genesis**](https://activation-model-83tbjhtkdhhnpbry53kwxi.streamlit.app/)

*Runs live in your browser — no installation required.*

</div>

---

## 🚀 Features

### 🛰️ Mission Control
Central landing page with an "Activation Visualizer" hero section, full-brain neural imagery, strategic intel cards, and an overview of core non-linear concepts — ReLU, Swish, Sigmoid, and Softmax.

### 🧠 Neural Archive Dive
An AI-powered knowledge explorer for activation functions, covering advantages, disadvantages, and real-world use cases via an integrated **Select Function** dropdown with a live Sigmoid graph viewer. Includes applications in medical imaging, self-driving tech, satellite tracking, and NLP research.

### 🧪 Live Synaptic Lab
A real-time neuron simulator with interactive sliders for **Input (x)**, **Weight (w)**, and **Bias (b)**, a live activation function switcher (Sigmoid, ReLU, Tanh, and more), an instant output display, and real-time graph rendering.

### 🗺️ Neural Map — Data Architecture Flow
Explains structured data pipelines and AI/ML system architecture through an interactive **Synaptic Pulse Visualization** — a scatter/network graph covering cloud computing, big data, and AI data flow concepts.

### 📊 Matrix View — Topology Matrix
Side-by-side comparison cards for six activation functions, each with a rendered mathematical formula:

| Function | Range | Use Case |
|---|---|---|
| Sigmoid | (0, 1) | Binary Classification |
| ReLU | [0, ∞) | CNNs |
| Tanh | (-1, 1) | RNNs |
| Leaky ReLU | (-∞, ∞) | GANs |
| Softmax | [0, 1] | Object Detection |
| Swish | (-0.278, ∞) | EfficientNets |

### 📉 Gradient Flow Analytics
A visual explainer for backpropagation and gradient movement, featuring a layered diagram (Layer 1 → Layer 2 → Layer 3), a breakdown of the vanishing gradient problem versus the ReLU solution, and a side-by-side comparison of the Sigmoid and ReLU formulas.

---

## 🗂️ Module Navigation

| Module | Description |
|---|---|
| 🛰️ **Mission Control** | Home / hero dashboard |
| 🧠 **Neural Archive** | Archive dive + function explorer |
| 🧪 **Synaptic Lab** | Live neuron simulator |
| 🗺️ **Neural Map** | Data architecture flow |
| 📊 **Matrix View** | Topology matrix of functions |
| 📉 **Gradient Flow** | Backpropagation analytics |

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Frontend** | HTML, CSS, JavaScript / React |
| **Charts** | Plotly.js / Chart.js |
| **Math Rendering** | KaTeX / MathJax |
| **Design** | Dark UI — cyan (`#00FFFF`) & purple (`#A855F7`) accent palette |
| **Hosting** | Streamlit Cloud / Localhost (port 8501) |

---

## 📁 Project Structure

```
neural-genesis/
├── index.html
├── assets/
│   ├── images/              # AI-generated visuals
│   └── icons/
├── modules/
│   ├── mission-control/
│   ├── neural-archive/
│   ├── synaptic-lab/
│   ├── neural-map/
│   ├── matrix-view/
│   └── gradient-flow/
├── components/
│   ├── Sidebar.jsx
│   ├── ActivationChart.jsx
│   ├── SynapticSliders.jsx
│   └── TopologyCard.jsx
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites
- Node.js `v16+` (for the React/JS build)
- Python `3.9+` (only if running the Streamlit version)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/neural-genesis.git
cd neural-genesis
```

### 2. Install dependencies
```bash
npm install
```

### 3. Start the development server
```bash
npm start
```

### Or, run the Streamlit version
```bash
pip install -r requirements.txt
streamlit run app.py   # opens on http://localhost:8501
```

---

## 📊 Key Concepts Covered

- ✅ Activation Functions — Sigmoid, ReLU, Tanh, Leaky ReLU, Softmax, Swish
- ✅ Vanishing Gradient Problem
- ✅ Backpropagation & Gradient Flow
- ✅ Neural Network Layers & Architecture
- ✅ Data Architecture & AI Pipelines

---

## 🤖 Built With AI Tools

| Capability | Purpose |
|---|---|
| **AI Image Generation** | Neural brain visuals, gradient flow diagrams |
| **AI Content Writing** | Module descriptions, mathematical explanations |
| **AI Code Assistance** | Interactive components, chart rendering, slider logic |
| **Plotly / Chart.js** | Live graph rendering |
| **MathJax / KaTeX** | Mathematical formula display |

---

## 🧭 Roadmap

- [ ] Add more activation functions (GELU, Mish, ELU)
- [ ] Export simulator results as CSV/PNG
- [ ] Mobile-responsive Command Hub layout
- [ ] Dark/light theme toggle
- [ ] Guided tutorial mode for beginners

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution. See the `LICENSE` file for full terms.

---

## 💬 Support & Contact

Have a question, found a bug, or want to suggest a module?

| Channel | Link |
|---|---|
| 🐛 Report a Bug | [Open an Issue](https://github.com/yourusername/neural-genesis/issues) |
| 💡 Request a Feature | [Start a Discussion](https://github.com/yourusername/neural-genesis/discussions) |
| ⭐ Show Support | Star this repo if Neural Genesis helped you learn! |

---

## 🙌 Acknowledgments

| Contribution | Powered By |
|---|---|
| 🖼️ Visual Design & Imagery | AI-assisted image generation |
| ✍️ Content & Explanations | AI-assisted technical writing |
| 💻 Interactive Components | AI-assisted code generation |
| 📈 Data Visualization | Plotly.js, Chart.js |
| 🔢 Math Rendering | KaTeX, MathJax |

<div align="center">

<br>

<img src="https://img.shields.io/badge/Made_with-🧠_Neural_Genesis-1a1a2e?style=for-the-badge&labelColor=0a0a12&color=00FFFF" alt="Made with Neural Genesis"/>

### *"Making the mathematics of learning visible."*

<sub>⭐ If this project sparked an idea, consider giving it a star. ⭐</sub>

</div>
