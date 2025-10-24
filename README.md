# 🕸️ NeuroWeave AI  
**The Fusion of Collective Intelligence and Blockchain Trust**  
Where multi-agent reasoning meets decentralized proof — shaping explainable innovation for tomorrow.

---

## 🧠 Overview  
**NeuroWeave AI** is an AI-powered collaborative intelligence and explainability platform that blends multi-agent reasoning, blockchain validation, and transparent analytics.  
It enables teams to ideate collectively, visualize their reasoning through explainable AI graphs, and mint insights as NFTs — ensuring both **trust** and **traceability** in the innovation process.

This project was built as part of a **Hackathon 2025 Edition** submission — showcasing innovation, transparency, and enterprise-grade scalability.

---

## 🚀 Features  
- 🤖 **Collective Intelligence Simulation** — Multi-agent reasoning (Logic, Data, Empathy, Creative) collaborating on user prompts.  
- 🧩 **NeuroGraph Visualization** — Interactive, explainable graph showing concept overlaps, agent influence, and reasoning trace.  
- 💰 **AI Performance Dashboard** — Real-time system metrics with explainability, token efficiency, and downloadable PDF report.  
- 🪙 **NFT Minting Portal** — Instantly mint AI-generated insights as NFTs on the Celo blockchain with Pinata IPFS storage.  
- 💼 **Business Impact Analyzer** — AI-evaluated market potential, feasibility, innovation index, and ROI analysis.  
- 🌗 **Light/Dark Theme Responsive Design** — Works beautifully across both themes and mobile devices.  

---

## 🏗️ Tech Stack  

| Layer | Technologies |
|-------|---------------|
| **Frontend** | [Streamlit](https://streamlit.io) |
| **Backend Logic** | Python, OpenAI GPT-4o-mini |
| **Blockchain** | Celo (Alfajores Testnet) + Web3.py |
| **Storage** | IPFS via [Pinata API](https://pinata.cloud) |
| **Visualization** | NetworkX, PyVis, Matplotlib, Plotly |
| **AI Explainability** | OpenAI API, TF-IDF, Multi-agent simulation |

---

## 🧩 Architecture  

```text
┌───────────────────────────┐
│     User Interaction      │
│  (Streamlit Web App)      │
└────────────┬──────────────┘
             │
             ▼
┌───────────────────────────┐
│  Multi-Agent Reasoning    │
│  (Logic, Data, Empathy,   │
│   Creative via OpenAI)    │
└────────────┬──────────────┘
             │
             ▼
┌───────────────────────────┐
│  NeuroGraph Visualization │
│  (Explainable AI + XAI)   │
└────────────┬──────────────┘
             │
             ▼
┌───────────────────────────┐
│ Blockchain & NFT Minting  │
│ (Celo + Pinata IPFS)      │
└───────────────────────────┘
```text

## 🛠️ Installation
1️⃣ Clone the Repository

git clone https://github.com/<your-username>/NeuroWeave.git
cd NeuroWeave

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate     # on Windows
# or
source venv/bin/activate  # on macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

## 🔐 Environment Variables

Create a .env file in your root directory:

OPENAI_API_KEY="your-openai-api-key"
PINATA_API_KEY="your-pinata-api-key"
PINATA_SECRET_API_KEY="your-pinata-secret"
PRIVATE_KEY="your-celo-wallet-private-key"
CELO_RPC="https://alfajores-forno.celo-testnet.org"
CONTRACT_ADDRESS="your-deployed-contract-address"
CONTRACT_ABI_JSON="contract_abi.json"

▶️ Run the App
streamlit run app.py

Then open http://localhost:8501
 in your browser.

## 🧾 Key Modules
File	Description
app.py	Main Streamlit application integrating all features
modules/agents.py	Handles multi-agent reasoning and OpenAI API integration
modules/ipfs.py	Uploads data to Pinata (IPFS)
modules/nft.py	Handles blockchain minting logic on Celo
contracts/NeuroWeave.sol	Smart contract for NFT minting
contract_abi.json	Contract ABI file for Web3 interaction

## 📄 AI Explainability Highlights

Transparent Reasoning: Each AI agent’s contribution and overlap are visible.

Explainability Dashboard: Quantitative performance metrics — coherence, diversity, reasoning depth.

Downloadable Reports: Professionally styled PDF generation with project logo and timeline trace.

## 🏆 Hackathon Highlights

🏅 Best AI Explainability
💫 Grand Prize Contender
🚀 Most Innovative Integration

## 💡 Why NeuroWeave Deserves to Win

NeuroWeave redefines transparency in AI — merging collective reasoning, explainable insights, and blockchain validation.
It stands out for its clarity, innovation, and storytelling that resonates with both judges and enterprise audiences.

## 🧑‍💻 Author

👨‍💻 Mohamed Farhun M
Hackathon Builder | AI × Blockchain Innovator

## ⭐ Show your support

If you liked this project, please give it a ⭐ on GitHub — it helps showcase hackathon innovation and inspires others!
