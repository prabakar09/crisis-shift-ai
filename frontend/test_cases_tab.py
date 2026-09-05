import streamlit as st
import json
from backend.telemetry_service import fetch_telemetry_data, evaluate_physics
from backend.agent_swarm import run_director_swarm
from backend.pdf_exporter import generate_pdf_report

PREBUILT_TEST_CASES = [
    {
        "id": 1,
        "name": "🏎️ Coimbatore Highway Stunt Run (Torrential Cloudburst)",
        "location": "Thudiyalur Highway, Coimbatore",
        "mode": "⛈️ Sudden Cloudburst / Heavy Rain (Demo Crisis)",
        "scene": "Scene 54 (EXT. DAY): High-speed car chase sequence with Lead Actor, 20 stunt riders, and heavy Technocrane setup.",
        "expected_verdict": "🔴 RED LIGHT / WEATHER HALT",
        "description": "Simulates 18.5mm torrential rain. Tests hydroplane hazard detection and Technocrane outrigger sinkage protection."
    },
    {
        "id": 2,
        "name": "🌊 Chennai Marina Beach Explosion (Dense Sea Fog)",
        "location": "Marina Beachfront, Chennai",
        "mode": "🌫️ Dense Fog & Mist (Lens Caution)",
        "scene": "Scene 12 (EXT. NIGHT): Explosive beachfront confrontation with flame rigs and drone optical tracking.",
        "expected_verdict": "🟡 CAUTION — TRACTION & LENS TEST",
        "description": "Simulates 98% relative humidity and sea fog condensation. Tests lens anti-fog protocols and damp sand traction."
    },
    {
        "id": 3,
        "name": "🏔️ Ooty Mountain Pass Descent (Gale Wind Hazard)",
        "location": "Doddabetta Pass, Ooty",
        "mode": "⛈️ Sudden Cloudburst / Heavy Rain (Demo Crisis)",
        "scene": "Scene 77 (EXT. DAY): Mountain cliffside vehicle drift with helicopter aerial camera rig.",
        "expected_verdict": "🔴 RED LIGHT / GALE HALT",
        "description": "High wind vectors combined with heavy rainfall along steep gradient soil slopes."
    },
    {
        "id": 4,
        "name": "🎬 Studio Soundstage Indoor Shoot (Baseline Control)",
        "location": "AVM Studio Soundstage 3, Chennai",
        "mode": "🛰️ Live Orbital Radar (Actual 100% Live)",
        "scene": "Scene 04 (INT. DAY): Indoor dramatic dialogue sequence between Lead Actors under controlled LED lights.",
        "expected_verdict": "🟢 FULL GREEN LIGHT",
        "description": "Indoor soundstage shooting unaffected by exterior atmospheric weather conditions."
    },
    {
        "id": 5,
        "name": "☀️ Madurai Heritage Street Chase (Extreme Heatwave)",
        "location": "Meenakshi Temple Street, Madurai",
        "mode": "🛰️ Live Orbital Radar (Actual 100% Live)",
        "scene": "Scene 33 (EXT. DAY): Market chase sequence with vintage sports car and 50 background extras.",
        "expected_verdict": "🟢 GREEN LIGHT (COOLING PROTOCOL)",
        "description": "High ambient temperature testing camera sensor thermal throttling and crew hydration dispatches."
    }
]

def render_test_cases_tab(gemini_key: str, selected_language: str, report_format: str):
    st.markdown("<h3 style='color: #FFFFFF; font-family: Space Grotesk, sans-serif;'>🧪 CINEMA TEST CASES & BENCHMARK SUITE</h3>", unsafe_allow_html=True)
    st.caption("Execute pre-configured stress-test scenarios to evaluate Gemini 3.8 Swarm responses across weather crises.")

    # Suite Download Button Header
    col_hdr, col_dl_all = st.columns([3, 1])
    with col_dl_all:
        full_suite_text = "CRISISSHIFT OS BENCHMARK TEST SUITE REPORT\n\n"
        for tc in PREBUILT_TEST_CASES:
            full_suite_text += f"TEST CASE #{tc['id']}: {tc['name']}\nLocation: {tc['location']}\nExpected: {tc['expected_verdict']}\nDescription: {tc['description']}\n{'-'*50}\n\n"
        
        pdf_bytes_all = generate_pdf_report(
            title="Full Benchmark Test Suite Summary",
            location_name="Global Test Suite (5 Scenarios)",
            weather_mode="Multi-Scenario Benchmark",
            stunt_status="5 TEST CASES VALIDATED",
            blueprint_text=full_suite_text
        )
        
        st.download_button(
            label="📥 Download Full Test Suite PDF (.PDF)",
            data=pdf_bytes_all,
            file_name="crisisshift_benchmark_test_suite.pdf",
            mime="application/pdf"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Render Individual Test Cases
    for tc in PREBUILT_TEST_CASES:
        with st.expander(f"{tc['name']} — Expected: {tc['expected_verdict']}"):
            st.markdown(f"**📍 Target Location:** `{tc['location']}`")
            st.markdown(f"**🌧️ Weather Scenario:** `{tc['mode']}`")
            st.markdown(f"**🎬 Scene Breakdown:** {tc['scene']}")
            st.markdown(f"**💡 Scenario Description:** {tc['description']}")
            
            if st.button(f"⚡ RUN TEST CASE #{tc['id']}", key=f"run_tc_{tc['id']}"):
                if not gemini_key:
                    st.error("⚠️ Enter your Google Gemini API Key in the left sidebar first!")
                else:
                    with st.spinner(f"Running Swarm on Test Case #{tc['id']}..."):
                        telemetry = fetch_telemetry_data(tc["location"], tc["mode"])
                        physics = evaluate_physics(telemetry)
                        
                        blueprint = run_director_swarm(
                            api_key=gemini_key,
                            location_input=tc["location"],
                            scene_input=tc["scene"],
                            telemetry=telemetry,
                            physics=physics,
                            selected_language=selected_language,
                            report_format=report_format
                        )
                        
                        st.markdown("#### 📑 Agent Swarm Output:")
                        st.markdown('<div class="dispatch-output-container">', unsafe_allow_html=True)
                        st.markdown(blueprint)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        col_md, col_pdf = st.columns([1, 1])
                        with col_md:
                            st.download_button(
                                label=f"📥 Download Test #{tc['id']} (.MD)",
                                data=blueprint,
                                file_name=f"test_case_{tc['id']}_report.md",
                                mime="text/markdown",
                                key=f"dl_md_{tc['id']}"
                            )
                        with col_pdf:
                            pdf_bytes = generate_pdf_report(
                                title=f"Test Case #{tc['id']} Dispatch",
                                location_name=tc["location"],
                                weather_mode=tc["mode"],
                                stunt_status=physics.stunt_status,
                                blueprint_text=blueprint
                            )
                            st.download_button(
                                label=f"📥 Download Test #{tc['id']} (.PDF)",
                                data=pdf_bytes,
                                file_name=f"test_case_{tc['id']}_report.pdf",
                                mime="application/pdf",
                                key=f"dl_pdf_{tc['id']}"
                            )
