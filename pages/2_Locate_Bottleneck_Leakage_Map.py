import base64
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Locate-Bottleneck & Leakage Map", layout="wide")

# ------------------------------------------------------------
# Logo
# ------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
LOGO_PATH = ROOT / "assets" / "sydiai_logo.png"

def _logo_uri(path: Path):
    if not path.exists():
        return None
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("utf-8")

logo_uri = _logo_uri(LOGO_PATH)

# ------------------------------------------------------------
# CSS (Same system as Sense page: logo 2.5x + exec typography)
# ------------------------------------------------------------
st.markdown(
    """
<style>
/* Sidebar wider */
section[data-testid="stSidebar"]{
  width: 480px !important;
  min-width: 480px !important;
  max-width: 480px !important;
}
div[data-testid="stSidebarContent"]{
  padding-top: 210px !important; /* room for BIG logo */
}

/* Nav bigger */
[data-testid="stSidebarNav"] a,
[data-testid="stSidebarNav"] span,
[data-testid="stSidebarNav"] div{
  font-size: 1.85rem !important;
  font-weight: 900 !important;
  line-height: 1.28 !important;
}

/* Sidebar labels bigger */
[data-testid="stSidebar"] label{
  font-size: 1.45rem !important;
  font-weight: 950 !important;
}

/* Sidebar select text bigger */
[data-testid="stSidebar"] [data-baseweb="select"] *{
  font-size: 1.18rem !important;
  font-weight: 800 !important;
}

/* BIG logo (2.5x) */
.sydiai-fixed-logo{
  position: fixed;
  top: 18px;
  left: 18px;
  width: 444px;
  height: 170px;
  display:flex;
  align-items:center;
  justify-content:center;
  background: rgba(246,246,243,0.98);
  border-radius: 22px;
  border: 1px solid rgba(0,0,0,0.07);
  box-shadow: 0 12px 30px rgba(0,0,0,0.10);
  z-index: 9999;
}
.sydiai-fixed-logo img{
  max-height: 140px;
  width: auto;
  display:block;
}

/* Main title/subtitle */
.page-title{
  font-size: 3.4rem;
  font-weight: 950;
  color: #0b1320;
  margin: 0;
}
.page-sub{
  font-size: 1.55rem;
  font-weight: 900;
  color: rgba(0,0,0,0.58);
  margin-top: 8px;
}

/* Header card */
.header-card{
  background: #ffffff;
  border: 1px solid rgba(0,0,0,0.06);
  border-radius: 18px;
  padding: 16px 18px;
  box-shadow: 0 10px 24px rgba(0,0,0,0.06);
}
.header-card .brand{
  font-size: 2.6rem;
  font-weight: 950;
}
.header-card .crumb{
  margin-top: 8px;
  font-size: 1.35rem;
  font-weight: 900;
  color: rgba(0,0,0,0.58);
}

/* KPI cards */
.kpi-row { display:flex; gap:18px; flex-wrap:wrap; margin: 14px 0 6px 0; }
.kpi-card{
  flex: 1 1 240px;
  background: linear-gradient(135deg,#0a1020,#020612);
  border-radius: 16px;
  padding: 20px;
  color:#fff;
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 10px 28px rgba(0,0,0,0.18);
  min-height: 108px;
}
.kpi-title{ opacity:0.70; font-size:1.15rem; font-weight:800; }
.kpi-value{ font-size:2.35rem; font-weight:950; margin-top:6px; }
.kpi-sub{ font-size:1.10rem; font-weight:950; margin-top:8px; }
.kpi-sub.good{ color:#3fd0ff; }
.kpi-sub.warn{ color:#ff6b6b; }
.kpi-sub.ok{ color:#58d68d; }

/* Section headings */
.h2{
  font-size: 2.35rem;
  font-weight: 950;
  margin-top: 14px;
}
.h2-sub{
  font-size: 1.25rem;
  color: rgba(0,0,0,0.55);
  font-weight: 900;
  margin-top: 4px;
}

/* Alert pill + insight cards */
.pill{
  display:inline-block;
  padding: 5px 12px;
  border-radius: 999px;
  font-size: 0.95rem;
  font-weight: 950;
  margin-bottom: 8px;
}
.pill.crit{ background: rgba(255,0,0,0.10); color:#b10000; border: 1px solid rgba(255,0,0,0.18); }
.pill.rec{ background: rgba(0,90,255,0.10); color:#003aa8; border: 1px solid rgba(0,90,255,0.18); }

.insight-card{
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 14px;
  padding: 14px 14px;
  background: #ffffff;
  box-shadow: 0 8px 18px rgba(0,0,0,0.05);
  margin-bottom: 12px;
}
.insight-title{
  font-size: 1.35rem;
  font-weight: 950;
  margin: 2px 0 6px 0;
}
.insight-text{
  font-size: 1.12rem;
  color: rgba(0,0,0,0.68);
  font-weight: 800;
}

/* Make DataFrames readable */
[data-testid="stDataFrame"] div,
[data-testid="stDataFrame"] span,
[data-testid="stDataFrame"] p{
  font-size: 1.06rem !important;
  font-weight: 650 !important;
}

/* Plotly text bigger (axis/labels) */
.js-plotly-plot .plotly text{
  font-size: 14px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Sidebar: pinned logo only (filters stay on page as per screenshot)
# ------------------------------------------------------------
with st.sidebar:
    if logo_uri:
        st.markdown(
            f"""
            <div class="sydiai-fixed-logo">
              <img src="{logo_uri}" alt="SYDIAI"/>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="sydiai-fixed-logo">
              <div style="font-weight:950;font-size:2rem;">SYDIAI</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------
# Page Header (same structure as screenshot)
# ------------------------------------------------------------
st.markdown('<div class="page-title">SYDIAI Network Optimization</div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">Enabling Purpose with Precision.</div>', unsafe_allow_html=True)

left, right = st.columns([0.62, 0.38], vertical_alignment="top")

with left:
    st.markdown(
        """
        <div class="header-card">
          <div class="brand">SYDIAI</div>
          <div class="crumb">Locate | Bottleneck &amp; Leakage Map</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown("**Scenario**")
    st.selectbox("", ["Baseline (Current)", "Latest Optimized"], key="scenario_main")
    st.markdown("**Focus Area**")
    st.selectbox("", ["All", "Capacity", "Service", "Inventory", "Transport"], key="focus_main")
    st.caption("Last refreshed: 11 Feb 2026 | 07:20 PM")

st.divider()

# ------------------------------------------------------------
# KPI Row (same as screenshot)
# ------------------------------------------------------------
st.markdown(
    """
<div class="kpi-row">
  <div class="kpi-card">
    <div class="kpi-title">Total Leakage Value</div>
    <div class="kpi-value">₹ 520 Cr</div>
    <div class="kpi-sub warn">High exposure</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Bottleneck Depots</div>
    <div class="kpi-value">4</div>
    <div class="kpi-sub warn">2 critical</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Cost-to-Serve Hotspots</div>
    <div class="kpi-value">6</div>
    <div class="kpi-sub warn">Lane overload</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">SLOB Leakage</div>
    <div class="kpi-value">₹ 185 Cr</div>
    <div class="kpi-sub warn">Expiry risk</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Optimization Potential</div>
    <div class="kpi-value">₹ 240 Cr</div>
    <div class="kpi-sub ok">Actionable</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Leakage Heatmap (same concept as screenshot)
# ------------------------------------------------------------
st.markdown('<div class="h2">Leakage Heatmap</div>', unsafe_allow_html=True)
st.markdown('<div class="h2-sub">Depot × Issue heatmap highlighting highest profit leakage and network constraints.</div>', unsafe_allow_html=True)

depots = ["Depot C", "Depot E", "Depot N", "Depot S", "Depot W"]
issues = [
    "Capacity Bottleneck",
    "Lane Disruption Risk",
    "Low Fill Rate",
    "SLOB / Expiry Risk",
    "Transport Cost Leakage",
]

# Values aligned to screenshot feel (0–90 range)
z = np.array([
    [70, 66, 79, 73, 54],
    [54, 29, 16, 65, 10],
    [57, 33, 77, 35, 78],
    [18, 17, 58, 78, 49],
    [67, 52, 82, 33, 24],
])

df_hm = pd.DataFrame(z, index=depots, columns=issues).reset_index().rename(columns={"index": "Depot"})
df_m = df_hm.melt(id_vars=["Depot"], var_name="Issue", value_name="Leakage (Cr)")

fig = px.density_heatmap(
    df_m,
    x="Issue",
    y="Depot",
    z="Leakage (Cr)",
    text_auto=True,
    color_continuous_scale="Blues",
)
fig.update_layout(
    height=420,
    margin=dict(l=10, r=10, t=30, b=20),
    coloraxis_colorbar=dict(title="Cr"),
)
fig.update_traces(textfont=dict(size=14))
st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------
# Top Bottlenecks (Ranked)
# ------------------------------------------------------------
st.markdown("###")
st.markdown('<div class="h2">Top Bottlenecks (Ranked)</div>', unsafe_allow_html=True)
st.markdown('<div class="h2-sub">System-ranked bottlenecks based on cost impact, service risk, and operational constraints.</div>', unsafe_allow_html=True)

t1, t2 = st.columns([0.68, 0.32], vertical_alignment="top")

with t1:
    st.markdown("### Bottleneck Ranking Table")
    df_bn = pd.DataFrame(
        {
            "Rank": [1, 2, 3, 4, 5, 6, 7],
            "Bottleneck": [
                "Depot W capacity breach",
                "Plant B → Depot W lane overload",
                "Depot C slow mover accumulation",
                "Depot N stock-out risk",
                "Plant A dispatch variability",
                "Depot S replenishment delay",
                "Depot E high cost-to-serve",
            ],
            "Type": [
                "Depot Capacity",
                "Lane Overload",
                "Inventory Leakage",
                "Service Risk",
                "Dispatch Risk",
                "Lead Time Risk",
                "Cost-to-Serve",
            ],
            "Estimated Impact (Cr)": [92, 78, 64, 58, 41, 33, 29],
            "Severity": ["Critical", "Critical", "High", "High", "Medium", "Medium", "Medium"],
        }
    )
    st.dataframe(df_bn, use_container_width=True, hide_index=True)

with t2:
    st.markdown("### Critical Bottleneck Insights")
    st.markdown(
        """
        <div class="insight-card">
          <div class="pill crit">CRITICAL</div>
          <div class="insight-title">Depot W capacity breach</div>
          <div class="insight-text">Depot W capacity breach is causing service loss and lane congestion.</div>
        </div>
        <div class="insight-card">
          <div class="pill crit">CRITICAL</div>
          <div class="insight-title">Plant B → Depot W overload</div>
          <div class="insight-text">Plant B → Depot W overload is driving premium freight and cost-to-serve escalation.</div>
        </div>
        <div class="insight-card">
          <div class="pill rec">SYSTEM RECOMMENDATION</div>
          <div class="insight-title">Enable alternate lane + shift sourcing</div>
          <div class="insight-text">Enable alternate lane + shift sourcing to Depot C.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# Opportunity Capture Plan
# ------------------------------------------------------------
st.markdown("###")
st.markdown('<div class="h2">Opportunity Capture Plan</div>', unsafe_allow_html=True)
st.markdown('<div class="h2-sub">Actionable orchestration opportunities derived from bottleneck and leakage diagnosis.</div>', unsafe_allow_html=True)

df_opp = pd.DataFrame(
    {
        "Opportunity": [
            "Shift sourcing from Depot W → Depot C",
            "Enable depot-to-depot replenishment Depot C → Depot N",
            "Rationalize slow movers in Depot C",
            "Convert road lane to rail Plant B → Depot W",
            "Reduce safety stock on low moving SKUs",
        ],
        "Benefit (Cr)": [62, 28, 55, 31, 45],
        "Time to Execute": ["2 weeks", "1 week", "4 weeks", "3 weeks", "2 weeks"],
        "Execution Priority": ["Immediate", "Immediate", "High", "Medium", "High"],
    }
)
st.dataframe(df_opp, use_container_width=True, hide_index=True)

st.divider()
st.caption("SYDIAI | Locate Bottleneck & Leakage Map | Supply Chain Decision Intelligence System")
