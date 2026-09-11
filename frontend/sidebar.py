import os
import streamlit as st
from typing import Dict, Any

def render_sidebar() -> Dict[str, Any]:
    """
    Renders mission parameter controls in the left sidebar with Amber Gold Robotics UI aesthetic.
    """
    with st.sidebar:
        st.markdown("<h3 style='color: #FF9F00; font-family: Space Grotesk, sans-serif; letter-spacing: 0.5px;'>🎛️ MISSION PARAMETERS</h3>", unsafe_allow_html=True)
        default_key = os.getenv("GEMINI_API_KEY", "")
        gemini_key = st.text_input("Google Gemini API Key", value=default_key, type="password", help="Enter Google AI Studio Gemini API Key. Can also be set via GEMINI_API_KEY environment variable.")
        if default_key:
            st.caption("🟢 GEMINI_API_KEY detected in environment.")
        
        st.markdown("---")
        st.markdown("<h3 style='color: #FF9F00; font-family: Space Grotesk, sans-serif; letter-spacing: 0.5px;'>🌧️ WEATHER TELEMETRY</h3>", unsafe_allow_html=True)
        weather_mode = st.radio(
            "Select Weather Feed:",
            [
                "🛰️ Live Orbital Radar (Actual 100% Live)",
                "⛈️ Sudden Cloudburst / Heavy Rain (Demo Crisis)",
                "🌫️ Dense Fog & Mist (Lens Caution)"
            ]
        )
        
        st.markdown("---")
        st.markdown("<h3 style='color: #FF9F00; font-family: Space Grotesk, sans-serif; letter-spacing: 0.5px;'>🌐 GLOBAL LANGUAGE</h3>", unsafe_allow_html=True)
        language_options = [
            "Tanglish (Tamil in English)",
            "Tamil (தமிழ்)",
            "English",
            "Hindi (हिंदी)",
            "Telugu (తెలుగు)",
            "Malayalam (മലയാളം)",
            "Kannada (ಕನ್ನಡ)",
            "Spanish (Español)",
            "French (Français)"
        ]
        selected_language = st.selectbox("🗣️ Target Output Language:", language_options)
        
        report_format = st.radio(
            "📑 Report Granularity:",
            [
                "⚡ 1-Minute Executive Flash (Short)",
                "📋 Full Production Blueprint (Detailed)"
            ]
        )
        
        st.markdown("---")
        st.markdown("<div style='text-align: center; color: #94A3B8; font-size: 0.78rem; font-family: JetBrains Mono, monospace;'>⚡ <b>CrisisShift OS v2.0</b><br><span style='color:#FF9F00;'>Enterprise Agentic Cinema</span></div>", unsafe_allow_html=True)

    return {
        "gemini_key": gemini_key,
        "weather_mode": weather_mode,
        "selected_language": selected_language,
        "report_format": report_format
    }
