import base64
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sense-Executive pulse", layout="wide")

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
# CSS (Same as Orchestration + BIG READABILITY BOOST)
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

/* Alert pill */
.pill{
  display:inline-block;
  padding: 5px 12px;
  border-radius: 999px;
  font-size: 0.95rem;
  font-weight: 950;
  margin-bottom: 8px;
}
.pill.crit{ background: rgba(255,0,0,0.10); color:#b10000; border: 1px solid rgba(255,0,0,0.18); }
.pill.act{ background: rgba(0,90,255,0.10); color:#003aa8; border: 1px solid rgba(0,90,255,0.18); }

.alert-card{
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 14px;
  padding: 14px 14px;
  background: #ffffff;
  box-shadow: 0 8px 18px rgba(0,0,0,0.05);
  margin-bottom: 12px;
}
.alert-title{
  font-size: 1.35rem;
  font-weight: 950;
  margin: 2px 0 6px 0;
}
.alert-text{
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

/* Make markdown headings readable */
h1, h2, h3{
  font-weight: 950 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Sidebar: pinned logo
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
# Page Header (same structure)
# ------------------------------------------------------------
st.markdown('<div class="page-title">SYDIAI Network Optimization</div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">Enabling Purpose with Precision.</div>', unsafe_allow_html=True)

left, right = st.columns([0.62, 0.38], vertical_alignment="top")

with left:
    st.markdown(
        """
        <div class="header-card">
          <div class="brand">SYDIAI</div>
          <div class="crumb">Sense | Executive Pulse (Supply Chain)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown("**Scenario**")
    st.selectbox("", ["Latest Optimized", "Baseline"], key="scenario_main")
    st.markdown("**Region**")
    st.selectbox("", ["All Regions", "North", "South", "East", "West"], key="region_main")
    st.caption("Last refreshed: 11 Feb 2026 | 06:32 PM")

st.divider()

# ------------------------------------------------------------
# KPI Row
# ------------------------------------------------------------
st.markdown(
    """
<div class="kpi-row">
  <div class="kpi-card">
    <div class="kpi-title">Service Level</div>
    <div class="kpi-value">96.2%</div>
    <div class="kpi-sub ok">+3.4 pts</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Inventory Coverage</div>
    <div class="kpi-value">27 days</div>
    <div class="kpi-sub warn">+4 days risk</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">SLOB Exposure</div>
    <div class="kpi-value">₹ 185 Cr</div>
    <div class="kpi-sub warn">High risk clusters</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Cost-to-Serve</div>
    <div class="kpi-value">₹ 1,420 Cr</div>
    <div class="kpi-sub ok">-9.6% optimized</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Network Bottlenecks</div>
    <div class="kpi-value">7</div>
    <div class="kpi-sub warn">2 critical</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# System Detected Exceptions
# ------------------------------------------------------------
st.markdown('<div class="h2">System Detected Exceptions</div>', unsafe_allow_html=True)
st.markdown('<div class="h2-sub">Auto-detected risk signals requiring immediate orchestration action.</div>', unsafe_allow_html=True)

c1, c2 = st.columns([0.68, 0.32], vertical_alignment="top")

with c1:
    st.markdown("### Exception Radar")
    df_ex = pd.DataFrame(
        {
            "Exception": [
                "Stock-out risk (Top 20 SKU cluster)",
                "Expiry exposure on Diet / Light portfolio",
                "Depot W utilization breach (>95%)",
                "Demand spike detected in East (+18%)",
                "Rail lane disruption risk (Plant B → Depot W)",
                "Slow movers accumulating in Depot C",
                "Customer service drop in North MT",
            ],
            "Severity": ["Critical", "Critical", "High", "High", "Medium", "Medium", "High"],
            "Impact Area": ["Service", "Inventory", "Capacity", "Demand", "Transport", "SLOB", "Service"],
            "Recommended Action": [
                "Trigger surge replenishment from Depot C",
                "Reduce batch size + liquidate risk SKUs",
                "Shift load to Depot C + re-route flows",
                "Increase replenishment frequency + safety stock",
                "Activate alternate lane (Road fallback)",
                "Rationalize SKUs + stop production",
                "Review allocation logic and route priority",
            ],
        }
    )
    st.dataframe(df_ex, use_container_width=True, hide_index=True)

with c2:
    st.markdown("### Critical Alerts")
    st.markdown(
        """
        <div class="alert-card">
          <div class="pill crit">CRITICAL</div>
          <div class="alert-title">Stock-out risk detected for top-selling SKUs in North</div>
          <div class="alert-text">Expected fill-rate drop within 72 hrs.</div>
        </div>
        <div class="alert-card">
          <div class="pill crit">CRITICAL</div>
          <div class="alert-title">Expiry exposure building in Diet / Light cluster</div>
          <div class="alert-text">Recommended action required within 10 days.</div>
        </div>
        <div class="alert-card">
          <div class="pill act">SYSTEM ACTION</div>
          <div class="alert-title">Scenario simulation recommended</div>
          <div class="alert-text">Run scenario before dispatch execution.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# Inventory Health Snapshot
# ------------------------------------------------------------
st.markdown("###")
st.markdown('<div class="h2">Inventory Health Snapshot</div>', unsafe_allow_html=True)
st.markdown('<div class="h2-sub">Coverage, expiry risk and slow-mover accumulation patterns across depots.</div>', unsafe_allow_html=True)

df_inv = pd.DataFrame(
    {
        "Depot": ["Depot N", "Depot W", "Depot S", "Depot E", "Depot C"],
        "Inventory Value (Cr)": [420, 510, 390, 280, 520],
        "Coverage (Days)": [18, 31, 26, 21, 38],
        "Expiry Risk (Cr)": [22, 18, 12, 9, 34],
        "SLOB Risk (Cr)": [35, 48, 22, 18, 62],
    }
)
st.dataframe(df_inv, use_container_width=True, hide_index=True)

# ------------------------------------------------------------
# Network Health Snapshot
# ------------------------------------------------------------
st.markdown("###")
st.markdown('<div class="h2">Network Health Snapshot</div>', unsafe_allow_html=True)
st.markdown('<div class="h2-sub">Lane utilization, sourcing shifts and bottleneck visibility across plant + depot network.</div>', unsafe_allow_html=True)

df_net = pd.DataFrame(
    {
        "Lane": ["Plant A → Depot N", "Plant B → Depot W", "Plant B → Depot S", "Plant C → Depot E", "Depot C → Depot N"],
        "Mode": ["Road", "Rail", "Road", "Road", "Depot-to-Depot"],
        "Volume (Cr Units)": [200, 240, 120, 190, 60],
        "Utilization %": [82, 96, 74, 79, 65],
        "Risk Flag": ["Stable", "High Risk", "Stable", "Stable", "Opportunity"],
    }
)
st.dataframe(df_net, use_container_width=True, hide_index=True)

# ------------------------------------------------------------
# Recommended Orchestration Actions
# ------------------------------------------------------------
st.markdown("###")
st.markdown('<div class="h2">Recommended Orchestration Actions</div>', unsafe_allow_html=True)
st.markdown('<div class="h2-sub">Auto-generated actions based on inventory + network signal detection.</div>', unsafe_allow_html=True)

df_act = pd.DataFrame(
    {
        "Action": [
            "Reallocate 12% inventory from Depot C → Depot N",
            "Trigger surge replenishment for North Top SKUs",
            "Reduce Diet/Light batch size + liquidation plan",
            "Re-route Plant B → Depot W via road fallback",
            "Cap Depot W inbound; shift to Depot C cross-dock",
        ],
        "Expected Benefit": ["Service +2.1 pts", "Avoid stock-outs", "Expiry -₹8 Cr", "Avoid disruption", "Prevent overload"],
        "Execution Priority": ["Immediate", "Immediate", "High", "Medium", "High"],
    }
)
st.dataframe(df_act, use_container_width=True, hide_index=True)
