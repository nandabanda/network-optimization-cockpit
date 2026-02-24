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
    page_title="SYDIAI | Diagnose Root Cause Studio",
    page_icon="🧪",
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
    min-height: 120px;
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

.kpi-delta-red {
    font-size: 1.0rem;
    color: #fb7185;
    font-weight: 900;
    margin-top: 10px;
}

.kpi-delta-green {
    font-size: 1.0rem;
    color: #34d399;
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
        <div class="subtitle">Diagnose | Root Cause Decomposition Studio</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.selectbox("Scenario", ["Baseline (Current)", "Optimized Network", "Demand Spike Scenario", "Capacity Constraint Scenario"])
    st.selectbox("Root Cause Lens", ["All", "Service Loss", "Cost Leakage", "Inventory Leakage", "Capacity Bottleneck"])
    st.caption(f"Last refreshed: {datetime.now().strftime('%d %b %Y | %I:%M %p')}")

st.markdown('<div class="hr-line"></div>', unsafe_allow_html=True)


# -----------------------------
# TOP KPI STRIP
# -----------------------------
k1, k2, k3, k4, k5 = st.columns(5)

k1.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Top Root Cause</div>
    <div class="kpi-value">Capacity</div>
    <div class="kpi-delta-red">Depot overload</div>
</div>
""", unsafe_allow_html=True)

k2.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Service Loss Value</div>
    <div class="kpi-value">₹ 92 Cr</div>
    <div class="kpi-delta-red">Critical risk</div>
</div>
""", unsafe_allow_html=True)

k3.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Cost Leakage</div>
    <div class="kpi-value">₹ 78 Cr</div>
    <div class="kpi-delta-red">Premium freight</div>
</div>
""", unsafe_allow_html=True)

k4.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Inventory Leakage</div>
    <div class="kpi-value">₹ 64 Cr</div>
    <div class="kpi-delta-red">SLOB build-up</div>
</div>
""", unsafe_allow_html=True)

k5.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Actionable Levers</div>
    <div class="kpi-value">11</div>
    <div class="kpi-delta-green">Optimization ready</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# ROOT CAUSE TREE (SIMULATED)
# -----------------------------
st.markdown('<div class="section-title">Root Cause Decomposition</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Breakdown of service loss and cost leakage into primary operational drivers.</div>', unsafe_allow_html=True)

np.random.seed(11)

df_root = pd.DataFrame({
    "Driver": [
        "Depot Capacity Overload",
        "Lane Overload (Plant B → Depot W)",
        "Demand Spike (East)",
        "Batch Size / MOQ Constraints",
        "Inventory Misallocation",
        "Poor Forecast Accuracy",
        "SKU Complexity (Long Tail)"
    ],
    "Contribution %": [24, 18, 15, 12, 11, 9, 11],
    "Impact (Cr)": [92, 78, 58, 45, 41, 33, 39],
    "Signal Strength": ["Very High", "High", "High", "Medium", "Medium", "Medium", "High"]
})

fig = px.bar(
    df_root.sort_values("Contribution %", ascending=True),
    x="Contribution %",
    y="Driver",
    orientation="h",
    text="Contribution %",
    title="Root Cause Contribution Breakdown"
)

fig.update_layout(height=480)

st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# ROOT CAUSE DRILLDOWN TABLE
# -----------------------------
st.markdown('<div class="section-title">Root Cause Drilldown Table</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Detailed drilldown across depots, lanes and SKU clusters causing the leakage.</div>', unsafe_allow_html=True)

df_drill = pd.DataFrame({
    "Entity": [
        "Depot W", "Depot W", "Plant B → Depot W",
        "Depot C", "Depot N", "East Region"
    ],
    "Issue": [
        "Capacity Utilization 97%",
        "Inbound congestion",
        "Rail lane overload",
        "Slow movers accumulation",
        "Stock-out risk (Top 20 SKUs)",
        "Demand spike (+18%)"
    ],
    "Root Cause": [
        "Depot capacity planning gap",
        "Dispatch schedule misalignment",
        "Sourcing imbalance",
        "SKU proliferation",
        "Allocation mis-prioritization",
        "Forecast lag"
    ],
    "Impact (Cr)": [92, 41, 78, 64, 58, 45],
    "Severity": ["Critical", "High", "Critical", "High", "High", "High"]
})

left, right = st.columns([2, 1])

with left:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Drilldown View")
    st.dataframe(df_drill, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("System Diagnosis Summary")

    st.markdown('<div class="badge-red">PRIMARY ROOT CAUSE</div>', unsafe_allow_html=True)
    st.write("**Depot W overload** is the top driver impacting service + cost-to-serve.")

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="badge">SECONDARY DRIVERS</div>', unsafe_allow_html=True)
    st.write("""
    - Lane imbalance Plant B → Depot W  
    - SKU long-tail build-up in Depot C  
    - Forecast lag in East demand spike  
    """)

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="badge">NEXT SYSTEM STEP</div>', unsafe_allow_html=True)
    st.write("Run Optimization Solver for sourcing + replenishment shifts.")

    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# LEVER RECOMMENDATION PANEL
# -----------------------------
st.markdown('<div class="section-title">Optimization Lever Recommendations</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">System-generated levers to remove bottlenecks and recover cost + service leakage.</div>', unsafe_allow_html=True)

df_levers = pd.DataFrame({
    "Lever": [
        "Shift sourcing from Depot W → Depot C",
        "Enable depot-to-depot replenishment",
        "Convert lane Plant B → Depot W to rail priority",
        "Reduce safety stock for long tail SKUs",
        "Trigger SKU rationalization for bottom 5% movers",
        "Reduce MOQ / batch size for Diet cluster"
    ],
    "Benefit Type": ["Cost + Service", "Service", "Cost", "Working Capital", "Complexity", "Expiry Risk"],
    "Expected Benefit (Cr)": [62, 28, 31, 45, 55, 34],
    "Execution Priority": ["Immediate", "Immediate", "High", "High", "High", "Medium"]
})

st.markdown('<div class="panel-card">', unsafe_allow_html=True)
st.dataframe(df_levers, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")
st.caption("SYDIAI | Diagnose Root Cause Decomposition Studio | Supply Chain Decision Intelligence System")
