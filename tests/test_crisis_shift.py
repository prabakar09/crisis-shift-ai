"""
Unit tests for CrisisShift OS (07_crisis_shift_ai).
Author: Prabakar A (@prabakar09), AI & DS, KGiSL Institute of Technology (KiTE)
"""

import os
import pytest
from pathlib import Path

# Add project root to sys.path
PROJECT_DIR = Path(__file__).resolve().parent.parent
import sys
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from database.models import TelemetryData, PhysicsAssessment
from database.db import (
    init_db,
    save_mission_log,
    get_mission_logs,
    get_film_scenes,
    add_film_scene,
    get_crew_contacts,
    add_crew_contact
)
from backend.telemetry_service import fetch_telemetry_data, evaluate_physics, safe_float
from backend.cost_calculator import classify_location_tier, calculate_production_burn_rate
from backend.pdf_exporter import generate_pdf_report, sanitize_pdf_text
from backend.agent_swarm import generate_offline_fallback_blueprint, run_director_swarm

def test_telemetry_cloudburst_mode():
    """Verify simulated cloudburst generates severe precipitation metrics."""
    data = fetch_telemetry_data("Coimbatore", "⛈️ Sudden Cloudburst / Heavy Rain (Demo Crisis)")
    assert data.rain >= 10.0
    assert "°C" in data.temp
    assert "km/h" in data.wind
    assert "Coimbatore" in data.summary

def test_telemetry_fog_mode():
    """Verify simulated dense fog generates high humidity and low rain."""
    data = fetch_telemetry_data("Ooty", "🌫️ Dense Fog & Mist (Lens Caution)")
    assert data.rain <= 1.0
    assert "98" in str(data.humidity)

def test_physics_evaluation_halt_on_rain():
    """Verify rain > 1.0mm triggers severe weather halt and slick road friction."""
    telemetry = TelemetryData(
        status="success",
        lat=11.0,
        lon=77.0,
        resolved_name="Test Location",
        temp="24°C",
        rain=15.0,
        precip=15.0,
        humidity="95%",
        wind="30 km/h",
        summary="Test rain"
    )
    physics = evaluate_physics(telemetry)
    assert "HALT" in physics.stunt_status
    assert "0.32" in physics.road_grip
    assert physics.status_color == "#FF0055"

def test_physics_evaluation_clear_green_light():
    """Verify clear weather produces optimal friction and full green light."""
    telemetry = TelemetryData(
        status="success",
        lat=11.0,
        lon=77.0,
        resolved_name="Test Location",
        temp="29°C",
        rain=0.0,
        precip=0.0,
        humidity="60%",
        wind="10 km/h",
        summary="Test clear"
    )
    physics = evaluate_physics(telemetry)
    assert "GREEN" in physics.stunt_status
    assert "0.85" in physics.road_grip
    assert physics.status_color == "#00FF66"

def test_classify_location_tier():
    """Verify cinema location tier classification across global, metro, hill, and regional hubs."""
    london = classify_location_tier("London Film Studio")
    assert "Global" in london["tier"]

    chennai = classify_location_tier("Chennai Marina Beach")
    assert "Metro" in chennai["tier"]

    ooty = classify_location_tier("Ooty Mountain Pass")
    assert "Hill" in ooty["tier"]

    coimbatore = classify_location_tier("Thudiyalur, Coimbatore")
    assert "Regional" in coimbatore["tier"]

def test_calculate_production_burn_rate():
    """Verify hourly burn rate, financial exposure, and pivot savings on halt."""
    result = calculate_production_burn_rate(
        stunt_status="🔴 SEVERE WEATHER HALT — ABORT EXTERIOR RUNS",
        rain_mm=12.5,
        location_name="Chennai Studio",
        crew_size=70
    )
    assert "₹" in result["hourly_burn"]
    assert "Lakhs" in result["total_financial_loss"]
    assert "Lakhs" in result["budget_saved_by_pivot"]
    assert "Soundstage A" in result["contingency_scene"]
    assert result["halt_hours"] > 0

def test_database_crud_operations():
    """Verify database initialization, scene insertion, contact retrieval, and log persistence."""
    init_db()

    scenes = get_film_scenes()
    assert len(scenes) >= 3

    new_id = add_film_scene("Scene 101 (EXT. DUSK)", "Coimbatore Bypass", "High-speed pursuit", "HIGH")
    assert new_id is not None
    updated_scenes = get_film_scenes()
    assert any(s.scene_number == "Scene 101 (EXT. DUSK)" for s in updated_scenes)

    contacts = get_crew_contacts()
    assert len(contacts) >= 4
    stunt_leads = [c for c in contacts if "Stunt" in c.role or "Stunts" in c.department]
    assert len(stunt_leads) > 0

    log_id = save_mission_log(
        location_name="Coimbatore",
        weather_mode="Test Mode",
        target_language="Tanglish",
        rain_mm=5.0,
        temperature="26°C",
        stunt_status="🔴 SEVERE WEATHER HALT",
        blueprint_text="Test blueprint content"
    )
    assert log_id > 0

    logs = get_mission_logs(limit=5)
    assert any(l.id == log_id for l in logs)

def test_pdf_report_generation():
    """Verify PDF generator produces valid PDF byte stream with Unicode emoji sanitization."""
    raw_text = "🎬 Test Cinema Dispatch with emojis ⛈️ 🔴 and special characters."
    clean = sanitize_pdf_text(raw_text)
    assert "[CINEMA]" in clean
    assert "[HALT]" in clean

    pdf_bytes = generate_pdf_report(
        title="Production Safety Dispatch",
        location_name="Marina Beach, Chennai",
        weather_mode="Simulated Fog",
        stunt_status="🟡 CAUTION",
        blueprint_text=raw_text
    )
    assert isinstance(pdf_bytes, bytes)
    assert pdf_bytes.startswith(b"%PDF")
    assert len(pdf_bytes) > 500

def test_agent_swarm_fallback_tanglish_and_tamil():
    """Verify offline fallback produces valid Tanglish and Tamil directorial blueprints."""
    telemetry = TelemetryData(
        status="success",
        lat=11.0,
        lon=77.0,
        resolved_name="Coimbatore Highway",
        temp="24°C",
        rain=18.0,
        precip=18.0,
        humidity="95%",
        wind="32 km/h",
        summary="Rain storm"
    )
    physics = evaluate_physics(telemetry)

    # Tanglish Test
    tanglish_bp = generate_offline_fallback_blueprint(
        location_input="Coimbatore",
        scene_input="Car chase",
        telemetry=telemetry,
        physics=physics,
        selected_language="Tanglish (Tamil in English)",
        report_format="⚡ 1-Minute Executive Flash (Short)",
        location_cost_rate="₹2.8L/hr"
    )
    assert "Technocrane" in tanglish_bp
    assert "Soundstage" in tanglish_bp
    assert "HALT" in tanglish_bp

    # Tamil Test
    tamil_bp = generate_offline_fallback_blueprint(
        location_input="Coimbatore",
        scene_input="Car chase",
        telemetry=telemetry,
        physics=physics,
        selected_language="Tamil (தமிழ்)",
        report_format="⚡ 1-Minute Executive Flash (Short)",
        location_cost_rate="₹2.8L/hr"
    )
    assert "படப்பிடிப்பு" in tamil_bp
    assert "நிறுத்தம்" in tamil_bp
