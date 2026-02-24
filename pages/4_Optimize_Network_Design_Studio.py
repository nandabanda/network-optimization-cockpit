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
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="SYDIAI | Optimize Network Design Studio",
    page_icon="🧠",
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
        <div class="subtitle">Optimize | Network Design Studio</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.selectbox("Optimization Run", ["Run #21 (Latest)", "Run #20", "Run #19", "Run #18"])
    st.selectbox("Constraint Set", ["Standard", "Capacity Constrained", "Low Cost Priority", "Service Priority"])
    st.caption(f"Last refreshed: {datetime.now().strftime('%d %b %Y | %I:%M %p')}")

st.markdown('<div class="hr-line"></div>', unsafe_allow_html=True)


# -----------------------------
# KPI STRIP
# -----------------------------
k1, k2, k3, k4, k5 = st.columns(5)

k1.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Logistics Cost Saving</div>
    <div class="kpi-value">₹ 136 Cr</div>
    <div class="kpi-delta-green">-9.6%</div>
</div>
""", unsafe_allow_html=True)

k2.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Service Improvement</div>
    <div class="kpi-value">+3.1 pts</div>
    <div class="kpi-delta-green">Fill-rate gain</div>
</div>
""", unsafe_allow_html=True)

k3.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Avg Lead Time</div>
    <div class="kpi-value">2.8 days</div>
    <div class="kpi-delta-green">-0.7 days</div>
</div>
""", unsafe_allow_html=True)

k4.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Depot Load Balance</div>
    <div class="kpi-value">84%</div>
    <div class="kpi-delta-green">Stable utilization</div>
</div>
""", unsafe_allow_html=True)

