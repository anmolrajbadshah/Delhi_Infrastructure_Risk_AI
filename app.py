import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="Delhi Infrastructure Risk Dashboard",
    layout="wide"
)

st.title("🏙️ Delhi Infrastructure Risk & Flood Dashboard")
st.caption("ML-driven decision support for urban infrastructure prioritization")

# -----------------------------
# Load Data
# -----------------------------
DATA_PATH = "data/processed/infrastructure_priority_index.csv"

if not os.path.exists(DATA_PATH):
    st.error("Data not found. Run Notebooks 04–06 first.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

priority_filter = st.sidebar.multiselect(
    "Priority Level",
    options=["High", "Medium", "Low"],
    default=["High", "Medium", "Low"]
)

df_f = df[df["priority_level"].isin(priority_filter)]

top_pct = st.sidebar.slider(
    "Show Top Critical Assets (%)",
    min_value=1,
    max_value=20,
    value=5
)

# -----------------------------
# KPIs
# -----------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Assets", f"{len(df_f):,}")
c2.metric("High Priority", f"{(df_f['priority_level']=='High').sum():,}")
c3.metric("Avg Risk Score", f"{df_f['risk_score'].mean():.2f}")
c4.metric("Avg Flood Impact", f"{df_f['predicted_flood_impact'].mean():.2f}")

st.divider()

# -----------------------------
# Charts Row 1
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    fig_risk = px.histogram(
        df_f, x="risk_score", nbins=40,
        title="Risk Score Distribution",
        labels={"risk_score": "Risk Score"}
    )
    st.plotly_chart(fig_risk, use_container_width=True)

with col2:
    fig_flood = px.histogram(
        df_f, x="predicted_flood_impact", nbins=40,
        title="Flood Impact Distribution",
        labels={"predicted_flood_impact": "Flood Impact"}
    )
    st.plotly_chart(fig_flood, use_container_width=True)

# -----------------------------
# Charts Row 2
# -----------------------------
col3, col4 = st.columns(2)

with col3:
    fig_scatter = px.density_heatmap(
        df_f,
        x="risk_score",
        y="predicted_flood_impact",
        nbinsx=40,
        nbinsy=40,
        title="Risk–Flood Interaction Heatmap",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col4:
    fig_bar = px.histogram(
        df_f,
        x="priority_level",
        category_orders={"priority_level": ["High", "Medium", "Low"]},
        title="Priority Level Counts",
        color="priority_level"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# -----------------------------
# Top Critical Assets Table
# -----------------------------
st.subheader("🚨 Top Critical Assets")

top_n = int(len(df_f) * top_pct / 100)
top_df = df_f.sort_values("D_CIPI", ascending=False).head(top_n)

st.dataframe(
    top_df[
        ["asset_id", "D_CIPI", "priority_level", "risk_score", "predicted_flood_impact"]
    ],
    use_container_width=True
)
