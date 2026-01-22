🏙️ ML-Based Urban Road Infrastructure Risk & Flood Impact Analysis (Delhi NCR)
📌 Project Overview

Urban road infrastructure in large metropolitan regions is highly vulnerable to structural aging, traffic stress, poor maintenance, and flooding.
This project presents an end-to-end Machine Learning–driven decision support system that evaluates road infrastructure risk, estimates flood impact severity, and prioritizes assets for maintenance and disaster-resilience planning.

The system is designed as a city-scale analytical pipeline, culminating in an interactive dashboard for decision-makers.

🎯 Objectives

Assess infrastructure failure risk at the road/flyover level

Predict flood impact severity on urban road assets

Combine multiple risk dimensions into a single priority index

Enable data-driven maintenance and disaster preparedness decisions

🧠 System Architecture
Feature Engineering
        ↓
Risk Classification Model
        ↓
Flood Impact Severity Model
        ↓
Composite Priority Index (D-CIPI)
        ↓
Interactive Dashboard (Streamlit)

📊 Feature Engineering

Due to the lack of publicly available asset-level failure and flood damage labels, the project uses statistically realistic synthetic data to demonstrate the full analytical pipeline.

Engineered Features
Feature	Description
SAI	Structural Age Index
TSI	Traffic Stress Index
FEI	Flood Exposure Index
MNS	Maintenance Neglect Score
CDI	Citizen Distress Index
is_flyover	Binary indicator for flyover assets

All features are normalized to 0–1 for comparability and modeling stability.

🤖 Machine Learning Models
1️⃣ Infrastructure Risk Classification

Model: Random Forest Classifier

Output: Risk category — Low / Medium / High

Purpose: Identify assets with higher probability of failure

2️⃣ Flood Impact Severity Prediction

Model: Random Forest Regressor

Output: Continuous flood impact score (0–1)

Purpose: Estimate disruption severity during flooding events

Both models are explainable, policy-friendly, and robust to noisy inputs.

🧮 Composite Priority Index (D-CIPI)

To support actionable decision-making, a Delhi Critical Infrastructure Priority Index (D-CIPI) was developed.

D-CIPI Formula (Conceptual)
D-CIPI = 
  0.40 × Failure Risk
+ 0.30 × Flood Impact
+ 0.20 × Maintenance Neglect
+ 0.10 × Traffic Stress

Priority Levels

High → Immediate intervention required

Medium → Planned maintenance

Low → Monitoring only

This index enables transparent ranking of assets for budget allocation and resilience planning.

📈 Visual Analytics & Dashboard

An interactive Streamlit dashboard was developed to present:

Risk and flood impact distributions

Risk–flood interaction heatmaps

Priority-level summaries

Ranked lists of critical infrastructure assets

The dashboard converts ML outputs into decision-ready insights.

🛠️ Tech Stack

Programming: Python

Data Analysis: Pandas, NumPy

Machine Learning: Scikit-learn (Random Forest)

Visualization: Plotly, Matplotlib, Seaborn

Dashboard: Streamlit

Version Control: Git, GitHub

📂 Project Structure
Delhi_Infrastructure_Risk_AI/
│
├── app.py                     # Streamlit dashboard
├── requirements.txt
│
├── data/
│   └── processed/
│       ├── engineered_features.csv
│       ├── risk_predictions.csv
│       ├── flood_impact_predictions.csv
│       └── infrastructure_priority_index.csv
│
├── models/
│   ├── risk_model.pkl
│   └── flood_impact_model.pkl
│
└── notebooks/
    ├── 03_feature_engineering.ipynb
    ├── 04_risk_modelling.ipynb
    ├── 05_flood_impact_model.ipynb
    ├── 06_priority_index_dcpi.ipynb
    └── 07_risk_flood_heatmaps.ipynb

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Dashboard
streamlit run app.py

🧠 Key Learnings & Insights

End-to-end ML systems are more valuable than standalone models

Explainability is critical for policy and infrastructure use cases

Composite indices bridge the gap between ML outputs and real-world decisions

Synthetic data can effectively demonstrate complex analytical pipelines when real labels are unavailable

📌 Use Cases

Urban infrastructure maintenance planning

Disaster resilience and flood preparedness

Smart city analytics

Policy-driven decision support systems

⚠️ Disclaimer

This project uses synthetic but statistically realistic data to demonstrate methodology and system design.
The framework is extensible to real-world datasets when asset-level observations become available.

👤 Author

Anmol Raj Badshah
Machine Learning & Data Science Practitioner
