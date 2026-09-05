from typing import Dict, Any

def classify_location_tier(location_name: str) -> Dict[str, Any]:
    """
    Classifies a shooting location into cinema industry production cost tiers.
    """
    loc = location_name.lower().strip() if location_name else "regional"
    
    # Tier 1: International Global Shooting Hubs
    intl_cities = [
        "london", "new york", "los angeles", "hollywood", "tokyo", "dubai", 
        "paris", "sydney", "berlin", "toronto", "vancouver", "singapore", 
        "rome", "bangkok", "zurich", "usa", "uk"
    ]
    # Tier 2: Indian Metro & Cinema Capitals
    metro_cities = [
        "mumbai", "chennai", "hyderabad", "bangalore", "bengaluru", 
        "kolkata", "delhi", "new delhi", "noida", "kochi", "pune", 
        "film city", "ramoji", "ahmedabad"
    ]
    # Tier 3: Hill Stations & Eco/Forest Mountain Logistics
    hill_stations = [
        "ooty", "udhagamandalam", "kodaikanal", "munnar", "leh", "ladakh", 
        "valparai", "manali", "shimla", "coorg", "darjeeling", "rishikesh", 
        "wayanad", "yercaud", "goa"
    ]
    
    if any(city in loc for city in intl_cities):
        return {
            "tier": "Global International Film Hub",
            "tier_badge": "🌐 GLOBAL TIER-1 HUB",
            "actor_hourly": 350000,
            "crew_rate_per_tech": 2500,
            "gear_hourly": 110000,
            "permit_hourly": 120000,
            "logistics_note": "Foreign Film Commission permits, local overseas union scale, and freight clearance."
        }
    elif any(city in loc for city in metro_cities):
        return {
            "tier": "Metro Cinema Capital (Tier-1 Studio)",
            "tier_badge": "🏛️ TIER-1 METRO CAPITAL",
            "actor_hourly": 220000,
            "crew_rate_per_tech": 1400,
            "gear_hourly": 65000,
            "permit_hourly": 50000,
            "logistics_note": "Metropolitan Corporation police road-block permits, FEFSI/FWICE guild rates, and high-demand rigs."
        }
    elif any(city in loc for city in hill_stations):
        return {
            "tier": "High-Altitude Hill Station / Forest Logistics",
            "tier_badge": "⛰️ HILL / FOREST ECO-ZONE",
            "actor_hourly": 200000,
            "crew_rate_per_tech": 1300,
            "gear_hourly": 60000,
            "permit_hourly": 45000,
            "logistics_note": "Forest Department eco-clearance, mountain generator convoy, and high-altitude cold weather gear."
        }
    else:
        # Tier 4: Regional Cinema Hub / Tier-2 City (Salem, Coimbatore, Madurai, Trichy, etc.)
        return {
            "tier": "Regional Production Center (Tier-2 Hub)",
            "tier_badge": "📍 REGIONAL CINEMA HUB",
            "actor_hourly": 160000,
            "crew_rate_per_tech": 950,
            "gear_hourly": 40000,
            "permit_hourly": 20000,
            "logistics_note": "Regional district collectorate road permits, regional guild crew, and local base camp logistics."
        }

def calculate_production_burn_rate(
    stunt_status: str,
    rain_mm: float,
    location_name: str = "Regional Production Hub",
    crew_size: int = 65,
    lead_actors_count: int = 2
) -> Dict[str, Any]:
    """
    Computes real-time location-aware film production burn rate, delay cost exposure,
    and recommends autonomous indoor soundstage contingency swaps.
    """
    tier_info = classify_location_tier(location_name)
    
    actor_cost = tier_info["actor_hourly"] * (lead_actors_count / 2)
    crew_cost = tier_info["crew_rate_per_tech"] * crew_size
    gear_cost = tier_info["gear_hourly"]
    permit_cost = tier_info["permit_hourly"]
    
    total_hourly_burn = actor_cost + crew_cost + gear_cost + permit_cost
    hourly_burn_formatted = f"₹{total_hourly_burn / 100000:.2f} Lakhs / hr"
    
    safe_loc = (location_name or "Regional Production Hub").strip()
    safe_loc_title = safe_loc.title() if safe_loc else "Regional Production Hub"
    status_upper = (stunt_status or "").upper()
    
    if "HALT" in status_upper or "RED" in status_upper or rain_mm > 1.0:
        halt_hours = 4.5 if rain_mm > 10.0 else 3.0
        total_loss = total_hourly_burn * halt_hours
        budget_saved_by_pivot = total_loss * 0.78
        
        contingency_scene = "Scene 88 (INT. DAY) — Studio Soundstage A (Dialogue sequence between leads)"
        action_plan = (
            f"🚨 CRITICAL PRODUCTION EXPOSURE: Outdoor shoot halt at {safe_loc_title} creates "
            f"₹{total_loss / 100000:.2f} Lakhs financial loss across {halt_hours} hours. "
            f"AUTONOMOUS CONTINGENCY: Instantly pivot crew & cast to {contingency_scene}. "
            f"Pivoting saves ₹{budget_saved_by_pivot / 100000:.2f} Lakhs in lost production budget!"
        )
        risk_level = "CRITICAL FINANCIAL HAZARD"
        risk_color = "#FF3366"
    elif "CAUTION" in status_upper:
        halt_hours = 1.0
        total_loss = total_hourly_burn * halt_hours
        budget_saved_by_pivot = total_loss * 0.5
        action_plan = (
            f"⚠️ MODERATE DELAY RISK: 1-hour anti-fog warmup and traction test at {safe_loc_title} creates "
            f"₹{total_loss / 100000:.2f} Lakhs buffer. Proceed with low-speed test before full stunts."
        )
        contingency_scene = "Maintain current location with warm lens covers."
        risk_level = "MODERATE DELAY BUFFER"
        risk_color = "#FFD000"
    else:
        halt_hours = 0.0
        total_loss = 0.0
        budget_saved_by_pivot = 0.0
        action_plan = f"🟢 OPTIMAL BUDGET EFFICIENCY: Zero downtime detected at {safe_loc_title}. Proceed with full exterior shooting schedule."
        contingency_scene = "None required. Exterior clearance 100% active."
        risk_level = "OPTIMAL (ZERO LOSS)"
        risk_color = "#00FF66"
        
    return {
        "location_name": safe_loc_title,
        "location_tier": tier_info["tier"],
        "tier_badge": tier_info["tier_badge"],
        "logistics_note": tier_info["logistics_note"],
        "hourly_burn": hourly_burn_formatted,
        "halt_hours": halt_hours,
        "total_financial_loss": f"₹{total_loss / 100000:.2f} Lakhs" if total_loss > 0 else "₹0.00",
        "budget_saved_by_pivot": f"₹{budget_saved_by_pivot / 100000:.2f} Lakhs" if budget_saved_by_pivot > 0 else "₹0.00",
        "contingency_scene": contingency_scene,
        "action_plan": action_plan,
        "risk_level": risk_level,
        "risk_color": risk_color,
        "crew_size": crew_size,
        "cast_cost": f"₹{actor_cost / 100000:.2f}L/hr",
        "crew_cost": f"₹{crew_cost / 100000:.2f}L/hr",
        "gear_cost": f"₹{gear_cost / 100000:.2f}L/hr",
        "permit_cost": f"₹{permit_cost / 100000:.2f}L/hr"
    }