k5.markdown("""
<div class="kpi-card">
    <div class="kpi-label">Depot-to-Depot Flow</div>
    <div class="kpi-value">60 Cr</div>
    <div class="kpi-delta-green">Enabled corridors</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# SYNTHETIC NETWORK NODES + FLOWS
# -----------------------------
plants = pd.DataFrame({
    "node": ["Plant A", "Plant B", "Plant C"],
    "type": ["Plant", "Plant", "Plant"],
    "lat": [28.6, 19.0, 22.7],
    "lon": [77.2, 72.8, 88.4]
})

depots = pd.DataFrame({
    "node": ["Depot N", "Depot W", "Depot S", "Depot E", "Depot C"],
    "type": ["Depot"] * 5,
    "lat": [29.1, 19.1, 13.1, 23.0, 21.2],
    "lon": [76.9, 73.0, 80.3, 87.3, 78.5]
})

nodes = pd.concat([plants, depots], ignore_index=True)

flows_before = pd.DataFrame({
    "source": ["Plant A","Plant A","Plant B","Plant B","Plant C","Plant C"],
    "target": ["Depot N","Depot C","Depot W","Depot S","Depot E","Depot C"],
    "volume": [180, 140, 210, 160, 170, 120],
    "mode": ["Road","Road","Rail","Road","Road","Road"],
    "cost_per_unit": [5.2, 4.8, 3.6, 4.9, 5.0, 4.7]
})

flows_after = pd.DataFrame({
    "source": ["Plant A","Plant B","Plant B","Plant C","Plant C","Depot C"],
    "target": ["Depot N","Depot W","Depot C","Depot E","Depot S","Depot N"],
    "volume": [200, 240, 120, 190, 150, 60],
    "mode": ["Road","Rail","Road","Road","Road","Depot-to-Depot"],
    "cost_per_unit": [4.9, 3.4, 4.3, 4.6, 4.5, 3.9]
})


# -----------------------------
# NETWORK MAP FUNCTION
# -----------------------------
def plot_network(nodes_df, flows_df, title):
    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon=nodes_df["lon"],
        lat=nodes_df["lat"],
        text=nodes_df["node"] + " (" + nodes_df["type"] + ")",
        mode="markers+text",
        textposition="bottom center",
        marker=dict(size=12),
        name="Nodes"
    ))

    for _, row in flows_df.iterrows():
        src = nodes_df[nodes_df["node"] == row["source"]].iloc[0]
        tgt = nodes_df[nodes_df["node"] == row["target"]].iloc[0]

        fig.add_trace(go.Scattergeo(
            lon=[src["lon"], tgt["lon"]],
            lat=[src["lat"], tgt["lat"]],
            mode="lines",
            line=dict(width=2),
            opacity=0.65,
            hoverinfo="text",
            text=f'{row["source"]} → {row["target"]}<br>'
                 f'Volume: {row["volume"]}<br>'
                 f'Mode: {row["mode"]}<br>'
                 f'Cost/Unit: {row["cost_per_unit"]}',
            name=f'{row["source"]} → {row["target"]}'
        ))

    fig.update_layout(
        title=title,
        geo=dict(
            scope="asia",
            projection_type="natural earth",
            showcountries=True,
            countrycolor="rgba(0,0,0,0.1)",
            showland=True,
            landcolor="rgba(240,240,240,0.8)"
        ),
        margin=dict(l=0, r=0, t=40, b=0),
        height=520
    )

    return fig


# -----------------------------
# BEFORE VS AFTER NETWORK VIEW
# -----------------------------
st.markdown('<div class="section-title">Network Design | Before vs After</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Plant + depot sourcing rebalancing, optimized lane flows, and depot-to-depot replenishment corridors.</div>', unsafe_allow_html=True)

m1, m2 = st.columns(2)

with m1:
    st.markdown('<div class="badge">Current Network</div>', unsafe_allow_html=True)
    st.plotly_chart(plot_network(nodes, flows_before, "Current Network Flow (Before Optimization)"), use_container_width=True)

with m2:
    st.markdown('<div class="badge">Optimized Network</div>', unsafe_allow_html=True)
    st.plotly_chart(plot_network(nodes, flows_after, "Optimized Network Flow (After Optimization)"), use_container_width=True)


# -----------------------------
# SOLVER OUTPUT TABLES
# -----------------------------
st.markdown('<div class="section-title">Solver Output | Lane Recommendations</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Recommended sourcing split, lane volume shifts, and cost-to-serve impact.</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)

with t1:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Before Optimization")
    df_before = flows_before.copy()
    df_before["Total Cost"] = (df_before["volume"] * df_before["cost_per_unit"]).round(1)
    st.dataframe(df_before, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t2:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("After Optimization")
    df_after = flows_after.copy()
    df_after["Total Cost"] = (df_after["volume"] * df_after["cost_per_unit"]).round(1)
    st.dataframe(df_after, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# COST COMPARISON CHART
# -----------------------------
st.markdown('<div class="section-title">Cost-to-Serve Comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Comparison of total cost across lanes (Before vs After).</div>', unsafe_allow_html=True)

df_before_chart = df_before[["source", "target", "Total Cost"]].copy()
df_before_chart["Scenario"] = "Before"

df_after_chart = df_after[["source", "target", "Total Cost"]].copy()
df_after_chart["Scenario"] = "After"

df_cost = pd.concat([df_before_chart, df_after_chart])
df_cost["Lane"] = df_cost["source"] + " → " + df_cost["target"]

fig_cost = px.bar(
    df_cost,
    x="Lane",
    y="Total Cost",
    color="Scenario",
    barmode="group",
    title="Lane Cost Comparison"
)

fig_cost.update_layout(height=450)

st.plotly_chart(fig_cost, use_container_width=True)


# -----------------------------
# DEPOT LOAD BALANCE
# -----------------------------
st.markdown('<div class="section-title">Depot Load Balance</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Expected inbound volume distribution across depots after optimization.</div>', unsafe_allow_html=True)

df_depot_load = df_after.groupby("target")["volume"].sum().reset_index()
df_depot_load.columns = ["Depot", "Inbound Volume"]

fig_load = px.bar(
    df_depot_load,
    x="Depot",
    y="Inbound Volume",
    title="Inbound Volume by Depot (Optimized)"
)

fig_load.update_layout(height=420)

st.plotly_chart(fig_load, use_container_width=True)


# -----------------------------
# LIGHTHOUSE NETWORK BLUEPRINT
# -----------------------------
st.markdown('<div class="section-title">Lighthouse Blueprint</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Future-state network blueprint for annual re-optimization and strategic sourcing governance.</div>', unsafe_allow_html=True)

st.markdown("""
<div class="panel-card">
    <h3 style="margin-top:0;">Lighthouse Network Concept</h3>
    <ul style="font-size:1.05rem; font-weight:800; color:#334155; line-height:1.65;">
        <li><b>Target sourcing split</b> by plant + depot (primary + secondary)</li>
        <li><b>Preferred lane modes</b> (rail priority corridors + road fallback)</li>
        <li><b>Depot-to-depot replenishment corridors</b> to protect service level</li>
        <li><b>Capacity governance</b> to avoid chronic overload patterns</li>
        <li><b>Scenario-driven re-optimization</b> for demand spikes & new product launches</li>
    </ul>
    <p style="font-size:0.95rem; font-weight:900; color:#64748b;">
        Lighthouse blueprint becomes the strategic reference model for long-term supply chain transformation.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("---")
st.caption("SYDIAI | Optimize Network Design Studio | Supply Chain Decision Intelligence System")
