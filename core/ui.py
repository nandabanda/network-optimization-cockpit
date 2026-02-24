import base64
from pathlib import Path
from typing import Optional
import streamlit as st

LOGO_PATH = Path("assets/sydiai_logo.png")

def _logo_data_uri() -> Optional[str]:
    if not LOGO_PATH.exists():
        return None
    b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{b64}"

def hero(title: str, subtitle: str = "", right: str = ""):
    uri = _logo_data_uri()
    logo_html = f'<img src="{uri}" style="height:54px; width:auto; margin-right:14px;" />' if uri else ""

    st.markdown(
        f"""
        <div class="syd-hero">
          <div style="display:flex; justify-content:space-between; gap:16px; align-items:flex-start;">
            <div style="display:flex; align-items:center;">
              {logo_html}
              <div>
                <div style="font-size:1.35rem; font-weight:700;">{title}</div>
                <div class="syd-subtle" style="margin-top:6px;">{subtitle}</div>
              </div>
            </div>
            <div class="syd-subtle" style="text-align:right; white-space:pre-line;">{right}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def section(title: str, hint: str = ""):
    st.markdown(
        f"""
        <div style="margin: 8px 0 6px 2px;">
          <div style="font-size:1.08rem; font-weight:700;">{title}</div>
          <div class="syd-subtle" style="margin-top:4px;">{hint}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def card_open():
    st.markdown('<div class="syd-card">', unsafe_allow_html=True)

def card_close():
    st.markdown("</div>", unsafe_allow_html=True)
