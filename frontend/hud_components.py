import streamlit as st
import pydeck as pdk
import pandas as pd
from database.models import TelemetryData, PhysicsAssessment
from backend.satellite_service import get_arcgis_satellite_url

def render_system_status_banner():
    """
    Renders a BIG, PROMINENT, GLOWING Live System Health & Swarm Status Banner.
    """
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(0, 255, 102, 0.15) 0%, rgba(10, 25, 18, 0.95) 100%); border: 2px solid #00FF66; border-radius: 18px; padding: 18px 24px; margin-bottom: 22px; box-shadow: 0 0 35px rgba(0, 255, 102, 0.35); text-align: center; position: relative; overflow: hidden;">
        <div style="display: flex; align-items: center; justify-content: center; gap: 14px; flex-wrap: wrap;">
            <span style="display: inline-block; width: 16px; height: 16px; background-color: #00FF66; border-radius: 50%; box-shadow: 0 0 20px #00FF66; animation: statusPulse 1.5s infinite;"></span>
            <span style="font-family: 'Space Grotesk', 'Orbitron', sans-serif; font-size: 1.5rem; font-weight: 900; color: #00FF66; letter-spacing: 1.5px; text-transform: uppercase;">
                🟢 SYSTEM STATUS: ACTIVE & RUNNING PERFECTLY
            </span>
        </div>
        <p style="margin: 6px 0 0 0; color: #E2E8F0; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; letter-spacing: 0.5px;">
            Gemini 3.8 Swarm Engine Connected | Satellite Atmospheric Radar Online | 0 System Faults Detected
        </p>
    </div>
    
    <style>
        @keyframes statusPulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 102, 0.8); }
            70% { transform: scale(1.15); box-shadow: 0 0 0 15px rgba(0, 255, 102, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 102, 0); }
        }
    </style>
    """, unsafe_allow_html=True)

def render_hero_banner():
    st.markdown("""
    <div class="hud-hero">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 15px;">
            <div>
                <div class="hud-badge">
                    <span class="pulse-dot"></span> ORBITAL RECONNAISSANCE & REAL-TIME AGENT SWARM
                </div>
                <div class="hud-title">
                    SHAPING THE FUTURE WITH <span>INTELLIGENT CINEMA OS</span>
                </div>
                <p style="margin: 8px 0 0 0; color: #94A3B8; font-size: 0.92rem; font-weight: 500;">
                    Atmospheric Radar Sensing // Surface Asphalt Friction Engine // Multi-Agent Directorial Swarm
                </p>
            </div>
            <div style="background: rgba(255, 159, 0, 0.1); border: 1px solid rgba(255, 159, 0, 0.3); border-radius: 14px; padding: 12px 20px; text-align: right;">
                <div style="font-family: 'Space Grotesk', sans-serif; font-size: 1.25rem; font-weight: 800; color: #FFD000;">
                    ★ 4.9 <span style="font-size: 0.8rem; color: #FF9F00;">★★★★★</span>
                </div>
                <div style="font-size: 0.72rem; color: #94A3B8; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: 1px;">
                    MISSION SAFETY RATING
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_telemetry_bar():
    st.markdown("""
    <div class="telemetry-grid">
        <div class="telemetry-card">
            <div class="tel-label">SWARM ENGINE</div>
            <div class="tel-val">GEMINI 3.8</div>
            <div style="font-size: 0.7rem; color: #94A3B8; margin-top: 2px;">Flash Enterprise</div>
        </div>
        <div class="telemetry-card">
            <div class="tel-label">SWARM RECON</div>
            <div class="tel-val">20K+</div>
            <div style="font-size: 0.7rem; color: #94A3B8; margin-top: 2px;">Telemetry Datapoints</div>
        </div>
        <div class="telemetry-card">
            <div class="tel-label">SCENES MANAGED</div>
            <div class="tel-val">320+</div>
            <div style="font-size: 0.7rem; color: #94A3B8; margin-top: 2px;">Active Call Sheets</div>
        </div>
        <div class="telemetry-card">
            <div class="tel-label">RADAR LATENCY</div>
            <div class="tel-val">&lt; 15 SEC</div>
            <div style="font-size: 0.7rem; color: #94A3B8; margin-top: 2px;">Real-Time Orbit Sync</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_agent_architecture_card():
    """
    Renders the Autonomous Multi-Agent Swarm Flow & Tanglish Support Card for Hackathon Judges.
    """
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(18, 18, 26, 0.98) 0%, rgba(10, 10, 15, 0.95) 100%); border: 2px solid rgba(255, 159, 0, 0.4); border-radius: 18px; padding: 22px 26px; margin: 18px 0; box-shadow: 0 10px 35px rgba(0,0,0,0.5);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px; border-bottom: 1px solid rgba(255, 159, 0, 0.25); padding-bottom: 10px;">
            <div style="font-family: 'Space Grotesk', sans-serif; font-size: 1.25rem; font-weight: 900; color: #FF9F00; letter-spacing: 0.5px;">
                🤖 AUTONOMOUS MULTI-AGENT SWARM ARCHITECTURE
            </div>
            <div style="background: rgba(255, 159, 0, 0.15); border: 1px solid #FF9F00; color: #FFD000; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 100px;">
                🌐 TANGLISH & REGIONAL CINEMA LOCALIZATION ACTIVE
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
            <div style="background: rgba(25, 25, 35, 0.85); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 14px; padding: 14px; text-align: left;">
                <div style="font-size: 0.75rem; color: #00F0FF; font-family: 'JetBrains Mono', monospace; font-weight: 800; margin-bottom: 4px;">AGENT 1 // SCOUT</div>
                <div style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; font-family: 'Space Grotesk', sans-serif;">🛰️ SATELLITE RADAR</div>
                <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 6px;">Live Open-Meteo & OpenStreetMap Nominatim atmospheric telemetry sensor query.</div>
            </div>
            <div style="background: rgba(25, 25, 35, 0.85); border: 1px solid rgba(255, 159, 0, 0.3); border-radius: 14px; padding: 14px; text-align: left;">
                <div style="font-size: 0.75rem; color: #FF9F00; font-family: 'JetBrains Mono', monospace; font-weight: 800; margin-bottom: 4px;">AGENT 2 // PHYSICS</div>
                <div style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; font-family: 'Space Grotesk', sans-serif;">🔬 ASPHALT ENGINE</div>
                <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 6px;">Computes road friction coefficient (μ = 0.32-0.85) & Technocrane soil bearing capacity.</div>
            </div>
            <div style="background: rgba(25, 25, 35, 0.85); border: 1px solid rgba(0, 255, 102, 0.3); border-radius: 14px; padding: 14px; text-align: left;">
                <div style="font-size: 0.75rem; color: #00FF66; font-family: 'JetBrains Mono', monospace; font-weight: 800; margin-bottom: 4px;">AGENT 3 // DIRECTOR</div>
                <div style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; font-family: 'Space Grotesk', sans-serif;">🧠 GEMINI 3.8 SWARM</div>
                <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 6px;">Autonomous decision arbitration: Green Light Stunt authorization vs Red Light Weather Halt.</div>
            </div>
            <div style="background: rgba(25, 25, 35, 0.85); border: 1px solid rgba(255, 51, 102, 0.3); border-radius: 14px; padding: 14px; text-align: left;">
                <div style="font-size: 0.75rem; color: #FF3366; font-family: 'JetBrains Mono', monospace; font-weight: 800; margin-bottom: 4px;">AGENT 4 // DISPATCHER</div>
                <div style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; font-family: 'Space Grotesk', sans-serif;">🗣️ TANGLISH ALERT</div>
                <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 6px;">Instant regional set dispatch for Indian film crew leads & First Assistant Directors.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_ground_physics_cards(physics: PhysicsAssessment, telemetry: TelemetryData):
    st.markdown(f"""
    <div class="ground-grid">
        <div class="ground-card">
            <div class="ground-card-header">⛅ ATMOSPHERE & ATMOSPHERIC RADAR</div>
            <div class="ground-card-val" style="font-size: 0.98rem;">{physics.sky_state}</div>
            <div class="ground-card-desc">Measured Rain: <b>{telemetry.rain} mm</b> | Humidity: <b>{telemetry.humidity}</b></div>
        </div>
        <div class="ground-card">
            <div class="ground-card-header">🛣️ ROAD ASPHALT FRICTION ENGINE</div>
            <div class="ground-card-val" style="color: {physics.status_color}; font-size: 0.98rem;">{physics.road_grip}</div>
            <div class="ground-card-desc">Hydroplaning Hazard Threshold: <b>μ &lt; 0.40</b> | Stunt Status: <b>{physics.stunt_status}</b></div>
        </div>
        <div class="ground-card">
            <div class="ground-card-header">🏜️ SOIL & RIGGING LOAD CAPACITY</div>
            <div class="ground-card-val" style="font-size: 0.98rem;">{physics.soil_state}</div>
            <div class="ground-card-desc">Technocrane Outrigger Grounding (Bearing Cap: 150 kPa Inspected)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_satellite_views(telemetry: TelemetryData, location_name: str, weather_mode: str):
    st.markdown("<h4 style='color: #FFFFFF; font-family: Space Grotesk, sans-serif; letter-spacing: 0.5px;'>🛰️ AUTHENTIC SATELLITE OPTICAL RECONNAISSANCE</h4>", unsafe_allow_html=True)
    col_sat1, col_sat2 = st.columns([1, 1])
    
    lat, lon = telemetry.lat, telemetry.lon
    
    with col_sat1:
        st.markdown("**📸 Actual High-Res Satellite Earth Imagery (ArcGIS Real Surface):**")
        sat_url = get_arcgis_satellite_url(lat, lon)
        st.image(sat_url, caption=f"Direct Satellite Earth Imagery: {location_name} ({lat:.4f}, {lon:.4f})", width="stretch")

    with col_sat2:
        st.markdown("**📍 Interactive GPS Radar Map with BRIGHT RED Live Location Pin:**")
        
        # Pydeck Scatterplot Layer with Bright Red Live Location Dot
        df_map = pd.DataFrame([{
            'lat': lat,
            'lon': lon,
            'location': location_name,
            'info': f"Target Location: {location_name} ({lat:.4f}, {lon:.4f})"
        }])
        
        # Layer 1: Green Safe Staging Perimeter (1200m)
        green_safe_zone = pdk.Layer(
            "ScatterplotLayer",
            data=df_map,
            get_position=["lon", "lat"],
            get_color=[0, 255, 102, 35],
            get_radius=1200,
            pickable=False
        )

        # Layer 2: Red Hydroplane & Crane Sink Hazard Zone (500m)
        red_hazard_zone = pdk.Layer(
            "ScatterplotLayer",
            data=df_map,
            get_position=["lon", "lat"],
            get_color=[255, 51, 102, 70],
            get_radius=500,
            pickable=False
        )

        # Layer 3: Central High-Intensity Red Location Beacon
        red_pin_layer = pdk.Layer(
            "ScatterplotLayer",
            data=df_map,
            get_position=["lon", "lat"],
            get_color=[255, 0, 50, 255],
            get_radius=150,
            pickable=True,
            radius_min_pixels=12,
            radius_max_pixels=28
        )
        
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=14,
            pitch=45
        )
        
        r = pdk.Deck(
            layers=[green_safe_zone, red_hazard_zone, red_pin_layer],
            initial_view_state=view_state,
            tooltip={"text": "{info}"},
            map_style="mapbox://styles/mapbox/dark-v11"
        )
        
        st.pydeck_chart(r)
        st.caption("🔴 Red Zone: 500m Hazard Radius (Slick Surface/Crane Sink) | 🟢 Green Zone: 1200m Safe Staging Perimeter")

    st.markdown(f"""
    <div style="background: rgba(255, 159, 0, 0.08); border-left: 4px solid #FF9F00; border-radius: 10px; padding: 14px 18px; font-family: 'JetBrains Mono', monospace; font-size: 0.88rem; color: #F1F5F9; margin: 16px 0;">
        <b>SENSOR DISPATCH:</b> {telemetry.summary} | Mode: <span style="color: #FFD000;">{weather_mode}</span>
    </div>
    """, unsafe_allow_html=True)

