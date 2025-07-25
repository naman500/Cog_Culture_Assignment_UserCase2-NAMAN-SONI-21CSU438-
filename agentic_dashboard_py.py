# -*- coding: utf-8 -*-
"""Agentic_dashboard.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KYo3o2mPrHxhnVICgLCij9Tbm6FCm4i4
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %pip install -U langchain-anthropic langchain-core

import streamlit as st
import json
import smtplib
from email.message import EmailMessage
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate

# ---------------------------
# SETUP
# ---------------------------
st.set_page_config(page_title="Agentic Churn Email Assistant", layout="wide")
st.title("📧 HR Email Generator for High-Risk Employees                         By NAMAN SONI")
st.markdown("Upload Claude's churn decisions and auto-draft emails for high-risk cases.")

# Claude API key input
api_key = st.sidebar.text_input("🔐 Claude API Key", type="password")

# Default email (static for now)
DEFAULT_EMAIL = "abc@gmail.com"

# Claude model setup
if api_key:
    claude = ChatAnthropic(
        model="claude-3-haiku-20240307",
        temperature=0.3,
        max_tokens=1024,
        api_key=api_key
    )
else:
    st.warning("Please enter your Claude API key in the sidebar to proceed.")
    st.stop()

# ---------------------------
# Upload LLM Decision JSON
# ---------------------------
uploaded_file = st.file_uploader("📂 Upload churn_llm_decisions.json", type="json")

if uploaded_file:
    churn_data = json.load(uploaded_file)
    df = [d for d in churn_data if d["status"] == "HIGH RISK"]

    st.markdown(f"### Found {len(df)} HIGH RISK employee(s)")

    selected_ids = st.multiselect(
        "👤 Select Employees to Notify",
        options=[d["employee_id"] for d in df],
        format_func=lambda x: f"Employee #{x}"
    )

    if st.button("✉️ Draft and Send Emails"):
        for entry in df:
            if entry["employee_id"] not in selected_ids:
                continue

            employee_id = entry["employee_id"]
            summary = entry["summary"]
            actions = entry["recommended_actions"]

            # ---------------------------
            # Claude Prompt
            # ---------------------------
            prompt = PromptTemplate(
                input_variables=["summary", "actions"],
                template="""
You're an HR assistant AI. Based on the following summary and action plan for an employee, write a short, empathetic and professional email from the HR team requesting a 1:1 meeting.

Summary:
{summary}

Recommended Actions:
{actions}

Return only the email body in markdown format.
"""
            )

            # Run Claude model
            llm_input = {
                "summary": summary,
                "actions": "\n".join(actions)
            }

            try:
                email_body = claude.invoke(prompt.format(**llm_input)).content
            except Exception as e:
                st.error(f"Error generating email for Employee #{employee_id}: {e}")
                continue

            # ---------------------------
            # Preview the Email
            # ---------------------------
            with st.expander(f"📨 Email Preview for Employee #{employee_id}"):
                st.markdown(email_body)

            # ---------------------------
            # Simulate Sending Email
            # ---------------------------
            try:
                msg = EmailMessage()
                msg["Subject"] = f"[HR] Let's Connect — Employee #{employee_id}"
                msg["From"] = "hr@company.com"
                msg["To"] = DEFAULT_EMAIL
                msg.set_content(email_body, subtype="html")

                # Optional: SMTP setup (demo: print instead of sending)
                # smtp = smtplib.SMTP("smtp.example.com", 587)
                # smtp.starttls()
                # smtp.login("your_user", "your_pass")
                # smtp.send_message(msg)
                # smtp.quit()

                # For demo purposes, simulate sending
                st.success(f"✅ Email drafted and sent to {DEFAULT_EMAIL} for Employee #{employee_id}")

            except Exception as e:
                st.error(f"❌ Failed to send email for Employee #{employee_id}: {e}")
else:
    st.info("Please upload `churn_llm_decisions.json` to begin.")


#  streamlit run agentic_dashboard_py.py
#  Local URL: http://localhost:8501
