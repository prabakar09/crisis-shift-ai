import streamlit as st

# Import 3-Tier Architecture Modules
from database.db import init_db, save_mission_log
from backend.telemetry_service import fetch_telemetry_data, evaluate_physics
from backend.cost_calculator import calculate_production_burn_rate
from backend.agent_swarm import run_director_swarm
from backend.pdf_exporter import generate_pdf_report
from frontend.styles import inject_hud_styles, disable_browser_autofill
from frontend.sidebar import render_sidebar
from frontend.hud_components import (
    render_system_status_banner,
    render_hero_banner,
    render_telemetry_bar,
    render_agent_architecture_card,
    render_ground_physics_cards,
    render_satellite_views,
    render_dispatch_output
)
from frontend.scene_manager import render_scene_manager
from frontend.history_tab import render_history_tab
from frontend.test_cases_tab import render_test_cases_tab

# Page Configuration
st.set_page_config(
    page_title="CrisisShift OS | Autonomous Cinema Command",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Database Schema & Seed Data
init_db()

# Inject Next-Gen Military Cinema HUD Styling & Suppress Browser Autofill
inject_hud_styles()
disable_browser_autofill()

# Render Sidebar Parameters
config = render_sidebar()
gemini_key = config["gemini_key"]
weather_mode = config["weather_mode"]
selected_language = config["selected_language"]
report_format = config["report_format"]

# 1. Render BIG PROMINENT LIVE SYSTEM HEALTH & SWARM STATUS BADGE
render_system_status_banner()

# 2. Main Banner & Telemetry Header
render_hero_banner()
render_telemetry_bar()

# 3. Navigation Tabs (Including Test Cases Benchmark Suite)
tab_hud, tab_scenes, tab_history, tab_testcases = st.tabs([
    "🛰️ Live Command HUD",
    "📋 Scene Breakdown Manager",
    "📜 Mission Audit Logs",
    "🧪 Scenario Test Suite"
])

with tab_hud:
    # Autonomous Multi-Agent Swarm Architecture & Tanglish Support Card
    render_agent_architecture_card()

    # Highlighted Active Production Location & Scene Input Box
    st.markdown("""
    <div class="target-input-box">
        <h4 style="color: #FF9F00; font-family: 'Space Grotesk', sans-serif; font-weight: 800; margin: 0 0 12px 0; letter-spacing: 0.5px;">
            📍 ACTIVE PRODUCTION TARGET & SCENE INPUT
        </h4>
        <p style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 16px;">
            Enter target shooting location coordinates and scheduled scene requirements below. Type any location in the world to analyze real-time satellite telemetry.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_loc, col_scene = st.columns([1, 1.8])
        
    with col_loc:
        location_input = st.text_input(
            "📍 Shooting Location / City (Global Worldwide):",
            value="",
            placeholder="e.g. Coimbatore, Chennai, Mumbai, London, Tokyo, New York...",
            key="manual_target_loc_clean"
        )

    with col_scene:
        scene_input = st.text_area(
            "🎬 Scheduled Scene Breakdown & Assets:",
            height=95,
            value="",
            placeholder="e.g. Scene 54 (EXT. DAY): High-speed car chase sequence with Lead Actor, 20 stunt riders, and heavy Technocrane setup...",
            key="manual_target_scene_clean"
        )

    target_loc = location_input.strip()

    if target_loc:
        # Fetch Real-time Environmental Telemetry & Evaluate Physics
        telemetry = fetch_telemetry_data(target_loc, weather_mode)
        physics = evaluate_physics(telemetry)

        # Render Terrain Physics & Surface Asphalt Cards
        render_ground_physics_cards(physics, telemetry)

        # Render Interactive Satellite Visual Optics & Pydeck Map with Red Hazard & Green Safe Zones
        render_satellite_views(telemetry, target_loc, weather_mode)

    else:
        st.markdown("""
        <div style="background: rgba(255, 159, 0, 0.06); border: 1px dashed rgba(255, 159, 0, 0.4); border-radius: 14px; padding: 20px 24px; text-align: center; margin: 18px 0;">
            <span style="color: #FF9F00; font-family: 'Space Grotesk', sans-serif; font-size: 1.05rem; font-weight: 700;">
                🌍 Enter any shooting location or city anywhere in the world above to initialize live satellite reconnaissance & radar.
            </span>
        </div>
        """, unsafe_allow_html=True)
        # Default baseline for ready execution if needed
        telemetry = fetch_telemetry_data("Global Base", weather_mode)
        physics = evaluate_physics(telemetry)

    # Initialize Session State to prevent dispatch output & buttons from disappearing on click
    if "active_blueprint" not in st.session_state:
        st.session_state["active_blueprint"] = None
        st.session_state["active_stunt_status"] = None
        st.session_state["active_loc"] = None
        st.session_state["active_weather_mode"] = None
        st.session_state["sms_dispatched"] = False

    # Multi-Agent Swarm Execution Engine
    if st.button("⚡ EXECUTE REAL-TIME SATELLITE RECON & RUN SWARM"):
        if not target_loc:
            st.warning("⚠️ Please enter a shooting location / city in the input box above.")
        elif not scene_input.strip():
            st.warning("⚠️ Please enter the scheduled scene breakdown & assets in the box above before executing.")
        elif not gemini_key:
            st.error("⚠️ CRITICAL: Enter your Google Gemini API Key in the left sidebar.")
        else:
            resolved_scene = scene_input.strip()
            
            # Calculate Approximate Location Production Burn Rate
            cost_info = calculate_production_burn_rate(physics.stunt_status, telemetry.rain, location_name=target_loc)
            approx_burn_rate = f"{cost_info['hourly_burn']} ({cost_info['location_tier']})"
            
            with st.status(f"🛰️ Executing Ground Truth Reconnaissance [{weather_mode}]...", expanded=True) as status:
                st.write(f"🛰️ **Agent 1 (Satellite Scout):** Querying atmospheric sensors for `{target_loc}`...")
                st.write(f"🔬 **Agent 2 (Terrain Physics & Logistics):** Road friction + {approx_burn_rate} rate...")
                st.write(f"🧠 **Agent 3 (Director Swarm & Language Engine):** Generating directorial blueprint in {selected_language}...")
                
                final_blueprint = run_director_swarm(
                    api_key=gemini_key,
                    location_input=target_loc,
                    scene_input=resolved_scene,
                    telemetry=telemetry,
                    physics=physics,
                    selected_language=selected_language,
                    report_format=report_format,
                    location_cost_rate=approx_burn_rate
                )

                # Save execution result to SQLite Database
                log_id = save_mission_log(
                    location_name=target_loc,
                    weather_mode=weather_mode,
                    target_language=selected_language,
                    rain_mm=telemetry.rain,
                    temperature=telemetry.temp,
                    stunt_status=physics.stunt_status,
                    blueprint_text=final_blueprint
                )
                
                # Persist into Session State
                st.session_state["active_blueprint"] = final_blueprint
                st.session_state["active_stunt_status"] = physics.stunt_status
                st.session_state["active_loc"] = target_loc
                st.session_state["active_weather_mode"] = weather_mode
                st.session_state["sms_dispatched"] = False
                
                status.update(label=f"✅ Live Recon & Production Blueprint Ready! (Saved to DB #{log_id})", state="complete", expanded=False)

    # Persistent Display of Swarm Dispatch, WhatsApp, Crew SMS, and Export Options
    if st.session_state.get("active_blueprint"):
        bp_text = st.session_state["active_blueprint"]
        st_status = st.session_state["active_stunt_status"]
        active_loc_name = st.session_state["active_loc"]
        active_wm = st.session_state["active_weather_mode"]

        st.markdown("<br>", unsafe_allow_html=True)
        
        # High-Impact Highlighted AI Swarm Dispatch Output Card
        render_dispatch_output(bp_text, st_status)

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Export Options: Markdown (.MD) AND Printable PDF (.PDF)
        col_md, col_pdf = st.columns([1, 1])
        with col_md:
            st.download_button(
                label=f"📥 EXPORT REPORT AS MARKDOWN (.MD)",
                data=bp_text,
                file_name=f"crisis_report_{selected_language.lower()[:3]}.md",
                mime="text/markdown"
            )
        with col_pdf:
            pdf_data = generate_pdf_report(
                title="CrisisShift Production Dispatch",
                location_name=active_loc_name,
                weather_mode=active_wm,
                stunt_status=st_status,
                blueprint_text=bp_text
            )
            st.download_button(
                label=f"📄 EXPORT REPORT AS PDF (.PDF)",
                data=pdf_data,
                file_name=f"crisis_report_{selected_language.lower()[:3]}.pdf",
                mime="application/pdf"
            )

with tab_scenes:
    render_scene_manager()

with tab_history:
    render_history_tab()

with tab_testcases:
    render_test_cases_tab(gemini_key, selected_language, report_format)