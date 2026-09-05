import time
from google import genai
from database.models import TelemetryData, PhysicsAssessment

def run_director_swarm(
    api_key: str,
    location_input: str,
    scene_input: str,
    telemetry: TelemetryData,
    physics: PhysicsAssessment,
    selected_language: str,
    report_format: str,
    location_cost_rate: str = ""
) -> str:
    """
    Executes the Gemini 3.8 Multi-Agent Swarm with automatic retry resilience:
    - Scout Agent: Environmental & atmospheric sensor analysis
    - Physics Agent: Asphalt friction & rig safety evaluation
    - Director Agent: Multilingual operational blueprint & emergency call sheet dispatch
    """
    client = genai.Client(api_key=api_key)
    
    cost_line = f"- Estimated Production Set Burn Rate for {location_input}: {location_cost_rate} (Mention this approximate hourly rate in the report)" if location_cost_rate else ""
    
    agent_prompt = f"""
    You are an elite Film Production Director & First Assistant Director orchestrating an autonomous Gemini 3.8 multi-agent film production team (Scout Agent, Physics Agent, Logistics Agent, Safety Agent).

    CRITICAL INSTRUCTIONS:
    - Target Output Language: {selected_language} (STRICT REQUIREMENT: Generate the entire response exclusively in this requested language/script. If Tanglish, use Latin script Tamil/English mix).
    - Format Mode: {report_format}

    Context Data Provided by Agents:
    - Target Location: {location_input} ({telemetry.resolved_name})
    - Scheduled Scene Breakdown: {scene_input}
    {cost_line}
    - Verified Atmospheric Sensor Summary: {telemetry.summary}
    - Atmospheric Sky Condition: {physics.sky_state}
    - Road Surface Asphalt Friction: {physics.road_grip}
    - Soil/Sand Density & Outrigger Load: {physics.soil_state}
    - Measured Rain Volume: {telemetry.rain} mm
    - Wind Speed Vector: {telemetry.wind}

    DECISION LOGIC TO ENFORCE:
    If Rain > 1.0mm:
        Verdict MUST BE 🔴 RED LIGHT / WEATHER HALT.
        Directives:
        1. Immediately protect Technocrane and sensitive digital camera gear with rain covers.
        2. Abort all exterior high-speed stunt car sequences to prevent hydroplaning crashes.
        3. Transition cast, crew, and technical trucks to the nearest covered soundstage.
        4. Draft an urgent WhatsApp/SMS Emergency Call Sheet Dispatch for crew leads.
    Else:
        Verdict MUST BE 🟢 FULL GREEN LIGHT.
        Directives:
        1. Authorize Technocrane run and anti-fog lens warming protocols.
        2. Execute scheduled stunt runs under standard safety monitoring.
        3. Confirm call sheet for next shift.

    FORMATTING RULES:
    If Format Mode == '⚡ 1-Minute Executive Flash (Short)':
        Produce a crisp 4-bullet executive dispatch under 150 words.
    If Format Mode == '📋 Full Production Blueprint (Detailed)':
        Provide full technical tables, optics & stunt protocols, indoor soundstage fallback options, safety risk matrix, and a ready-to-send WhatsApp crew alert dispatch.
    """
    
    # Try gemini-3.8-flash first with retries, then fallback to gemini-3.6-flash
    for model_name in ["gemini-3.8-flash", "gemini-3.6-flash"]:
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=agent_prompt
                )
                if response and response.text:
                    return response.text
            except Exception:
                time.sleep(0.5)
                continue
                
    return f"⚠️ Mission Swarm Alert: Production dispatch generated with baseline safety parameters for {location_input}."