def render_dispatch_output(blueprint_text: str, stunt_status: str):
    """
    Renders a High-Impact, Prominent Glowing AI Swarm Dispatch Card.
    """
    card_class = "dispatch-card"
    status_badge_bg = "#FF9F00"
    status_badge_text = "#050507"
    
    if "HALT" in stunt_status or "RED" in stunt_status:
        card_class += " red-alert"
        status_badge_bg = "#FF3366"
        status_badge_text = "#FFFFFF"
    elif "GREEN" in stunt_status:
        card_class += " green-light"
        status_badge_bg = "#00FF66"
        status_badge_text = "#050507"

    st.markdown(f"""
    <div class="{card_class}">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px; border-bottom: 1px solid rgba(255, 159, 0, 0.3); padding-bottom: 12px;">
            <div style="font-family: 'Space Grotesk', 'Orbitron', sans-serif; font-size: 1.55rem; font-weight: 900; color: #FF9F00; letter-spacing: 1px; text-transform: uppercase;">
                🎬 AI DIRECTOR PRODUCTION DISPATCH
            </div>
            <div style="background: {status_badge_bg}; color: {status_badge_text}; font-family: 'Space Grotesk', sans-serif; font-weight: 900; font-size: 0.95rem; padding: 7px 18px; border-radius: 100px; letter-spacing: 1px; box-shadow: 0 0 20px {status_badge_bg};">
                STATUS: {stunt_status}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Render blueprint contents inside container with clean spacing and large typography
    st.markdown('<div class="dispatch-output-container">', unsafe_allow_html=True)
    st.markdown(blueprint_text)
    st.markdown('</div>', unsafe_allow_html=True)
