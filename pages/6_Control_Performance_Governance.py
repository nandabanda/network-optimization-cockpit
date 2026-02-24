import streamlit as st

# --- SYDIAI Brand Header (auto-injected) ---
st.markdown(
    """
    <style>
        html, body, [class*="css"] { font-size: 150% !important; }
    </style>
    """,
    unsafe_allow_html=True
)

c_logo, c_title = st.columns([1, 6], vertical_alignment="center")
with c_logo:
    st.image("assets/sydiai_logo.png", width=140)
with c_title:
    st.markdown("## SYDIAI Network Optimization")
    st.caption("Enabling Purpose with Precision.")
# --- end brand header ---


import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="SYDIAI | Control Performance & Governance",
    page_icon="🎛️",
    layout="wide"
)

# -----------------------------
# PREMIUM THEME CSS
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #f6f7fb;
}

.block-container {
    padding-top: 1.1rem;
    padding-bottom: 2rem;
}

.header-bar {
    background: white;
    border-radius: 18px;
    padding: 16px 20px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.06);
    margin-bottom: 12px;
}

.logo {
    font-size: 2.05rem;
    font-weight: 900;
    color: #06152b;
    letter-spacing: 0.5px;
}

.logo span {
    color: #2563eb;
}

.subtitle {
    font-size: 1.1rem;
    font-weight: 800;
    color: #64748b;
    margin-top: 3px;
}

.hr-line {
    height: 2px;
    background: linear-gradient(90deg, rgba(37,99,235,0.85), rgba(6,21,43,0.12));
    border-radius: 999px;
    margin-top: 14px;
    margin-bottom: 18px;
}

.section-title {
    font-size: 1.55rem;
    font-weight: 900;
    margin-top: 1.8rem;
    margin-bottom: 0.4rem;
    color: #06152b;
}

.section-sub {
    font-size: 1.05rem;
    font-weight: 750;
    color: #64748b;
    margin-bottom: 1.2rem;
}

.panel-card {
    background: white;
    border-radius: 22px;
    padding: 16px 18px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0px 12px 25px rgba(0,0,0,0.06);
}

