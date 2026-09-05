import streamlit as st
from database.db import get_mission_logs, clear_mission_logs

def render_history_tab():
    st.markdown("<h3 style='color: #FFFFFF; font-family: Space Grotesk, sans-serif;'>📜 MISSION AUDIT LOGS & HISTORIC DISPATCHES</h3>", unsafe_allow_html=True)
    st.caption("Inspect past satellite reconnaissance runs, weather alerts, and AI Director verdicts saved in database.")
    
    col_hdr, col_btn = st.columns([4, 1])
    with col_btn:
        if st.button("🗑️ Clear Database Logs"):
            clear_mission_logs()
            st.success("Database logs cleared!")
            st.rerun()

    logs = get_mission_logs()
    
    if not logs:
        st.info("ℹ️ No mission logs found in database. Execute a Satellite Recon run in the Live Command HUD to populate logs.")
        return

    st.markdown(f"**Total Saved Recon Executions:** <span style='color:#FF9F00; font-weight: 800;'>{len(logs)}</span>", unsafe_allow_html=True)
    
    for item in logs:
        verdict_color = "#FF3366" if ("HALT" in item.stunt_status.upper() or "RED" in item.stunt_status.upper()) else ("#FBBF24" if "CAUTION" in item.stunt_status.upper() else "#00FF66")
        st.markdown(f"""
        <div class="history-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: 'Space Grotesk', sans-serif; font-weight: 800; font-size: 1.05rem; color: #FF9F00;">
                    📍 {item.location_name}
                </span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #94A3B8;">
                    ⏱️ {item.timestamp}
                </span>
            </div>
            <div style="margin: 8px 0; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: #E2E8F0;">
                Mode: <span style="color: #FFD000;">{item.weather_mode}</span> | 
                Rain: <span style="color: #FF3366;">{item.rain_mm} mm</span> | 
                Temp: {item.temperature} | 
                Lang: {item.target_language}
            </div>
            <div style="font-family: 'Space Grotesk', sans-serif; font-size: 0.88rem; font-weight: 700; color: {verdict_color}; margin-bottom: 8px;">
                VERDICT: {item.stunt_status}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"📑 View AI Director Blueprint Dispatch ({item.target_language})"):
            st.markdown(item.blueprint_text)
            st.download_button(
                label=f"📥 Download Dispatch #{item.id}",
                data=item.blueprint_text,
                file_name=f"crisis_report_log_{item.id}.md",
                mime="text/markdown",
                key=f"dl_btn_{item.id}"
            )
