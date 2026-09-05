import os
from fpdf import FPDF

class PresentationPDF(FPDF):
    def __init__(self):
        # A4 Landscape: 297mm width, 210mm height
        super().__init__(orientation='L', unit='mm', format='A4')
        self.set_auto_page_break(auto=False, margin=0)

    def draw_background(self):
        # Deep Obsidian background #0A0E17
        self.set_fill_color(10, 14, 23)
        self.rect(0, 0, 297, 210, 'F')

    def draw_header(self, category, title, subtitle=None):
        self.draw_background()

        # Top Bar
        self.set_xy(15, 10)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(245, 158, 11) # Amber
        self.cell(100, 6, "CRISISSHIFT OS  |  DIRECTOR TRACK", ln=0)

        self.set_xy(182, 10)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(56, 189, 248) # Cyan
        self.cell(100, 6, "GEMINI 3.8 ENTERPRISE PLATFORM", align="R", ln=1)

        # Thin header rule
        self.set_draw_color(38, 50, 75)
        self.set_line_width(0.3)
        self.line(15, 17, 282, 17)

        # Category Tag
        self.set_xy(15, 20)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(245, 158, 11)
        self.cell(0, 5, category.upper(), ln=1)

        # Main Title
        self.set_xy(15, 25)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(248, 250, 252) # White
        self.cell(0, 8, title, ln=1)

        # Subtitle
        if subtitle:
            self.set_xy(15, 34)
            self.set_font("Helvetica", "", 10)
            self.set_text_color(148, 163, 184) # Muted Silver
            self.cell(0, 5, subtitle, ln=1)

    def draw_footer(self, slide_num, total_slides=10):
        self.set_draw_color(38, 50, 75)
        self.set_line_width(0.3)
        self.line(15, 196, 282, 196)

        self.set_xy(15, 199)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(148, 163, 184)
        self.cell(150, 5, "CrisisShift OS  --  Autonomous Cinema Command", ln=0)

        self.set_xy(182, 199)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(245, 158, 11)
        self.cell(100, 5, f"{slide_num:02d} / {total_slides:02d}", align="R", ln=1)

    def draw_card(self, x, y, w, h, title, items, badge=None, accent_rgb=(56, 189, 248)):
        # Card Background
        self.set_fill_color(19, 27, 44)
        self.set_draw_color(38, 50, 75)
        self.set_line_width(0.4)
        self.rect(x, y, w, h, 'DF')

        curr_y = y + 4

        # Badge if present
        if badge:
            self.set_xy(x + 4, curr_y)
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(*accent_rgb)
            self.cell(w - 8, 4, f"[{badge}]", ln=1)
            curr_y += 5

        # Card Title
        self.set_xy(x + 4, curr_y)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(255, 255, 255)
        self.cell(w - 8, 6, title, ln=1)
        curr_y += 8

        # Items
        for item in items:
            self.set_xy(x + 4, curr_y)
            self.set_font("Helvetica", "", 9)
            
            # Check for bold prefix (before ':')
            if ":" in item:
                parts = item.split(":", 1)
                prefix = "- " + parts[0] + ":"
                body = parts[1]

                self.set_font("Helvetica", "B", 9)
                self.set_text_color(248, 250, 252)
                self.write(4.5, prefix)

                self.set_font("Helvetica", "", 8.5)
                self.set_text_color(156, 163, 175)
                self.write(4.5, body + "\n")
            else:
                self.set_text_color(156, 163, 175)
                self.cell(w - 8, 4.5, "- " + item, ln=1)

            curr_y = self.get_y() + 1.5

