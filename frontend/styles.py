import streamlit as st
import streamlit.components.v1 as components

def disable_browser_autofill():
    """
    Suppresses browser 'Saved Info' / autocomplete dropdown popups on text inputs.
    """
    components.html("""
    <script>
        function suppressAutofill() {
            try {
                const doc = window.parent.document;
                const elements = doc.querySelectorAll('input, textarea');
                elements.forEach(el => {
                    el.setAttribute('autocomplete', 'off');
                    el.setAttribute('autocorrect', 'off');
                    el.setAttribute('autocapitalize', 'off');
                    el.setAttribute('spellcheck', 'false');
                    el.setAttribute('data-lpignore', 'true');
                    el.setAttribute('data-form-type', 'other');
                });
            } catch(e) {}
        }
        suppressAutofill();
        setInterval(suppressAutofill, 600);
    </script>
    """, height=0, width=0)

def inject_hud_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
        
        :root {
            --amber-primary: #FF9F00;
            --amber-glow: #FF7700;
            --gold-accent: #FFD000;
            --neon-green: #00FF66;
            --neon-red: #FF3366;
            --dark-bg: #070709;
            --dark-card: rgba(18, 18, 24, 0.94);
            --border-amber: rgba(255, 159, 0, 0.35);
            --border-glass: rgba(255, 255, 255, 0.08);
        }

        * { font-family: 'Plus Jakarta Sans', sans-serif; }
        
        .stApp {
            background: radial-gradient(circle at 75% 15%, rgba(255, 120, 0, 0.09) 0%, rgba(15, 12, 10, 0.98) 50%, #060608 100%);
            color: #F1F5F9;
        }

        /* Top Hero Header Card */
        .hud-hero {
            background: linear-gradient(135deg, rgba(255, 140, 0, 0.14) 0%, rgba(20, 16, 14, 0.95) 60%, rgba(8, 8, 11, 0.98) 100%);
            border: 1px solid var(--border-amber);
            border-radius: 20px;
            padding: 26px 32px;
            backdrop-filter: blur(20px);
            box-shadow: 0 16px 50px rgba(255, 120, 0, 0.1);
            margin-bottom: 22px;
            position: relative;
            overflow: hidden;
        }

        .hud-hero::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
            background: linear-gradient(90deg, #FF9F00, #FF5500, #FFD000, #FF9F00);
            background-size: 200% 100%;
            animation: amberMove 4s linear infinite;
        }

        @keyframes amberMove {
            0% { background-position: 0% 0%; }
            100% { background-position: 200% 0%; }
        }

        .hud-title {
            font-family: 'Space Grotesk', 'Orbitron', sans-serif;
            font-weight: 800;
            font-size: 2.4rem;
            letter-spacing: -0.5px;
            color: #FFFFFF;
            margin: 0;
            text-transform: uppercase;
        }

        .hud-title span {
            color: var(--amber-primary);
            background: linear-gradient(180deg, #FFD000 0%, #FF8800 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hud-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 159, 0, 0.14);
            color: var(--amber-primary);
            border: 1px solid rgba(255, 159, 0, 0.4);
            border-radius: 100px;
            padding: 5px 16px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            background-color: var(--amber-primary);
            border-radius: 50%;
            box-shadow: 0 0 14px var(--amber-primary);
        }

        /* Location & Target Input Card Highlight */
        .target-input-box {
            background: linear-gradient(135deg, rgba(255, 159, 0, 0.08) 0%, rgba(18, 18, 24, 0.96) 100%);
            border: 2px solid rgba(255, 159, 0, 0.5);
            border-radius: 20px;
            padding: 22px 26px;
            margin-bottom: 24px;
            box-shadow: 0 12px 35px rgba(255, 159, 0, 0.12);
        }

        /* Telemetry Stat Cards */
        .telemetry-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
            margin-bottom: 22px;
        }

        .telemetry-card {
            background: var(--dark-card);
            border: 1px solid var(--border-amber);
            border-radius: 16px;
            padding: 16px 14px;
            text-align: center;
            backdrop-filter: blur(16px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
        }

        .telemetry-card:hover {
            border-color: rgba(255, 159, 0, 0.6);
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(255, 140, 0, 0.15);
        }

        .tel-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.68rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 1.4px;
        }

        .tel-val {
            font-family: 'Space Grotesk', 'Orbitron', sans-serif;
            font-size: 1.4rem;
            font-weight: 800;
            margin-top: 4px;
            color: var(--amber-primary);
        }

        /* Ground Physics Cards */
        .ground-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            margin: 18px 0;
        }

        .ground-card {
            background: rgba(14, 14, 18, 0.94);
            border: 1px solid var(--border-amber);
            border-radius: 16px;
            padding: 16px;
            font-family: 'JetBrains Mono', monospace;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
        }

        .ground-card-header {
            font-size: 0.72rem;
            color: var(--amber-primary);
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .ground-card-val {
            font-size: 1.1rem;
            font-weight: 800;
            color: #FFFFFF;
        }

        .ground-card-desc {
            font-size: 0.76rem;
            color: #94A3B8;
            margin-top: 6px;
        }

        /* Streamlit Input Fields */
        .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div {
            background-color: rgba(12, 12, 16, 0.98) !important;
            border: 1px solid rgba(255, 159, 0, 0.4) !important;
            border-radius: 14px !important;
            color: #FFFFFF !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 1.02rem !important;
            font-weight: 600 !important;
            padding: 12px 16px !important;
        }

        .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
            border-color: var(--amber-primary) !important;
            box-shadow: 0 0 20px rgba(255, 159, 0, 0.35) !important;
        }

        /* Main CTA Button - Electric Amber Gradient */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #FF9F00 0%, #D85000 100%) !important;
            color: #050507 !important;
            font-family: 'Space Grotesk', 'Orbitron', sans-serif !important;
            font-weight: 800 !important;
            font-size: 1.1rem !important;
            letter-spacing: 1.5px !important;
            border: 1px solid rgba(255, 200, 0, 0.6) !important;
            border-radius: 16px !important;
            padding: 18px 32px !important;
            text-transform: uppercase !important;
            box-shadow: 0 0 40px rgba(255, 159, 0, 0.45) !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }

        div.stButton > button:first-child:hover {
            background: linear-gradient(135deg, #FFB300 0%, #F56000 100%) !important;
            box-shadow: 0 0 50px rgba(255, 159, 0, 0.7) !important;
            transform: translateY(-2px) !important;
        }

        /* High-Impact AI Dispatch Result Card */
        .dispatch-card {
            background: linear-gradient(135deg, rgba(20, 20, 28, 0.98) 0%, rgba(10, 10, 14, 0.99) 100%);
            border: 2px solid var(--amber-primary);
            border-radius: 22px;
            padding: 28px 34px;
            margin: 24px 0;
            box-shadow: 0 16px 50px rgba(255, 159, 0, 0.2);
            position: relative;
        }

        .dispatch-card.red-alert {
            border-color: var(--neon-red);
            box-shadow: 0 16px 50px rgba(255, 51, 102, 0.25);
        }

        .dispatch-card.green-light {
            border-color: var(--neon-green);
            box-shadow: 0 16px 50px rgba(0, 255, 102, 0.25);
        }
        
        .dispatch-header {
            font-family: 'Space Grotesk', 'Orbitron', sans-serif;
            font-size: 1.55rem;
            font-weight: 900;
            color: var(--amber-primary);
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255, 159, 0, 0.3);
            padding-bottom: 10px;
        }

        /* Direct Streamlit Markdown Big Text Rules (User requested large text) */
        div[data-testid="stMarkdownContainer"] ul,
        div[data-testid="stMarkdownContainer"] ol {
            font-size: 1.45rem !important;
            line-height: 2.1 !important;
            margin-top: 14px !important;
        }

        div[data-testid="stMarkdownContainer"] li {
            font-size: 1.45rem !important;
            line-height: 2.1 !important;
            color: #F8FAFC !important;
            margin-bottom: 16px !important;
            font-weight: 500 !important;
        }

        div[data-testid="stMarkdownContainer"] li strong,
        div[data-testid="stMarkdownContainer"] p strong,
        div[data-testid="stMarkdownContainer"] li b,
        div[data-testid="stMarkdownContainer"] p b {
            font-size: 1.55rem !important;
            color: #FFD000 !important;
            font-weight: 900 !important;
        }

        div[data-testid="stMarkdownContainer"] p {
            font-size: 1.35rem !important;
            line-height: 2.0 !important;
            color: #F1F5F9 !important;
        }

        div[data-testid="stMarkdownContainer"] h1 {
            font-size: 2.2rem !important;
            color: var(--amber-primary) !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 900 !important;
        }

        div[data-testid="stMarkdownContainer"] h2 {
            font-size: 1.9rem !important;
            color: var(--amber-primary) !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 900 !important;
        }

        div[data-testid="stMarkdownContainer"] h3 {
            font-size: 1.7rem !important;
            color: var(--amber-primary) !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 800 !important;
        }

        div[data-testid="stMarkdownContainer"] h4 {
            font-size: 1.55rem !important;
            color: var(--amber-primary) !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 800 !important;
        }

        /* History & Scene Cards */
        .history-card {
            background: rgba(18, 18, 24, 0.9);
            border: 1px solid var(--border-amber);
            border-radius: 16px;
            padding: 18px;
            margin-bottom: 14px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.4);
        }

        /* Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: rgba(12, 12, 16, 0.8);
            padding: 6px;
            border-radius: 14px;
            border: 1px solid var(--border-glass);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 10px;
            color: #94A3B8;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            padding: 8px 20px;
        }

        .stTabs [aria-selected="true"] {
            background: rgba(255, 159, 0, 0.18) !important;
            color: var(--amber-primary) !important;
            border: 1px solid var(--border-amber) !important;
        }
    </style>
    """, unsafe_allow_html=True)
