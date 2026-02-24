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
from datetime import datetime, timedelta

st.set_page_config(
    page_title="SYDIAI | Execute Dispatch Plan",
    page_icon="🚚",
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
        <div class="subtitle">Execute | Dispatch & Replenishment Plan</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.selectbox("Execution Horizon", ["Next 7 Days", "Next 14 Days", "Next 30 Days"])
    st.selectbox("Dispatch Mode", ["Optimized Dispatch", "Manual Override", "Exception-Only Dispatch"])
    st.caption(f"Last refreshed: {datetime.now().strftime('%d %b %Y | %I:%M %p')}")

st.markdown('<div class="hr-line"></div>', unsafe_allow_html=True)


# -----------------------------
# KPI STRIP
# -----------------------------
k1, k2, k3, k4, k5 = st.columns(5)

k1.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Total Dispatch Volume</div>
    <div class="kpi-value">1,240 Cr</div>
    <div class="kpi-delta-green">Optimized allocation</div>
</div>
""", unsafe_allow_html=True)

k2.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Urgent Replenishments</div>
    <div class="kpi-value">18</div>
    <div class="kpi-delta-red">Service critical</div>
</div>
""", unsafe_allow_html=True)

k3.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Depot-to-Depot Corridors</div>
    <div class="kpi-value">3</div>
    <div class="kpi-delta-green">Activated</div>
</div>
""", unsafe_allow_html=True)

k4.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Expected Fill Rate</div>
    <div class="kpi-value">97.1%</div>
    <div class="kpi-delta-green">+2.2 pts</div>
</div>
""", unsafe_allow_html=True)

k5.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Premium Freight Risk</div>
    <div class="kpi-value">₹ 12 Cr</div>
    <div class="kpi-delta-red">Lane risk</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# DISPATCH PLAN TABLE
# -----------------------------
st.markdown('<div class="section-title">Dispatch Plan (Plant → Depot)</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Optimized sourcing plan with recommended mode selection and dispatch quantities.</div>', unsafe_allow_html=True)

df_dispatch = pd.DataFrame({
    "Dispatch Date": pd.date_range(datetime.today(), periods=10).strftime("%d-%b"),
    "Source": ["Plant A", "Plant B", "Plant B", "Plant C", "Plant C", "Plant A", "Plant B", "Plant C", "Plant A", "Plant B"],
    "Destination": ["Depot N", "Depot W", "Depot C", "Depot E", "Depot S", "Depot C", "Depot S", "Depot N", "Depot E", "Depot N"],
    "Mode": ["Road", "Rail", "Road", "Road", "Road", "Road", "Road", "Depot-to-Depot", "Road", "Road"],
    "Volume (Cr Units)": [120, 160, 90, 140, 110, 80, 75, 55, 95, 85],
    "Priority": ["High", "High", "Medium", "High", "High", "Medium", "Medium", "High", "Medium", "High"]
})

st.markdown('<div class="panel-card">', unsafe_allow_html=True)
st.dataframe(df_dispatch, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# DEPOT-TO-DEPOT REPLENISHMENT
# -----------------------------
st.markdown('<div class="section-title">Depot-to-Depot Replenishment Corridors</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Activated replenishment corridors to protect service levels and reduce stock-outs.</div>', unsafe_allow_html=True)

df_corridors = pd.DataFrame({
    "From Depot": ["Depot C", "Depot C", "Depot W"],
    "To Depot": ["Depot N", "Depot S", "Depot E"],
    "Volume (Cr Units)": [55, 35, 28],
    "Reason": ["Stock-out risk", "Demand spike", "Lane disruption"],
    "Execution Window": ["48 hrs", "72 hrs", "96 hrs"]
})

st.markdown('<div class="panel-card">', unsafe_allow_html=True)
st.dataframe(df_corridors, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# EXECUTION CALENDAR VIEW (SIMULATED)
# -----------------------------
st.markdown('<div class="section-title">Execution Calendar View</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Dispatch schedule visibility across the next planning horizon.</div>', unsafe_allow_html=True)

df_calendar = df_dispatch.copy()
df_calendar["Dispatch Date"] = pd.to_datetime(df_calendar["Dispatch Date"], format="%d-%b", errors="coerce")
df_calendar["Dispatch Date"] = df_calendar["Dispatch Date"].fillna(datetime.today())

calendar_summary = df_dispatch.groupby("Dispatch Date")["Volume (Cr Units)"].sum().reset_index()

fig_cal = px.bar(
    calendar_summary,
    x="Dispatch Date",
    y="Volume (Cr Units)",
    title="Dispatch Volume by Day (Next Horizon)"
)

fig_cal.update_layout(height=420)

st.plotly_chart(fig_cal, use_container_width=True)


# -----------------------------
# EXECUTION EXCEPTIONS
# -----------------------------
st.markdown('<div class="section-title">Execution Exceptions & Overrides</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">System detected exceptions requiring manual approval or override before execution.</div>', unsafe_allow_html=True)

df_exceptions = pd.DataFrame({
    "Exception": [
        "Rail delay expected Plant B → Depot W",
        "Depot W unloading capacity constraint",
        "High expiry exposure for Diet cluster",
        "Premium freight triggered on Plant A → Depot E",
        "Unplanned sales spike in East"
    ],
    "Severity": ["High", "High", "Critical", "Medium", "High"],
    "Recommended Resolution": [
        "Shift partial volume to road fallback",
        "Move volume to Depot C + cross-dock",
        "Reduce batch size + accelerate liquidation",
        "Route through alternate depot",
        "Trigger surge replenishment"
    ],
    "Approval Required": ["Yes", "Yes", "Yes", "No", "Yes"]
})

left, right = st.columns([2, 1])

with left:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Execution Exception Table")
    st.dataframe(df_exceptions, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Execution Controls")

    st.markdown('<div class="badge-red">MANUAL APPROVAL</div>', unsafe_allow_html=True)
    st.write("3 high-risk dispatches require approval before release.")

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="badge-green">AUTO-EXECUTABLE</div>', unsafe_allow_html=True)
    st.write("7 dispatches can be executed immediately with no risk flags.")

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="badge">NEXT STEP</div>', unsafe_allow_html=True)
    st.write("Push plan to ERP / TMS integration layer.")

    st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")
st.caption("SYDIAI | Execute Dispatch & Replenishment Plan | Supply Chain Decision Intelligence System")
