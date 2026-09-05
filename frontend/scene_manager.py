import streamlit as st
from database.db import get_film_scenes, add_film_scene

def render_scene_manager():
    st.markdown("<h3 style='color: #FFFFFF; font-family: Space Grotesk, sans-serif;'>📋 PRODUCTION SCENE BREAKDOWN & CALL SHEET SCHEDULE</h3>", unsafe_allow_html=True)
    st.caption("Manage active scene parameters and store technical requirements into database.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("<h4 style='color: #FF9F00; font-family: Space Grotesk, sans-serif;'>🎬 Current Scenes in Database</h4>", unsafe_allow_html=True)
        scenes = get_film_scenes()
        for sc in scenes:
            risk_color = "#FF3366" if sc.risk_level in ["HIGH", "CRITICAL"] else "#00FF66"
            st.markdown(f"""
            <div class="history-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-family: 'Space Grotesk', sans-serif; font-weight: 800; font-size: 1.15rem; color: #FF9F00;">
                        {sc.scene_number}
                    </span>
                    <span style="background: rgba(255, 159, 0, 0.12); border: 1px solid {risk_color}; color: {risk_color}; padding: 3px 12px; border-radius: 20px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; font-weight: 700;">
                        RISK: {sc.risk_level}
                    </span>
                </div>
                <div style="font-size: 0.88rem; color: #F1F5F9; margin: 8px 0;">📍 <b>Location:</b> {sc.location}</div>
                <div style="font-size: 0.88rem; color: #94A3B8;">📝 {sc.description}</div>
                <div style="font-size: 0.75rem; color: #64748B; margin-top: 8px; font-family: 'JetBrains Mono', monospace;">Status: {sc.status}</div>
            </div>
            """, unsafe_allow_html=True)
            
    with col2:
        st.markdown("<h4 style='color: #FF9F00; font-family: Space Grotesk, sans-serif;'>➕ Add New Film Scene</h4>", unsafe_allow_html=True)
        with st.form("new_scene_form"):
            new_num = st.text_input("Scene Tag:", value="Scene 99 (EXT. NIGHT)")
            new_loc = st.text_input("Shooting Location:", value="Gandhipuram, Coimbatore")
            new_desc = st.text_area("Scene & Gear Description:", value="Heavy rain sequence with helicopter rig and stunt double.")
            new_risk = st.selectbox("Risk Assessment:", ["LOW", "MODERATE", "HIGH", "CRITICAL"])
            
            submitted = st.form_submit_button("➕ Save Scene to Database")
            if submitted:
                add_film_scene(new_num, new_loc, new_desc, new_risk)
                st.success(f"✅ Saved '{new_num}' to database!")
                st.rerun()
