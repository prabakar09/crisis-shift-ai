from dataclasses import dataclass
from typing import Optional, List
import datetime

@dataclass
class TelemetryData:
    status: str
    lat: float
    lon: float
    resolved_name: str
    temp: str
    rain: float
    precip: float
    humidity: str
    wind: str
    summary: str

@dataclass
class PhysicsAssessment:
    sky_state: str
    road_grip: str
    soil_state: str
    stunt_status: str
    status_color: str

@dataclass
class ReconMissionLog:
    id: Optional[int]
    timestamp: str
    location_name: str
    weather_mode: str
    target_language: str
    rain_mm: float
    temperature: str
    stunt_status: str
    blueprint_text: str

@dataclass
class FilmScene:
    id: Optional[int]
    scene_number: str
    location: str
    description: str
    risk_level: str
    status: str

@dataclass
class CrewContact:
    id: Optional[int]
    name: str
    role: str
    phone: str
    department: str