def build_pdf_presentation(output_path):
    pdf = PresentationPDF()

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_background()

    # Track Badge
    pdf.set_fill_color(26, 36, 56)
    pdf.set_draw_color(245, 158, 11)
    pdf.set_line_width(0.4)
    pdf.rect(15, 28, 115, 8, 'DF')
    pdf.set_xy(17, 30)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(245, 158, 11)
    pdf.cell(110, 4, "GOOGLE GEMINI 3.8 ENTERPRISE AGENT PLATFORM", ln=1)

    # Hero Title
    pdf.set_xy(15, 42)
    pdf.set_font("Helvetica", "B", 34)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 14, "CrisisShift OS", ln=1)

    # Subtitle
    pdf.set_xy(15, 58)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(56, 189, 248)
    pdf.cell(0, 8, "Autonomous Cinema Command & Set Orchestration", ln=1)

    # Paragraph Description
    pdf.set_xy(15, 72)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(148, 163, 184)
    pdf.multi_cell(265, 6.5, 
        "Transforming real-world film set chaos into deterministic autonomous cinema decisions powered by "
        "Gemini 3.8 Multi-Agent Swarm, Real-Time Satellite Atmospheric Radar, and Surface Asphalt Friction Physics.")

    # 4 Quick Metric Cards
    metrics = [
        ("TRACK", "Agentic Cinema Track", (245, 158, 11)),
        ("AI SWARM", "Gemini 3.8 Flash Engine", (56, 189, 248)),
        ("LOCALIZATION", "Bilingual Tanglish Dispatch", (16, 185, 129)),
        ("SAVINGS", "$50k - $500k Saved / Day", (239, 68, 68))
    ]
    for i, (m_tag, m_val, m_col) in enumerate(metrics):
        x = 15 + i * 68
        pdf.set_fill_color(19, 27, 44)
        pdf.set_draw_color(38, 50, 75)
        pdf.rect(x, 120, 62, 38, 'DF')

        pdf.set_xy(x + 4, 125)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*m_col)
        pdf.cell(54, 4, f"[{m_tag}]", ln=1)

        pdf.set_xy(x + 4, 134)
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(255, 255, 255)
        pdf.multi_cell(54, 5, m_val)

    pdf.draw_footer(1)

    # -------------------------------------------------------------
    # SLIDE 2: Executive Summary
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("Executive Overview", "CrisisShift OS at a Glance",
                    "Bridging orbital atmospheric science, terrain physics, and production logistics into an autonomous command cockpit.")

    pdf.draw_card(15, 44, 84, 144, "The Core Problem", [
        "Astronomical Losses: Outdoor film shoots lose $50,000 to $500,000 (Rs 40L - 4Cr) per cancelled day.",
        "Stunt & Crane Disasters: Stunt cars hydroplane on wet tarmac; 50-ft Technocranes tip over in softened mud.",
        "Static Failures: Paper call sheets and consumer weather apps fail to provide mathematical risk arbitration."
    ], badge="PAIN POINT", accent_rgb=(239, 68, 68))

    pdf.draw_card(104, 44, 84, 144, "The Innovation", [
        "Deterministic Swarm: Gemini 3.8 arbitrates telemetry across 4 specialized autonomous agents.",
        "Physical Grounding: Real-time radar plus dynamic friction (mu) and soil bearing capacity (sigma).",
        "Cultural Precision: First bilingual Tanglish dispatch engine for regional Indian & global crew communication."
    ], badge="INNOVATION", accent_rgb=(56, 189, 248))

    pdf.draw_card(193, 44, 89, 144, "The Business Impact", [
        "Sub-15s Execution: Instant Go/No-Go verdict replaces hours of panicked set arguments.",
        "Insurance Discounts: 15% to 25% lower completion bond premiums through verified physics audit trails.",
        "High Margin SaaS: 85%+ gross profit margin across Indie, Studio, and Slate enterprise tiers."
    ], badge="IMPACT & ROI", accent_rgb=(16, 185, 129))

    pdf.draw_footer(2)

    # -------------------------------------------------------------
    # SLIDE 3: Problem Statement
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("01. Problem Statement", "Multi-Million Dollar Losses & Safety Blindspots",
                    "Cinema outdoor shoots face uncontrollable micro-climates, disastrous budget blowouts, and life-threatening stunts.")

    pdf.draw_card(15, 44, 84, 144, "Financial Bleed", [
        "Daily Sunk Costs: Film productions bleed $50k to $500k every day outdoor shooting is rained out.",
        "Idle Overhead: Star cast date locks, 200+ union crew wages, and Technocrane daily leases run regardless.",
        "Budget Ballooning: Just 3 unpredicted weather cancellations can swell overall project budget by 20% to 30%."
    ], badge="FINANCIAL RISK", accent_rgb=(239, 68, 68))

    pdf.draw_card(104, 44, 84, 144, "Stunt & Rig Hazards", [
        "Hydroplaning Wrecks: High-speed chase stunts on damp asphalt suffer fatal skids when friction drops below 0.35.",
        "Technocrane Overturns: 50-foot camera cranes exert extreme ground pressure, risking collapse into rain-soaked mud.",
        "Zero Sensory Data: Directors and 1st ADs cannot visually estimate road friction or subsurface soil density."
    ], badge="LIFE SAFETY", accent_rgb=(245, 158, 11))

    pdf.draw_card(193, 44, 89, 144, "Broken Legacy Tools", [
        "Static Call Sheets: Paper call sheets and Excel matrices are outdated the moment micro-weather shifts.",
        "Consumer Weather Apps: Generic phone apps lack precision atmospheric radar or camera rig engineering context.",
        "Language Bottlenecks: Regional film crews (Tamil, Hindi, Telugu) struggle with delayed formal English directives."
    ], badge="OPERATIONS", accent_rgb=(56, 189, 248))

    pdf.draw_footer(3)

    # -------------------------------------------------------------
    # SLIDE 4: The Solution & What We Built
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("02. The Solution", "The 4-Agent Autonomous Directorial Architecture",
                    "An end-to-end intelligent cockpit replacing guesswork with autonomous multi-agent orchestration.")

    pdf.draw_card(15, 44, 62, 144, "Agent 1: Scout", [
        "Radar Telemetry: Live Open-Meteo atmospheric radar.",
        "Rain & Wind: Instant wind vector and rain volume extraction.",
        "ArcGIS Recon: High-res satellite optical imagery.",
        "3D Radar: Live location beacon."
    ], badge="SATELLITE", accent_rgb=(56, 189, 248))

    pdf.draw_card(81, 44, 62, 144, "Agent 2: Physics", [
        "Asphalt Grip (mu): Computes road friction (0.32 wet vs 0.85 dry).",
        "Soil Bearing (sigma): Checks crane outrigger load pressure against soil limits.",
        "Braking Curves: Precision stunt stopping distance."
    ], badge="PHYSICS", accent_rgb=(245, 158, 11))

    pdf.draw_card(147, 44, 64, 144, "Agent 3: Swarm", [
        "Deterministic Decision: Strict Go/No-Go decision.",
        "RED HALT Action: If Rain > 1.0mm or mu < 0.40, triggers emergency halt.",
        "Indoor Routing: Instant fallback to covered soundstages.",
        "Zero Guesswork: Telemetry-grounded."
    ], badge="ORCHESTRATOR", accent_rgb=(16, 185, 129))

    pdf.draw_card(215, 44, 67, 144, "Agent 4: Dispatch", [
        "Tanglish First: Native Tamil+English WhatsApp alerts.",
        "Multilingual: Hindi, Telugu and English dispatches.",
        "1-Click PDF: FPDF2 Unicode audit dispatches.",
        "SQLite Trail: Permanent mission database logs."
    ], badge="DISPATCH", accent_rgb=(248, 250, 252))

    pdf.draw_footer(4)

    # -------------------------------------------------------------
    # SLIDE 5: How It Works
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("03. How It Works", "5-Stage Deterministic Production Pipeline",
                    "From location GPS coordinates to emergency crew WhatsApp broadcast in under 15 seconds.")

    steps = [
        ("01", "Location & Scene Ingestion", 
         "Director or 1st AD inputs shoot GPS coordinates, scheduled call time, and scene parameters (Highway Chase, Technocrane).", (56, 189, 248)),
        ("02", "Orbital Satellite Radar Recon", 
         "Agent 1 connects to Open-Meteo and OpenStreetMap atmospheric radar, extracting live precipitation volume, wind gusts, and clouds.", (245, 158, 11)),
        ("03", "Terrain Physics Calculation", 
         "Agent 2 calculates surface asphalt friction (mu = 0.32 - 0.85) and tests Technocrane outrigger ground pressure against soil limits.", (16, 185, 129)),
        ("04", "Gemini 3.8 Swarm Decision Arbitration", 
         "Agent 3 synthesizes telemetry. If Rain > 1.0mm or mu < 0.40, it triggers an immediate RED HALT and routes crew to covered Soundstage B.", (239, 68, 68)),
        ("05", "Bilingual Tanglish Crew Dispatch & Audit Log", 
         "Agent 4 formats WhatsApp alerts in native Tanglish/English for instant broadcast, auto-logging the compliance record to SQLite and PDF.", (168, 85, 247))
    ]

    for i, (num, stitle, sdesc, scol) in enumerate(steps):
        y = 44 + i * 28
        pdf.set_fill_color(19, 27, 44)
        pdf.set_draw_color(38, 50, 75)
        pdf.rect(15, y, 267, 24, 'DF')

        # Badge
        pdf.set_fill_color(26, 36, 56)
        pdf.set_draw_color(*scol)
        pdf.rect(20, y + 4, 16, 16, 'DF')
        pdf.set_xy(20, y + 8)
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(*scol)
        pdf.cell(16, 6, num, align="C", ln=0)

        # Text
        pdf.set_xy(42, y + 3.5)
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(230, 5, stitle, ln=1)

        pdf.set_xy(42, y + 9.5)
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(148, 163, 184)
        pdf.multi_cell(235, 4.5, sdesc)

    pdf.draw_footer(5)

    # -------------------------------------------------------------
    # SLIDE 6: Core Benefits
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("04. Core Benefits", "Why Film Productions Choose CrisisShift OS",
                    "Unrivaled operational speed, life safety assurance, and flawless set coordination across departments.")

    pdf.draw_card(15, 44, 84, 144, "Sub-15s Latency", [
        "Lightning Fast: Orbital radar, friction math, and swarm decision execute in under 15 seconds.",
        "Replaces Endless Debates: Eliminates frantic phone calls between director, producer, and camera crew in the rain.",
        "Real-Time Adaptability: Automatically monitors micro-climate shifts and updates production dispatches."
    ], badge="SPEED", accent_rgb=(56, 189, 248))

    pdf.draw_card(104, 44, 84, 144, "Zero Stunt Casualties", [
        "Mathematical Grounding: Eliminates guesswork by calculating true braking distance and grip coefficients.",
        "Rig & Gear Protection: Prevents $500,000 Technocranes and luxury cinema camera packages from mud sinking or tip-overs.",
        "Insurance Compliance: Generates timestamped PDF dispatches for completion bond underwriting and liability audits."
    ], badge="LIFE SAFETY", accent_rgb=(16, 185, 129))

    pdf.draw_card(193, 44, 89, 144, "Native Tanglish Edge", [
        "Cultural Precision: Local crew members in Chennai, Hyderabad, and Mumbai understand Tanglish immediately.",
        "Actionable Set Language: Direct colloquial directives (e.g. 'Vandi slow pannunga, technocrane plates podunga').",
        "WhatsApp Native: Formatted for 1-click copy-paste into departmental chat groups without delay."
    ], badge="LOCALIZATION", accent_rgb=(245, 158, 11))

    pdf.draw_footer(6)

    # -------------------------------------------------------------
    # SLIDE 7: Business Value, ROI & Profit Model
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("05. Business Value & Profit", "Financial ROI & High-Margin Revenue Profit",
                    "Saving massive production budgets while unlocking an enterprise SaaS commercial revenue stream.")

    pdf.draw_card(15, 44, 128, 144, "Direct Financial ROI for Productions", [
        "Rainout Prevention: Saves $50,000 to $500,000 (Rs 40 Lakhs - Rs 4 Crores) per averted cancellation day by shifting crew indoors early.",
        "15% to 25% Insurance Discounts: Production completion bond insurers offer lower policy premiums for productions utilizing verified physics risk monitoring.",
        "Gear Wreckage Avoidance: Prevents $200k+ cinema camera bodies and specialized stunt vehicles from crash damage.",
        "Crew Overtime Optimization: Eliminates paid idle standby hours for 200+ crew by orchestrating immediate soundstage fallback."
    ], badge="PRODUCTION ROI", accent_rgb=(16, 185, 129))

    pdf.draw_card(150, 44, 132, 144, "Commercial Monetization & Profit Model", [
        "Indie Tier (Rs 25,000 / month): Targeted at ad commercials and indie filmmakers for basic atmospheric radar and physics.",
        "Blockbuster Tier (Rs 1,50,000 / shoot): Full 4-agent swarm, Tanglish WhatsApp dispatcher, and PDF audit engine for 90-day schedules.",
        "Enterprise Studio Slate ($25,000 / year): Unlimited access for major production banners (Lyca, Sun Pictures, Dharma, Netflix India).",
        "85%+ Gross Profit Margin: High-efficiency Gemini 3.8 Flash API inference provides near-zero marginal cost per recon run."
    ], badge="COMMERCIAL REVENUE", accent_rgb=(245, 158, 11))

    pdf.draw_footer(7)

    # -------------------------------------------------------------
    # SLIDE 8: Market Comparison Matrix
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("06. Market Comparison", "Why CrisisShift OS Dominates Legacy Methods",
                    "Comparing traditional production tools against CrisisShift OS Autonomous Cinema Command.")

    # Table Header
    headers = [("Feature / Capability", 80), ("Static Call Sheets", 60), ("Weather Apps", 60), ("CrisisShift OS", 67)]
    x_start = 15
    y_start = 50

    pdf.set_fill_color(26, 36, 56)
    pdf.set_draw_color(38, 50, 75)
    pdf.set_line_width(0.3)
    curr_x = x_start
    for h_name, h_w in headers:
        pdf.set_xy(curr_x, y_start)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(245, 158, 11) if h_name == "CrisisShift OS" else pdf.set_text_color(255, 255, 255)
        pdf.cell(h_w, 10, h_name, border=1, fill=True, align="C" if curr_x > x_start else "L")
        curr_x += h_w

    # Table Rows
    rows = [
        ("Real-Time Radar & Satellite", "None / Paper Only", "City-Level Forecast", "Live Open-Meteo + ArcGIS"),
        ("Surface Friction (mu) Physics", "None", "None", "Exact Mathematical Model"),
        ("Autonomous Decision Making", "Manual Set Debates", "User Must Interpret", "Deterministic Gemini 3.8 Swarm"),
        ("Set Localization (Tanglish)", "English / Manual", "English Only", "Native Tanglish / Regional Broadcast"),
        ("1-Click PDF Audit Records", "Manual Paperwork", "None", "Instant FPDF2 Unicode PDF Export")
    ]

    for r_idx, row in enumerate(rows):
        y = y_start + 10 + r_idx * 22
        curr_x = x_start
        for c_idx, val in enumerate(row):
            w = headers[c_idx][1]
            pdf.set_xy(curr_x, y)
            pdf.set_fill_color(19, 27, 44) if c_idx < 3 else pdf.set_fill_color(22, 34, 52)
            pdf.set_font("Helvetica", "B" if (c_idx == 0 or c_idx == 3) else "", 9.5)
            pdf.set_text_color(56, 189, 248) if c_idx == 3 else (pdf.set_text_color(255, 255, 255) if c_idx == 0 else pdf.set_text_color(148, 163, 184))
            pdf.cell(w, 22, val, border=1, fill=True, align="C" if c_idx > 0 else "L")
            curr_x += w

    pdf.draw_footer(8)

    # -------------------------------------------------------------
    # SLIDE 9: Vision & Roadmap
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_header("07. Roadmap & Vision", "Scaling to the Global Cinema Operating System",
                    "Evolving from location safety to an enterprise-grade Operating System for global film productions.")

    pdf.draw_card(15, 44, 84, 144, "Phase 1: Hackathon MVP", [
        "Gemini 3.8 Swarm: 4-agent autonomous directorial logic.",
        "Radar & Physics Engine: Live Open-Meteo, asphalt friction, and crane load math.",
        "Bilingual Localization: Tanglish WhatsApp dispatcher.",
        "Audit Compliance: SQLite database and FPDF2 PDF exports."
    ], badge="PHASE 1: CURRENT", accent_rgb=(16, 185, 129))

    pdf.draw_card(104, 44, 84, 144, "Phase 2: Studio MCP", [
        "MCP Server Adapter: Model Context Protocol sync with Movie Magic Scheduling.",
        "Live Drone Feeds: Direct aerial optical reconnaissance.",
        "Twilio WhatsApp API: Automated simultaneous dispatch to 200+ crew phones.",
        "Multi-Camera Tracking: Dynamic lighting and shadow calculation."
    ], badge="PHASE 2: NEAR-TERM", accent_rgb=(56, 189, 248))

    pdf.draw_card(193, 44, 89, 144, "Phase 3: Global Cinema OS", [
        "Multi-Unit Orchestration: Autonomous sync between 1st Unit and 2nd Unit teams.",
        "AI Stunt Simulations: Pre-visualized trajectory and friction collision modeling.",
        "Automated Insurance Filing: Instant claim settlement dispatch for weather delays.",
        "Studio Slate Cockpit: Global dashboard for multi-film slates."
    ], badge="PHASE 3: LONG-TERM", accent_rgb=(245, 158, 11))

    pdf.draw_footer(9)

    # -------------------------------------------------------------
    # SLIDE 10: Conclusion & Call to Action
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.draw_background()

    pdf.set_fill_color(26, 36, 56)
    pdf.set_draw_color(245, 158, 11)
    pdf.set_line_width(0.4)
    pdf.rect(15, 28, 70, 8, 'DF')
    pdf.set_xy(17, 30)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(245, 158, 11)
    pdf.cell(66, 4, "THE BLOCKBUSTER HACKATHON", ln=1)

    pdf.set_xy(15, 42)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(255, 255, 255)
    pdf.multi_cell(265, 11, "From Chaos on Set to Autonomous Mastery.")

    pdf.set_xy(15, 68)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(56, 189, 248)
    pdf.multi_cell(265, 7, "CrisisShift OS protects crew lives, saves multi-crore film budgets, and brings deterministic AI command to global cinema.")

    summary_pillars = [
        ("Sub-15s Speed", "Instant satellite radar telemetry and physics-backed Go/No-Go verdict.", (56, 189, 248)),
        ("Rs 40L - Rs 4Cr Saved", "Proven production cost avoidance per prevented outdoor rainout cancellation.", (16, 185, 129)),
        ("Gemini 3.8 Swarm", "The ultimate autonomous directorial and safety engine for modern cinema.", (245, 158, 11))
    ]
    for i, (p_title, p_desc, p_col) in enumerate(summary_pillars):
        x = 15 + i * 92
        pdf.set_fill_color(19, 27, 44)
        pdf.set_draw_color(*p_col)
        pdf.set_line_width(0.5)
        pdf.rect(x, 105, 84, 60, 'DF')

        pdf.set_xy(x + 6, 112)
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(*p_col)
        pdf.cell(72, 6, p_title, ln=1)

        pdf.set_xy(x + 6, 124)
        pdf.set_font("Helvetica", "", 10.5)
        pdf.set_text_color(248, 250, 252)
        pdf.multi_cell(72, 6, p_desc)

    pdf.draw_footer(10)

    # Save PDF
    pdf.output(output_path)
    print(f"Presentation PDF successfully created at: {output_path}")

if __name__ == "__main__":
    build_pdf_presentation("CrisisShift_OS_Presentation.pdf")