.kpi-card {
    background: linear-gradient(135deg, #06152b, #020812);
    padding: 22px;
    border-radius: 22px;
    border: 1px solid rgba(56,189,248,0.18);
    box-shadow: 0px 14px 32px rgba(0,0,0,0.30);
    min-height: 125px;
}

.kpi-label {
    font-size: 1.05rem;
    color: rgba(255,255,255,0.65);
    font-weight: 800;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 2.2rem;
    font-weight: 900;
    color: white;
    line-height: 1.1;
}

.kpi-delta-green {
    font-size: 1.0rem;
    color: #34d399;
    font-weight: 900;
    margin-top: 10px;
}

.kpi-delta-red {
    font-size: 1.0rem;
    color: #fb7185;
    font-weight: 900;
    margin-top: 10px;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(37,99,235,0.10);
    color: #2563eb;
    font-weight: 900;
    font-size: 0.9rem;
}

.badge-green {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(16,185,129,0.12);
    color: #059669;
    font-weight: 900;
    font-size: 0.9rem;
}

.badge-red {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(244,63,94,0.10);
    color: #e11d48;
    font-weight: 900;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------
c1, c2 = st.columns([3, 2])

with c1:
    st.markdown("""
    <div class="header-bar">
        <div class="logo">SYD<span>IAI</span></div>
        <div class="subtitle">Control | Performance & Governance</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.selectbox("Control Horizon", ["Last 7 Days", "Last 30 Days", "Quarter to Date"])
    st.selectbox("KPI Lens", ["All KPIs", "Service", "Cost", "Inventory", "Network Utilization"])
    st.caption(f"Last refreshed: {datetime.now().strftime('%d %b %Y | %I:%M %p')}")

st.markdown('<div class="hr-line"></div>', unsafe_allow_html=True)


# -----------------------------
# KPI STRIP
# -----------------------------
k1, k2, k3, k4, k5 = st.columns(5)

k1.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Plan Adherence</div>
    <div class="kpi-value">91%</div>
    <div class="kpi-delta-green">Stable</div>
</div>
""", unsafe_allow_html=True)

k2.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Service Achievement</div>
    <div class="kpi-value">95.8%</div>
    <div class="kpi-delta-green">+2.6 pts</div>
</div>
""", unsafe_allow_html=True)

k3.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Cost Variance</div>
    <div class="kpi-value">+1.9%</div>
    <div class="kpi-delta-red">Fuel + freight</div>
</div>
""", unsafe_allow_html=True)

k4.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Inventory Deviation</div>
    <div class="kpi-value">+6.2%</div>
    <div class="kpi-delta-red">Overstock pockets</div>
</div>
""", unsafe_allow_html=True)

k5.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Exception Closures</div>
    <div class="kpi-value">82%</div>
    <div class="kpi-delta-green">Improving</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# PERFORMANCE TREND (SIMULATED)
# -----------------------------
st.markdown('<div class="section-title">Performance Trends</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Plan vs Actual tracking across cost, service, inventory and network utilization.</div>', unsafe_allow_html=True)

np.random.seed(99)
days = pd.date_range(end=datetime.today(), periods=14)

df_trend = pd.DataFrame({
    "Date": days,
    "Service Level %": np.random.normal(95.5, 0.8, 14).round(2),
    "Cost Variance %": np.random.normal(2.0, 0.6, 14).round(2),
    "Inventory Variance %": np.random.normal(5.5, 1.2, 14).round(2),
    "Plan Adherence %": np.random.normal(90, 2.5, 14).round(2)
})

col1, col2 = st.columns(2)

with col1:
    fig_service = px.line(df_trend, x="Date", y="Service Level %", title="Service Level Trend")
    fig_service.update_layout(height=420)
    st.plotly_chart(fig_service, use_container_width=True)

with col2:
    fig_adherence = px.line(df_trend, x="Date", y="Plan Adherence %", title="Plan Adherence Trend")
    fig_adherence.update_layout(height=420)
    st.plotly_chart(fig_adherence, use_container_width=True)


col3, col4 = st.columns(2)

with col3:
    fig_cost = px.line(df_trend, x="Date", y="Cost Variance %", title="Cost Variance Trend")
    fig_cost.update_layout(height=420)
    st.plotly_chart(fig_cost, use_container_width=True)

with col4:
    fig_inv = px.line(df_trend, x="Date", y="Inventory Variance %", title="Inventory Variance Trend")
    fig_inv.update_layout(height=420)
    st.plotly_chart(fig_inv, use_container_width=True)


# -----------------------------
# GOVERNANCE TABLE
# -----------------------------
st.markdown('<div class="section-title">Governance Scorecard</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Weekly governance scorecard tracking execution performance and closure of exceptions.</div>', unsafe_allow_html=True)

df_scorecard = pd.DataFrame({
    "Governance Metric": [
        "Plan Adherence",
        "Dispatch Compliance",
        "Exception Closure Rate",
        "Depot Utilization Stability",
        "Stock-out Avoidance",
        "Expiry Risk Reduction",
        "Premium Freight Control"
    ],
    "Target": ["95%", "98%", "90%", "Stable", "Zero", "-15%", "Below ₹10 Cr"],
    "Actual": ["91%", "94%", "82%", "Medium Variance", "2 incidents", "-8%", "₹12 Cr"],
    "Status": ["Amber", "Amber", "Red", "Amber", "Red", "Amber", "Amber"]
})

st.markdown('<div class="panel-card">', unsafe_allow_html=True)
st.dataframe(df_scorecard, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# EXCEPTION CONTROL TOWER
# -----------------------------
st.markdown('<div class="section-title">Exception Control Tower</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Open exceptions requiring governance intervention and ownership escalation.</div>', unsafe_allow_html=True)

df_exceptions = pd.DataFrame({
    "Exception": [
        "Depot W overload persists",
        "Expiry risk in Diet cluster",
        "Premium freight triggered (East)",
        "Stock-out incident in North",
        "Rail delay disruption (Plant B lane)"
    ],
    "Severity": ["Critical", "Critical", "High", "High", "Medium"],
    "Owner": ["Supply Planning", "Inventory Control", "Logistics", "Demand Planning", "Transport Ops"],
    "Open Since": ["6 days", "12 days", "4 days", "2 days", "3 days"],
    "Recommended Governance Action": [
        "Escalate sourcing rebalancing",
        "Trigger liquidation + reduce MOQ",
        "Review alternate depot routing",
        "Reallocate buffer inventory",
        "Approve fallback mode shift"
    ]
})

left, right = st.columns([2, 1])

with left:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Open Exception Register")
    st.dataframe(df_exceptions, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Governance Actions")

    st.markdown('<div class="badge-red">ESCALATION REQUIRED</div>', unsafe_allow_html=True)
    st.write("2 critical exceptions are open beyond acceptable SLA window.")

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="badge">GOVERNANCE LOOP</div>', unsafe_allow_html=True)
    st.write("""
    - Review deviation cause  
    - Re-optimize scenario  
    - Approve dispatch overrides  
    - Close exceptions  
    """)

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="badge-green">SYSTEM READY</div>', unsafe_allow_html=True)
    st.write("Optimization rerun can be triggered for new constraints.")

    st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")
st.caption("SYDIAI | Control Performance & Governance | Supply Chain Decision Intelligence System")
