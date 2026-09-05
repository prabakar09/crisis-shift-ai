import sqlite3
import datetime
from typing import List, Optional
from database.models import ReconMissionLog, FilmScene, CrewContact

DB_PATH = "crisis_shift.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        # Mission Logs Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mission_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            location_name TEXT NOT NULL,
            weather_mode TEXT NOT NULL,
            target_language TEXT NOT NULL,
            rain_mm REAL NOT NULL,
            temperature TEXT NOT NULL,
            stunt_status TEXT NOT NULL,
            blueprint_text TEXT NOT NULL
        )
        """)
        
        # Film Scenes Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS film_scenes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scene_number TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL,
            risk_level TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """)
        
        # Seed default scenes if table is empty
        cursor.execute("SELECT COUNT(*) as count FROM film_scenes")
        if cursor.fetchone()["count"] == 0:
            default_scenes = [
                ("Scene 54 (EXT. DAY)", "Thudiyalur Highway, Coimbatore", "High-speed car chase sequence with Lead Actor, 20 stunt riders, and heavy Technocrane setup.", "HIGH", "SCHEDULED"),
                ("Scene 12 (EXT. NIGHT)", "Marina Beach, Chennai", "Explosive beachfront confrontation with flame rigs and drone optics.", "CRITICAL", "PENDING_RECON"),
                ("Scene 88 (INT. DAY)", "Studio Soundstage A", "Dialogue scene between leads. Weather independent.", "LOW", "STANDBY")
            ]
            cursor.executemany(
                "INSERT INTO film_scenes (scene_number, location, description, risk_level, status) VALUES (?, ?, ?, ?, ?)",
                default_scenes
            )
            
        # Crew Contacts Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crew_contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL
        )
        """)
        
        cursor.execute("SELECT COUNT(*) as count FROM crew_contacts")
        if cursor.fetchone()["count"] == 0:
            default_contacts = [
                ("Peter Hein (Stunt Dir)", "Stunt Coordinator", "+919840123456", "Stunts"),
                ("Rathnavelu ISC (DoP)", "Director of Photography", "+919884056789", "Camera & Rigging"),
                ("Senthil (1st AD)", "First Assistant Director", "+919940011223", "Direction"),
                ("Kumar (Production Head)", "Line Producer / Logistics", "+919444099887", "Production Logistics")
            ]
            cursor.executemany(
                "INSERT INTO crew_contacts (name, role, phone, department) VALUES (?, ?, ?, ?)",
                default_contacts
            )
            
        conn.commit()
    finally:
        conn.close()

def save_mission_log(
    location_name: str,
    weather_mode: str,
    target_language: str,
    rain_mm: float,
    temperature: str,
    stunt_status: str,
    blueprint_text: str
) -> int:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
        INSERT INTO mission_logs (timestamp, location_name, weather_mode, target_language, rain_mm, temperature, stunt_status, blueprint_text)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (ts, location_name, weather_mode, target_language, rain_mm, temperature, stunt_status, blueprint_text))
        log_id = cursor.lastrowid
        conn.commit()
        return log_id
    finally:
        conn.close()

def get_mission_logs(limit: int = 50) -> List[ReconMissionLog]:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mission_logs ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        
        logs = []
        for r in rows:
            logs.append(ReconMissionLog(
                id=r["id"],
                timestamp=r["timestamp"],
                location_name=r["location_name"],
                weather_mode=r["weather_mode"],
                target_language=r["target_language"],
                rain_mm=r["rain_mm"],
                temperature=r["temperature"],
                stunt_status=r["stunt_status"],
                blueprint_text=r["blueprint_text"]
            ))
        return logs
    finally:
        conn.close()

def clear_mission_logs():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM mission_logs")
        conn.commit()
    finally:
        conn.close()

def get_film_scenes() -> List[FilmScene]:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM film_scenes ORDER BY id ASC")
        rows = cursor.fetchall()
        
        scenes = []
        for r in rows:
            scenes.append(FilmScene(
                id=r["id"],
                scene_number=r["scene_number"],
                location=r["location"],
                description=r["description"],
                risk_level=r["risk_level"],
                status=r["status"]
            ))
        return scenes
    finally:
        conn.close()

def add_film_scene(scene_number: str, location: str, description: str, risk_level: str) -> int:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO film_scenes (scene_number, location, description, risk_level, status)
        VALUES (?, ?, ?, ?, 'SCHEDULED')
        """, (scene_number, location, description, risk_level))
        scene_id = cursor.lastrowid
        conn.commit()
        return scene_id
    finally:
        conn.close()

def get_crew_contacts() -> List[CrewContact]:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM crew_contacts ORDER BY id ASC")
        rows = cursor.fetchall()
        
        contacts = []
        for r in rows:
            contacts.append(CrewContact(
                id=r["id"],
                name=r["name"],
                role=r["role"],
                phone=r["phone"],
                department=r["department"]
            ))
        return contacts
    finally:
        conn.close()

def add_crew_contact(name: str, role: str, phone: str, department: str) -> int:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO crew_contacts (name, role, phone, department)
        VALUES (?, ?, ?, ?)
        """, (name, role, phone, department))
        contact_id = cursor.lastrowid
        conn.commit()
        return contact_id
    finally:
        conn.close()
