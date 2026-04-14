# PharmaGuard: Pharmacogenomic Risk Prediction System

PharmaGuard is an AI-powered web application built for the **RIFT 2026 Hackathon**. It analyzes authentic patient VCF (Variant Call Format) files to predict personalized drug risks based on key pharmacogenomic genes (CYP2D6, CYP2C19, CYP2C9, SLCO1B1, TPMT, DPYD) aligning strictly with CPIC clinical guidelines.

## 🚀 Features
- **VCF Parsing:** A memory-optimized, streaming Python parser capable of identifying specific STAR alleles from raw `.vcf` or `.vcf.gz` files securely in-memory.
- **Explainable AI UI:** A dynamic React + Vite dashboard utilizing a custom "clinical-glassmorphism" design system to render Pharmacokinetic (PK) curves and Risk Triage alerts natively.
- **Workflow & Equity Tools:** Instantly generates FHIR-style Clinical Notes for EHR insertion, and mitigates treatment bias by actively surfacing Demographic/Ancestry warnings against "one-size-fits-all" prescribing.

---

## 🛠️ Tech Stack
- **Frontend:** React, Vite, React-Router, Recharts, Lucide Icons, Vanilla CSS
- **Backend:** Python, FastAPI, Uvicorn (Regex streaming parser)

## 💻 Local Setup Instructions

### 1. Start the Backend API (Python)
Ensure Python 3 is installed.
```bash
cd pharmaguard-backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```
The API documentation will mount automatically at `http://127.0.0.1:8000/docs`.

### 2. Start the Frontend Dashboard (React Node)
Ensure Node.js is installed. Open a *secondary* terminal:
```bash
cd pharmaguard-app
npm install
npm run dev
```
Access the application interface at `http://localhost:5173`.

---

## 📹 Hackathon Deliverables (Placeholders)
- **Live Demo URL:** [Insert Vercel/Render Link Here]
- **Video Walkthrough:** [Insert LinkedIn Video Link Here]

*This project was developed to mitigate adverse drug reactions through transparent, accessible, and deeply integrated precision medicine.*
