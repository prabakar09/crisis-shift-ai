#!/usr/bin/env python3
"""
CrisisShift OS | Autonomous Cinema Command CLI
Author: Prabakar A (@prabakar09), AI & DS, KGiSL Institute of Technology (KiTE)

Headless command-line reconnaissance and disaster contingency analyzer.
"""

import os
import sys
import argparse
from pathlib import Path

# Fix Windows console UTF-8 unicode encoding for emojis
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ensure package directory is on path
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

from database.db import init_db, save_mission_log
from backend.telemetry_service import fetch_telemetry_data, evaluate_physics
from backend.cost_calculator import calculate_production_burn_rate
from backend.agent_swarm import run_director_swarm

def main():
    parser = argparse.ArgumentParser(
        description="CrisisShift OS — Autonomous Cinema Operations & Disaster Pivot CLI"
    )
    parser.add_argument(
        "--location", "-l",
        type=str,
        default="Coimbatore, India",
        help="Shooting location or coordinates"
    )
    parser.add_argument(
        "--scene", "-s",
        type=str,
        default="Scene 54 (EXT. DAY): High-speed vehicle chase with Technocrane and 20 stunt drivers.",
        help="Scene breakdown and scheduled assets"
    )
    parser.add_argument(
        "--mode", "-m",
        type=str,
        default="live",
        choices=["live", "rain", "fog"],
        help="Weather simulation mode: live, rain (cloudburst demo), fog"
    )
    parser.add_argument(
        "--lang",
        type=str,
        default="English",
        choices=["English", "Tanglish", "Tamil"],
        help="Directorial dispatch output language"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=os.getenv("GEMINI_API_KEY", ""),
        help="Google Gemini API key (optional, falls back to offline engine)"
    )

    args = parser.parse_args()

    # Map mode string to internal mode
    mode_map = {
        "live": "🛰️ Live Orbital Radar (Actual 100% Live)",
        "rain": "⛈️ Sudden Cloudburst / Heavy Rain (Demo Crisis)",
        "fog": "🌫️ Dense Fog & Mist (Lens Caution)"
    }
    weather_mode = mode_map.get(args.mode, mode_map["live"])

    print("=" * 70)
    print("🎬 CRISISSHIFT OS | AUTONOMOUS CINEMA DISPATCH ENGINE")
    print(f"Author: Prabakar A (@prabakar09) | KGiSL Institute of Technology (KiTE)")
    print("=" * 70)
    print(f"📍 Target Location: {args.location}")
    print(f"🎬 Scheduled Scene: {args.scene}")
    print(f"🌧️ Weather Feed:   {weather_mode}")
    print(f"🗣️ Output Language: {args.lang}")
    print("-" * 70)

    # Initialize DB
    init_db()

    # Step 1: Telemetry
    print("🛰️ Agent 1 (Satellite Scout): Querying orbital telemetry...")
    telemetry = fetch_telemetry_data(args.location, weather_mode)
    print(f"   Status: {telemetry.summary}")

    # Step 2: Ground Physics
    print("🔬 Agent 2 (Physics Engine): Evaluating surface asphalt friction...")
    physics = evaluate_physics(telemetry)
    print(f"   Sky:    {physics.sky_state}")
    print(f"   Grip:   {physics.road_grip}")
    print(f"   Status: {physics.stunt_status}")

    # Step 3: Production Burn
    cost_info = calculate_production_burn_rate(physics.stunt_status, telemetry.rain, location_name=args.location)
    approx_burn = f"{cost_info['hourly_burn']} ({cost_info['location_tier']})"
    print(f"💰 Production Set Burn: {approx_burn}")
    if "HALT" in physics.stunt_status.upper() or "RED" in physics.stunt_status.upper():
        print(f"   🚨 Total Delay Exposure: {cost_info['total_financial_loss']}")
        print(f"   ✅ Saved by Pivot:       {cost_info['budget_saved_by_pivot']}")
        print(f"   🔄 Contingency:          {cost_info['contingency_scene']}")

    # Step 4: Director Swarm
    print("🧠 Agent 3 & 4 (Director Swarm & Dispatcher): Generating Call Sheet...")
    blueprint = run_director_swarm(
        api_key=args.api_key,
        location_input=args.location,
        scene_input=args.scene,
        telemetry=telemetry,
        physics=physics,
        selected_language=args.lang,
        report_format="⚡ 1-Minute Executive Flash (Short)",
        location_cost_rate=approx_burn
    )

    # Save to DB
    log_id = save_mission_log(
        location_name=args.location,
        weather_mode=weather_mode,
        target_language=args.lang,
        rain_mm=telemetry.rain,
        temperature=telemetry.temp,
        stunt_status=physics.stunt_status,
        blueprint_text=blueprint
    )

    print("-" * 70)
    print(blueprint)
    print("-" * 70)
    print(f"✅ Mission Log #{log_id} recorded in SQLite database.")
    print("=" * 70)

if __name__ == "__main__":
    main()
