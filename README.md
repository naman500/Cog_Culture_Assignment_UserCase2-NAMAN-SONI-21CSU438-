# Agentic HR Churn Risk Dashboard

**By Naman Soni**

# Google_Drive Link : **https://drive.google.com/drive/folders/1ytjsAox5tX1_gHPpv5Jq52y6PL_r1heT?usp=drive_link**

## Problem Statement : **USE CASE 2: Predictive Model + Actionable Agent for Project Risk

Scenario: You build a predictive model for project delays or employee churn, and wrap it with a recommendation agent that advises HR/PMs on what to do next.

Tasks:

Train ML model using real-world dataset (Kaggle/HuggingFace)

Predict: Who is at risk?

Wrap in agent logic that:

Interprets result

Recommends action (e.g., assign mentor, reduce workload)

Notifies user (Slack/email logic)

Deliverables:

Python Notebook + Dashboard mockup

Output recommendations

Short explainer on agent flow

Bonus: Decision tree or LLM-based reasoner

Agentic Element: Predict Interpret Recommend Notify - full Al decision loop.

Final Deliverables (CHOOSE ANY ONE USE CASE)

Item

Description

Code

Collab link or GitHub repo with README

Agent Flow Diagram

PNG or draw.io or Figma diagram

Explanation (PDF/Slides)

One-pager explaining agent use case & impact

Output Screenshots

Sample inputs/outputs of the agent

(Optional) Demo Video

Phone/Screen-recorded demo

**Tools Allowed but not limited feel free to choose others:

Python (LangChain, ChromaDB, FAISS, OpenAl/Claude/Gemini APIs)

Speech: Whisper / Google Speech-to-Text

SQL (for bonus tasks / embedded search layer)

Streamlit/Gradio / FastAPI for simple frontends

AutoGPT/ CrewAl/ LangGraph (for advanced submissions)

Visualization: Notion, Figma, Canva, Mermaid

Google Drive /GitHub link with: [While Sharing pls make it accessible]

Code

How to Submit:

Architecture

Demo/video if any**

## Overview

This project is an end-to-end HR analytics and intervention system that:
- Predicts employee churn risk using machine learning.
- Uses a Large Language Model (Claude via LangChain) to generate human-readable risk assessments and recommended HR actions.
- Provides a Streamlit dashboard for HR to review high-risk cases and auto-draft empathetic emails for intervention.

---

## Folder Structure

```
.
├── agentic_dashboard_py.py           # Streamlit dashboard for HR email generation
├── Agent(llm_recommender).ipynb     # Notebook: LLM-based risk assessment
├── Main_Notebook.ipynb              # Notebook: ML pipeline for churn prediction
├── churn_predictions.json            # ML model predictions (input to LLM)
├── churn_llm_decisions.json          # LLM risk assessments (input to dashboard)
└── data/
    └── employee_churn.csv           # Main employee dataset
```

---

## Workflow

1. **Data Science & Prediction**
   - Clean and process employee data in `Main_Notebook.ipynb`.
   - Train and evaluate a churn prediction model (Random Forest, Gradient Boosting, etc.).
   - Export predictions to `churn_predictions.json`.

2. **LLM Risk Assessment**
   - Use `Agent(llm_recommender).ipynb` to convert predictions into structured, human-readable risk assessments and recommended actions using Claude.
   - Output is saved as `churn_llm_decisions.json`.

3. **HR Dashboard & Email Generation**
   - Run `agentic_dashboard_py.py` with Streamlit.
   - Upload `churn_llm_decisions.json`.
   - Select high-risk employees and auto-draft professional, empathetic HR emails for intervention.

---

## Setup

1. **Install dependencies**
   ```bash
   pip install streamlit langchain-anthropic langchain-core
   ```

2. **(Optional) Set up a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Get a Claude API key**
   - Sign up at [Anthropic](https://www.anthropic.com/) and obtain your API key.

---

## Usage

### 1. Run the Dashboard

```bash
streamlit run agentic_dashboard_py.py
```

- Open the local URL shown in your terminal (usually http://localhost:8501).
- Enter your Claude API key in the sidebar.
- Upload `churn_llm_decisions.json`.
- Select employees and draft/send emails.

### 2. Generate LLM Decisions (if needed)

- Run `Main_Notebook.ipynb` to generate `churn_predictions.json`.
- Run `Agent(llm_recommender).ipynb` to generate `churn_llm_decisions.json` from predictions.

---

## Data

- **`data/employee_churn.csv`**  
  Columns: `avg_monthly_hrs`, `department`, `filed_complaint`, `last_evaluation`, `n_projects`, `recently_promoted`, `salary`, `satisfaction`, `status`, `tenure`

- **`churn_predictions.json`**  
  Example:
  ```json
  {
    "prediction": "Left",
    "churn_probability": 1.0,
    "features": {
      "avg_monthly_hrs": 135,
      "filed_complaint": 0.0,
      ...
    }
  }
  ```

- **`churn_llm_decisions.json`**  
  Example:
  ```json
  {
    "employee_id": 0,
    "status": "HIGH RISK",
    "reasons": ["Low satisfaction score (0.45)", ...],
    "recommended_actions": ["Schedule immediate manager check-in...", ...],
    "summary": "Employee shows multiple risk factors including low satisfaction..."
  }
  ```

---

## Notes

- The dashboard simulates email sending for demo purposes. To enable real email sending, configure the SMTP section in `agentic_dashboard_py.py`.
- The LLM notebook currently uses a hardcoded API key for Claude. For production, use environment variables or secure input.
- All code is for educational/demo use and should be adapted for production security and privacy.

---

## Author

- **Name:** Naman Soni
- **Email:** naman21csu438@ncuindia.edu
- **Mobile:** 9166157517

---

## License

MIT License 
