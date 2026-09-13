<div align="center">

# Neural Genesis

**An interactive platform for exploring neural network activation functions, live neuron simulations, and gradient flow analytics.**

[![Status](https://img.shields.io/badge/status-active-2ea44f?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](#)
[![Modules](https://img.shields.io/badge/modules-6-6f42c1?style=flat-square)](#module-navigation)
[![AI Assisted](https://img.shields.io/badge/AI--assisted-yes-0891b2?style=flat-square)](#built-with-ai-tools)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](#contributing)

[**Live Demo**](https://activation-model-83tbjhtkdhhnpbry53kwxi.streamlit.app/) · [Features](#features) · [Getting Started](#getting-started) · [Contributing](#contributing)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Module Navigation](#module-navigation)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Key Concepts Covered](#key-concepts-covered)
- [Built With AI Tools](#built-with-ai-tools)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Neural Genesis** is a dark-themed, interactive learning platform for visualizing and understanding the core concepts behind neural networks and deep learning.

Activation functions are the mathematical heart of every neural network — they introduce non-linearity, determine which neurons fire, and directly shape a model's ability to learn complex patterns in tasks like image recognition, natural language processing, and conversational AI.

Through six focused modules, Neural Genesis turns theory into live simulations, interactive charts, and data-rich visualizations, all accessible from a unified sidebar navigation hub.

| Module | Purpose |
|---|---|
| **Mission Control** | Central hero dashboard |
| **Neural Archive** | AI-powered activation function explorer |
| **Synaptic Lab** | Live neuron simulator |
| **Gradient Flow** | Backpropagation analytics |

---

## Features

### Explore & Learn

**Mission Control**
The landing page, featuring an activation function visualizer, neural network imagery, and a curated overview of the core non-linearity concepts: ReLU, Swish, Sigmoid, and Softmax.

**Neural Archive**
A guided knowledge explorer covering the advantages, disadvantages, and real-world applications of each activation function, paired with a live function selector and graph viewer. Includes use cases in medical imaging, autonomous vehicles, satellite tracking, and NLP research.

**Neural Map**
An explainer on structured data pipelines and ML system architecture, visualized through an interactive network graph covering cloud computing, big data, and end-to-end AI data flow.

### Simulate & Compare

**Synaptic Lab**
A real-time neuron simulator with interactive controls for input, weight, and bias, a live activation function switcher (Sigmoid, ReLU, Tanh, and more), and instant graph rendering of the resulting output.

**Matrix View**
Side-by-side comparison cards for six activation functions, each with its rendered mathematical formula for quick reference.

**Gradient Flow Analytics**
A visual walkthrough of backpropagation and gradient movement across network layers, including a breakdown of the vanishing gradient problem and how ReLU addresses it, with a direct comparison of the Sigmoid and ReLU formulas.

### Activation Function Reference

| Function | Range | Common Use Case |
|---|:---:|---|
| Sigmoid | (0, 1) | Binary classification |
| ReLU | [0, ∞) | Convolutional neural networks |
| Tanh | (-1, 1) | Recurrent neural networks |
| Leaky ReLU | (-∞, ∞) | Generative adversarial networks |
| Softmax | [0, 1] | Object detection |
| Swish | (-0.278, ∞) | EfficientNet architectures |

---

## Module Navigation

| Module | Description |
|---|---|
| Mission Control | Home and hero dashboard |
| Neural Archive | Function explorer and reference archive |
| Synaptic Lab | Live neuron simulator |
| Neural Map | Data architecture and pipeline flow |
| Matrix View | Topology comparison of activation functions |
| Gradient Flow | Backpropagation analytics |

---

## Tech Stack

| Category | Technologies |
|---|---|
| Frontend | HTML, CSS, JavaScript / React |
| Charts | Plotly.js / Chart.js |
| Math Rendering | KaTeX / MathJax |
| Design | Dark UI with cyan and purple accents |
| Hosting | Streamlit Cloud / Localhost (port 8501) |

---

## Project Structure

```
neural-genesis/
├── index.html
├── assets/
│   ├── images/              # Visual assets
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

| Path | Responsibility |
|---|---|
| `index.html` | Application entry point |
| `assets/` | Imagery and icons |
| `modules/` | One folder per navigation module |
| `components/` | Reusable UI components (sidebar, charts, sliders, cards) |

---

## Getting Started

### Prerequisites

- Node.js v16 or higher (for the React/JS build)
- Python 3.9 or higher (only if running the Streamlit version)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/neural-genesis.git
cd neural-genesis
```

**2. Install dependencies**
```bash
npm install
```

**3. Start the development server**
```bash
npm start
```

**Or, run the Streamlit version**
```bash
pip install -r requirements.txt
streamlit run app.py   # opens on http://localhost:8501
```

---

## Key Concepts Covered

- Activation functions: Sigmoid, ReLU, Tanh, Leaky ReLU, Softmax, Swish
- The vanishing gradient problem
- Backpropagation and gradient flow
- Neural network layers and architecture
- Data architecture and AI pipelines

---

## Built With AI Tools

| Capability | Purpose |
|---|---|
| AI Image Generation | Neural network visuals and diagrams |
| AI Content Writing | Module descriptions and mathematical explanations |
| AI Code Assistance | Interactive components, chart rendering, slider logic |
| Plotly / Chart.js | Live graph rendering |
| MathJax / KaTeX | Mathematical formula display |

---

## Roadmap

- [ ] Add more activation functions (GELU, Mish, ELU)
- [ ] Export simulator results as CSV/PNG
- [ ] Mobile-responsive layout
- [ ] Dark/light theme toggle
- [ ] Guided tutorial mode for beginners

---

## Contributing

Contributions are welcome. To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License — free to use, modify, and distribute with attribution. See the `LICENSE` file for full terms.

<div align="center">

<sub>If this project sparked an idea, consider giving it a star.</sub>

</div>
