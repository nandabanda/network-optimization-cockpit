import base64
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYDIAI | Orchestration Landing", layout="wide")

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
# CSS (Logo 2.5x, Title/Sub 2x, Framework text 2x, Sidebar wider)
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
  width: 444px;     /* 480 - margins */
  height: 170px;    /* BIG */
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
  max-height: 140px;  /* BIG */
  width: auto;
  display:block;
}

/* Title 2x */
.page-title{
  font-size: 4.2rem;
  font-weight: 950;
  color: #0b1320;
  margin: 0;
}

/* Subtitle 2x */
.page-sub{
  font-size: 2.0rem;
  font-weight: 900;
  color: rgba(0,0,0,0.65);
  margin-top: 10px;
}

/* KPI cards */
.kpi-row { display:flex; gap:18px; flex-wrap:wrap; margin-top: 14px; }
.kpi-card{
  flex: 1 1 240px;
  background: linear-gradient(135deg,#0a1020,#020612);
  border-radius: 16px;
  padding: 18px;
  color:#fff;
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 10px 28px rgba(0,0,0,0.18);
  min-height: 92px;
}
.kpi-title{ opacity:0.70; font-size:0.95rem; font-weight:700; }
.kpi-value{ font-size:1.85rem; font-weight:950; margin-top:6px; }
.kpi-sub{ color:#3fd0ff; font-weight:900; margin-top:6px; }

/* Framework text 2x */
.fw-title{
  font-size: 2.4rem;
  font-weight: 950;
  color:#0b1320;
  margin-top: 18px;
}
.fw-line{
  font-size: 1.6rem;
  font-weight: 950;
  color: rgba(0,0,0,0.60);
  margin-top: 6px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Sidebar
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

    st.markdown("**Business Unit**")
    st.selectbox("", ["All Business Units", "BU-1", "BU-2"], key="bu")

    st.markdown("**Scenario**")
    st.selectbox("", ["Latest Optimized", "Baseline"], key="scenario")

    st.caption("Last refreshed: 11 Feb 2026 | 03:20 PM")

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
st.markdown('<div class="page-title">SYDIAI</div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">Supply Chain Orchestration Cockpit | Inventory + Network Optimization</div>', unsafe_allow_html=True)
st.divider()

# ------------------------------------------------------------
# KPIs (5 cards like your earlier view)
# ------------------------------------------------------------
st.markdown(
    """
<div class="kpi-row">
  <div class="kpi-card">
    <div class="kpi-title">Total Supply Chain Cost</div>
    <div class="kpi-value">₹ 3,420 Cr</div>
    <div class="kpi-sub">-8.4% Optimized</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Inventory Value</div>
    <div class="kpi-value">₹ 2,120 Cr</div>
    <div class="kpi-sub">-12.1% vs Baseline</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Service Level</div>
    <div class="kpi-value">96.2%</div>
    <div class="kpi-sub">+3.4 pts</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">SLOB Risk</div>
    <div class="kpi-value">₹ 185 Cr</div>
    <div class="kpi-sub">-22% Exposure</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-title">Network Cost-to-Serve</div>
    <div class="kpi-value">₹ 1,420 Cr</div>
    <div class="kpi-sub">-9.6% Optimized</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Framework header (2x)
# ------------------------------------------------------------
st.markdown('<div class="fw-title">Decision Orchestration Framework</div>', unsafe_allow_html=True)
st.markdown('<div class="fw-line">Sense → Locate → Prioritize → Diagnose → Optimize → Execute → Control</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# RESTORED: Beautiful circular/orbit framework (text 2x inside SVG)
# ------------------------------------------------------------
components.html(
    """
<div style="width:100%; display:flex; justify-content:center; padding: 18px 0 6px 0;">
  <div style="
      width: 100%;
      max-width: 1400px;
      border-radius: 24px;
      border: 1px solid rgba(0,0,0,0.06);
      background: radial-gradient(circle at center, rgba(20,60,120,0.16), rgba(255,255,255,0));
      padding: 26px 18px;
      overflow:hidden;
  ">
    <svg width="1320" height="560" viewBox="0 0 1320 560" xmlns="http://www.w3.org/2000/svg"
         style="max-width:100%; height:auto;">
      <defs>
        <filter id="shadow" x="-25%" y="-25%" width="150%" height="150%">
          <feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="rgba(0,0,0,0.20)"/>
        </filter>
      </defs>

      <rect x="16" y="16" width="1288" height="528" rx="22" fill="rgba(255,255,255,0.38)"/>

      <!-- orbit -->
      <circle cx="660" cy="280" r="235" fill="none" stroke="rgba(11,19,32,0.18)"
              stroke-dasharray="5,6" stroke-width="2"/>

      <!-- center -->
      <circle cx="660" cy="280" r="145" fill="#0a1020" filter="url(#shadow)"/>
      <text x="660" y="262" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="950"
            font-family="ui-sans-serif, system-ui, -apple-system">SYDIAI Supply Chain</text>
      <text x="660" y="295" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="950"
            font-family="ui-sans-serif, system-ui, -apple-system">Cockpit</text>
      <text x="660" y="332" text-anchor="middle" fill="rgba(255,255,255,0.82)" font-size="15" font-weight="900"
            font-family="ui-sans-serif, system-ui, -apple-system">Inventory Orchestration + Network</text>
      <text x="660" y="355" text-anchor="middle" fill="rgba(255,255,255,0.82)" font-size="15" font-weight="900"
            font-family="ui-sans-serif, system-ui, -apple-system">Optimization</text>
      <text x="660" y="382" text-anchor="middle" fill="rgba(255,255,255,0.72)" font-size="13.5" font-weight="850"
            font-family="ui-sans-serif, system-ui, -apple-system">across the Demand-to-Fulfillment loop</text>

      <!-- cards (2x-ish readable) -->
      <!-- Sense -->
      <g filter="url(#shadow)"><rect x="520" y="58" width="320" height="100" rx="18" fill="#0a1020"/></g>
      <text x="548" y="96" fill="#ffffff" font-size="18" font-weight="950" font-family="ui-sans-serif, system-ui">Sense</text>
      <text x="548" y="121" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">Demand signals & supply</text>
      <text x="548" y="140" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">constraints</text>

      <!-- Locate -->
      <g filter="url(#shadow)"><rect x="950" y="176" width="320" height="100" rx="18" fill="#0a1020"/></g>
      <text x="978" y="214" fill="#ffffff" font-size="18" font-weight="950" font-family="ui-sans-serif, system-ui">Locate</text>
      <text x="978" y="239" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">Profit leakage & bottlenecks</text>

      <!-- Prioritize -->
      <g filter="url(#shadow)"><rect x="920" y="338" width="350" height="112" rx="18" fill="#0a1020"/></g>
      <text x="948" y="380" fill="#ffffff" font-size="18" font-weight="950" font-family="ui-sans-serif, system-ui">Prioritize</text>
      <text x="948" y="405" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">SKU lanes & cost-to-serve</text>
      <text x="948" y="424" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">hotspots</text>

      <!-- Diagnose -->
      <g filter="url(#shadow)"><rect x="520" y="450" width="320" height="100" rx="18" fill="#0a1020"/></g>
      <text x="548" y="488" fill="#ffffff" font-size="18" font-weight="950" font-family="ui-sans-serif, system-ui">Diagnose</text>
      <text x="548" y="513" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">Root cause decomposition</text>

      <!-- Optimize -->
      <g filter="url(#shadow)"><rect x="50" y="338" width="350" height="112" rx="18" fill="#0a1020"/></g>
      <text x="78" y="380" fill="#ffffff" font-size="18" font-weight="950" font-family="ui-sans-serif, system-ui">Optimize</text>
      <text x="78" y="405" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">Plant + depot network</text>
      <text x="78" y="424" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">rebalancing</text>

      <!-- Execute -->
      <g filter="url(#shadow)"><rect x="160" y="176" width="330" height="100" rx="18" fill="#0a1020"/></g>
      <text x="188" y="214" fill="#ffffff" font-size="18" font-weight="950" font-family="ui-sans-serif, system-ui">Execute</text>
      <text x="188" y="239" fill="rgba(255,255,255,0.80)" font-size="13.5" font-weight="850" font-family="ui-sans-serif, system-ui">Dispatch & replenishment decisions</text>
    </svg>
  </div>
</div>
""",
    height=620,
)

# ------------------------------------------------------------
# Executive Signals
# ------------------------------------------------------------
st.markdown("## Executive Signals")
st.markdown("Top optimization recommendations and risk alerts detected by the system.")

c1, c2 = st.columns(2)

with c1:
    st.markdown("🔥 **Top Optimization Recommendations**")
    df1 = pd.DataFrame({
        "Recommendation": [
            "Shift 12% sourcing from Depot C to Depot N",
            "Enable depot-to-depot replenishment: Depot C → Depot N",
            "Reduce safety stock on slow movers (Class C)",
            "Rationalize 38 SKUs with <1% contribution",
            "Increase rail share on Plant B → Depot W lane",
        ],
        "Impact (Cr)": [62, 28, 45, 55, 31],
        "Confidence": ["High", "High", "Medium", "High", "Medium"],
    })
    st.dataframe(df1, use_container_width=True, hide_index=True)

with c2:
    st.markdown("⚠️ **Key Risks & Alerts**")
    df2 = pd.DataFrame({
        "Alert": [
            "Stock-out risk detected in North",
            "Expiry exposure for Diet SKU cluster",
            "Demand spike in East: +18%",
            "Depot W capacity overload risk",
            "Competitor price war expected in South",
        ],
        "Severity": ["High", "High", "Medium", "Medium", "Medium"],
        "Recommended Action": [
            "Reallocate inventory from Depot C",
            "Reduce production batch size + liquidate",
            "Trigger surge replenishment",
            "Shift volume to Depot C",
            "Protect premium mix, avoid discount spiral",
        ],
    })
    st.dataframe(df2, use_container_width=True, hide_index=True)
