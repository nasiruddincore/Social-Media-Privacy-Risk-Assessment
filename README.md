# 🛡️ Social Media Privacy Risk Assessment Framework

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

A defensive, privacy-focused cybersecurity framework designed to evaluate social-media exposure, account-security practices, social-engineering risk, and digital-footprint vulnerability using synthetic data and self-reported configuration audits.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [System Objectives](#-system-objectives)
- [Cybersecurity Relevance](#-cybersecurity-relevance)
- [Privacy vs Security](#-privacy-vs-security)
- [Key Features](#-key-features)
- [Risk Scoring Rubric](#-risk-scoring-rubric)
- [Privacy by Design Controls](#-privacy-by-design-controls)
- [Folder Structure](#-folder-structure)
- [Installation & Setup Guide](#-installation--setup-guide)
- [How to Run the Dashboard](#-how-to-run-the-dashboard)
- [Testing Strategy](#-testing-strategy)
- [Educational Disclaimer](#-educational-disclaimer)

---

## 📌 Project Overview
As online profiles become primary targets for threat actors conducting doxxing, impersonation, and social engineering, maintaining proper digital hygiene is vital. This platform provides a structured, repeatable assessment model that empowers users to audit their configuration settings, understand their exposure vectors, and apply targeted remediation steps.

## ⚠️ Problem Statement
* **Oversharing & Doxxing Risks:** Users frequently expose sensitive PII (phone numbers, full birth dates, real-time location check-ins) publicly without realizing the downstream security implications.
* **Account Compromise Vulnerabilities:** Weak authentication practices, disabled Multi-Factor Authentication (MFA), and unreviewed third-party application permissions leave accounts vulnerable to takeover.
* **Lack of Actionable Guidance:** Raw privacy settings menus on social platforms can be confusing, making it difficult for everyday users and job-seekers to know what to fix first.

## 🎯 System Objectives
1. **Self-Service Assessment:** Provide a comprehensive 40-question audit covering 10 distinct privacy and security categories.
2. **Algorithmic Risk Scoring:** Translate survey inputs into category scores and an overall 0–100 risk metric.
3. **Interactive Simulation:** Demonstrate the direct impact of security improvements via a live remediation simulator.
4. **Aggregate Telemetry Intelligence:** Visualize population-level vulnerability metrics using safe, synthetic datasets.

---

## 🏭 Cybersecurity Relevance
* **Governance, Risk & Compliance (GRC):** Mirrors organizational security posture assessments and data minimization audits.
* **Security Awareness Training:** Educates students, job-seekers, and employees on social engineering and digital footprint reduction.
* **Identity Protection & IAM:** Highlights the critical difference between account security controls and data privacy exposure.

---

## ⚖️ Privacy vs. Security
* **Privacy:** Controls how personal information is collected, exposed, shared, and used (e.g., hiding a phone number or disabling public location check-ins).
* **Security:** Protects systems and accounts from unauthorized access or misuse (e.g., enforcing strong unique passwords and authenticator-app MFA).
* *Key Takeaway:* An account can have strong security credentials (MFA enabled) while still exhibiting extreme privacy exposure (public personal details).

---

## ✨ Key Features
* **40+ Question Audit Survey:** Categorized evaluation spanning profile visibility, location tracking, tagging, and digital footprint.
* **Weighted Scoring Engine:** Mathematically weights categories (e.g., Personal Information and Account Security weighted higher) to produce accurate risk levels.
* **Interactive Risk Radar:** Visualizes category vulnerabilities using dynamic Plotly polar charts.
* **Remediation & Recommendation Engine:** Generates prioritized security fixes categorized into Immediate, Important, and Good Practice actions.
* **Privacy Improvement Simulator:** Allows users to toggle setting corrections and instantly view simulated score improvements.

---

## 📊 Risk Scoring Rubric
| Score Range | Risk Level | Description |
| :--- | :--- | :--- |
| **0 – 20** | `LOW` | Strong privacy hygiene; minimal public exposure. |
| **21 – 40** | `MODERATE` | Basic settings configured, but minor exposure points exist. |
| **41 – 70** | `HIGH` | Significant PII or location exposure; immediate review required. |
| **71 – 100** | `CRITICAL` | Severe exposure across multiple categories; high vulnerability to doxxing/takeover. |

---

## 🔒 Privacy by Design Controls
* **Data Minimization:** The application never requests, collects, or stores sensitive PII (no actual phone numbers, home addresses, or passwords).
* **Configuration Assessment Only:** Evaluates *posture states* (e.g., "Is your phone number public? Yes/No") rather than harvesting raw data.
* **Local Processing:** All risk calculations occur locally within the client runtime.

---

## 📂 Folder Structure
```text
Social-Media-Privacy-Risk-Assessment/
│
├── data/
│   ├── generate_dataset.py          # Synthetic dataset generator script
│   └── social_media_privacy_assessments.csv # Fictional assessment records for dashboard analytics
│
├── app.py                           # Core Streamlit application (Engine, UI, and Dashboard)
├── requirements.txt                 # Python project dependencies
├── .env.example                     # Environment variables configuration template
├── .gitignore                       # Git exclusion rules
└── README.md                        # Professional project documentation
