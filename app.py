import os
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# 1. PAGE SETUP (Mobile First & Favicon)
# ---------------------------------------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))
logo_candidates = ["logo.png", "logo.jpg", "logo.jpeg", "logo.webp"]
found_logo = None
for fname in logo_candidates:
  full_path = os.path.join(APP_DIR, fname)
  if os.path.exists(full_path):
    found_logo = full_path
    break

st.set_page_config(
    page_title="5th UKM Renal Symposium 2026",
    page_icon=found_logo if found_logo else "🩺",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# 2. APP STYLING (Modern Slate Theme & Native Card UI)
# ---------------------------------------------------------
st.markdown(
    """
<style>
    /* 1. Global Background: Native Mobile Slate */
    .stApp {
        background-color: #f1f5f9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* 2. Hide Streamlit Chrome & Headers */
    #MainMenu, footer, header {
        visibility: hidden;
        height: 0px;
    }
    div[data-testid="stDecoration"] {
        display: none;
    }

    /* 3. Mobile Viewport Container */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 5rem;
        max-width: 540px;
        margin: 0 auto;
    }

    /* 4. Native App Hero Card */
    .hero-banner {
        background: linear-gradient(145deg, #0f2744 0%, #1e3a8a 50%, #0369a1 100%);
        border-radius: 18px;
        padding: 22px 20px;
        color: white;
        margin-top: 10px;
        margin-bottom: 18px;
        box-shadow: 0 8px 24px -4px rgba(15, 39, 68, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(8px);
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 8px;
        color: #e0f2fe;
    }
    .hero-title {
        font-size: 1.38rem;
        font-weight: 800;
        margin: 0;
        line-height: 1.25;
        letter-spacing: -0.02em;
        color: #ffffff;
    }
    .hero-subtitle {
        font-size: 0.82rem;
        color: #bae6fd;
        margin-top: 6px;
        line-height: 1.4;
    }

    /* 5. Native Segmented Tab Switcher */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #e2e8f0;
        padding: 5px;
        border-radius: 14px;
        border: none;
    }
    .stTabs [data-baseweb="tab"] {
        height: 38px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 10px;
        color: #475569;
        font-size: 0.84rem;
        font-weight: 600;
        border: none;
        padding: 0 14px;
        flex: 1;
        justify-content: center;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #0f2744 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08) !important;
    }

    /* 6. Session Cards */
    .session-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        border-left: 5px solid #0284c7;
    }
    .card-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }
    .session-time {
        font-weight: 700;
        color: #0284c7;
        font-size: 0.86rem;
        letter-spacing: -0.01em;
    }
    .session-room {
        font-size: 0.74rem;
        color: #475569;
        background: #f1f5f9;
        font-weight: 600;
        padding: 3px 9px;
        border-radius: 20px;
    }
    .session-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #0f172a;
        margin: 4px 0 6px 0;
        line-height: 1.35;
    }
    .session-speaker {
        font-size: 0.86rem;
        color: #475569;
        margin-bottom: 10px;
        font-weight: 500;
    }

    /* 7. Category Badges */
    .badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 700;
    }
    .badge-plenary { background: #f3e8ff; color: #6b21a8; }
    .badge-ckm { background: #e0f2fe; color: #0369a1; }
    .badge-break { background: #fef3c7; color: #92400e; }
    .badge-cardio { background: #fee2e2; color: #991b1b; }
    .badge-pharma { background: #ccfbf1; color: #115e59; }
    .badge-diet { background: #dcfce7; color: #166534; }
    .badge-default { background: #f1f5f9; color: #475569; }

    /* 8. Synopsis Expander */
    .streamlit-expanderHeader {
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        color: #64748b !important;
        background-color: transparent !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. PWA META TAGS (Enables Fullscreen Standalone App Mode)
# ---------------------------------------------------------
components.html(
    """
<script>
    let metaApple = document.createElement('meta');
    metaApple.name = 'apple-mobile-web-app-capable';
    metaApple.content = 'yes';
    document.getElementsByTagName('head')[0].appendChild(metaApple);

    let metaStatus = document.createElement('meta');
    metaStatus.name = 'apple-mobile-web-app-status-bar-style';
    metaStatus.content = 'black-translucent';
    document.getElementsByTagName('head')[0].appendChild(metaStatus);

    let metaChrome = document.createElement('meta');
    metaChrome.name = 'mobile-web-app-capable';
    metaChrome.content = 'yes';
    document.getElementsByTagName('head')[0].appendChild(metaChrome);
</script>
""",
    height=0,
)


def render_badge(track_name):
  t = track_name.lower()
  if "plenary" in t:
    return f'<span class="badge badge-plenary">🌟 {track_name}</span>'
  elif "cardio" in t or "heart" in t:
    return f'<span class="badge badge-cardio">❤️ {track_name}</span>'
  elif "metabolic" in t or "nephrology" in t or "ckm" in t:
    return f'<span class="badge badge-ckm">🩺 {track_name}</span>'
  elif "pharma" in t:
    return f'<span class="badge badge-pharma">💊 {track_name}</span>'
  elif "nutrition" in t or "diet" in t:
    return f'<span class="badge badge-diet">🥗 {track_name}</span>'
  elif "break" in t:
    return f'<span class="badge badge-break">☕ {track_name}</span>'
  else:
    return f'<span class="badge badge-default">📌 {track_name}</span>'


# ---------------------------------------------------------
# 4. SCIENTIFIC PROGRAMME DATA
# ---------------------------------------------------------
SESSIONS = [
    {
        "Time": "07:30 - 08:15",
        "Track": "General",
        "Title": "Delegate Registration & Welcome Breakfast",
        "Speaker": "Organizing Secretariat",
        "Room": "Auditorium Foyer",
        "Description": "",
    },
    {
        "Time": "08:15 - 08:30",
        "Track": "General",
        "Title": "Arrival of VIPs & Guests of Honour",
        "Speaker": "Faculty Administration",
        "Room": "Main Auditorium",
        "Description": "",
    },
    {
        "Time": "08:30 - 09:15",
        "Track": "Plenary",
        "Title": "Official Opening Ceremony: 5th UKM Renal Symposium",
        "Speaker": "Prof. Dato' Dr. Marina Mat Baki (Dean, Faculty of Medicine)",
        "Room": "Main Auditorium",
        "Description": "",
    },
    {
        "Time": "09:15 - 09:45",
        "Track": "Cardio-Kidney-Metabolic",
        "Title": "The Rise of CKM: Why We Must Break Clinical Silos",
        "Speaker": (
            "Prof. Dr. Abdul Halim Abdul Gafor (Senior Consultant Nephrologist)"
        ),
        "Room": "Main Auditorium",
        "Description": (
            "Rethinking multisystem care to bridge cardiology, nephrology, and"
            " endocrinology, focusing on unified screening, early risk"
            " interception, and coordinated organ protection."
        ),
    },
    {
        "Time": "09:45 - 10:15",
        "Track": "Metabolic & Diabetes",
        "Title": "The 'M' in CKM: Redefining Metabolic Control",
        "Speaker": "Prof. Dr. Christopher Lim (Senior Consultant Nephrologist)",
        "Room": "Main Auditorium",
        "Description": (
            "Modernizing glycemic and metabolic targets in chronic kidney"
            " disease beyond traditional HbA1c metrics, emphasizing insulin"
            " resistance, body composition, and cardiorenal outcomes."
        ),
    },
    {
        "Time": "10:15 - 10:30",
        "Track": "Break",
        "Title": "Morning Tea & Exhibition Viewing",
        "Speaker": "-",
        "Room": "The Gallery",
        "Description": "",
    },
    {
        "Time": "10:30 - 11:00",
        "Track": "Cardiology & Renal",
        "Title": (
            "The 'C' in CKRM: Pathophysiological Cardiorenal Crosstalk &"
            " Metabolic Involvement"
        ),
        "Speaker": (
            "Assoc. Prof. Dr. Hamat Hamdi Che Hassan (Consultant Cardiologist)"
        ),
        "Room": "Main Auditorium",
        "Description": (
            "Detailed dissection of reciprocal hemodynamic, neurohormonal, and"
            " inflammatory signaling between failing kidneys and myocardium in"
            " the presence of metabolic dysfunction."
        ),
    },
    {
        "Time": "11:00 - 11:30",
        "Track": "Cardiology & Renal",
        "Title": "Practical Challenges in Treating Heart Failure in Advanced CKD",
        "Speaker": "Dr. Hafidz Abd Hadi (Consultant Cardiologist)",
        "Room": "Main Auditorium",
        "Description": (
            "Overcoming clinical hurdles in guideline-directed medical therapy"
            " (GDMT) titration, loop diuretic resistance, intravascular volume"
            " assessment, and cardiorenal syndrome in stage 4-5 CKD."
        ),
    },
    {
        "Time": "11:30 - 12:00",
        "Track": "Pharmacotherapy",
        "Title": "Polypharmacy in the CKM Spectrum",
        "Speaker": "Ms. Pau Kiew Bing (Clinical Pharmacist)",
        "Room": "Main Auditorium",
        "Description": (
            "Deprescribing strategies, avoiding adverse drug-drug"
            " interactions, dose adjustments across fluctuating eGFR, and"
            " ensuring adherence in multimorbid cardiorenal patients."
        ),
    },
    {
        "Time": "12:00 - 12:30",
        "Track": "Clinical Nephrology",
        "Title": "Managing AKI Alerts and Hyperkalemia in CKM",
        "Speaker": (
            "Assoc. Prof. Dr. Ruslinda Mustafar (Senior Consultant Nephrologist)"
        ),
        "Room": "Main Auditorium",
        "Description": (
            "Distinguishing transient hemodynamic eGFR dips from true acute"
            " tubular injury, along with practical protocols for modern"
            " potassium binders to maintain RAASi and mineralocorticoid receptor"
            " antagonist therapy."
        ),
    },
    {
        "Time": "12:30 - 13:15",
        "Track": "Industry Symposium",
        "Title": (
            "Lunch Symposium (DKSH): Navigating the Cardio-Kidney-Metabolic"
            " Spectrum with Novel nsMRAs"
        ),
        "Speaker": "Prof. Dr. Abdul Halim Abdul Gafor",
        "Room": "Main Auditorium",
        "Description": (
            "Clinical trial evidence and real-world implementation of"
            " non-steroidal mineralocorticoid receptor antagonists in slowing"
            " kidney disease progression and mitigating cardiovascular events."
        ),
    },
    {
        "Time": "13:15 - 14:00",
        "Track": "Break",
        "Title": "Lunch & Midday Prayers",
        "Speaker": "-",
        "Room": "The Gallery",
        "Description": "",
    },
    {
        "Time": "14:00 - 14:30",
        "Track": "Nutrition & Dietetics",
        "Title": (
            "Optimizing Nutrition and Prevention of Sarcopenia: Challenges in"
            " CKM"
        ),
        "Speaker": (
            "Prof. Dr. Barakatun Nisak Mohd Yusof (President, Malaysian"
            " Dietitians' Association)"
        ),
        "Room": "Main Auditorium",
        "Description": (
            "Balancing protein restriction for kidney preservation against"
            " protein-energy wasting, sarcopenia prevention, and personalized"
            " dietary prescriptions in combined diabetic kidney disease and"
            " heart failure."
        ),
    },
    {
        "Time": "14:30 - 15:00",
        "Track": "Clinical Nephrology",
        "Title": (
            "Conservative Kidney Management (CKM) in Advanced Cardiorenal"
            " Failure"
        ),
        "Speaker": (
            "Assoc. Prof. Dr. Rozita Mohd (Senior Consultant Nephrologist)"
        ),
        "Room": "Main Auditorium",
        "Description": (
            "Comprehensive non-dialytic supportive care pathways, symptom"
            " management (fatigue, dyspnea, edema), advance care planning, and"
            " quality-of-life optimization in frail older patients."
        ),
    },
    {
        "Time": "15:00 - 16:00",
        "Track": "Case Discussion",
        "Title": (
            "Real-World Complex Scenarios: Multidisciplinary Panel Discussion"
        ),
        "Speaker": (
            "Panelists: Assoc. Prof. Dr. Norasyikin, Dr. Lydia, Assoc. Prof."
            " Dr. Hamat Hamdi (Cases presented by Nephrology Trainees)"
        ),
        "Room": "Main Auditorium",
        "Description": (
            "Interactive case presentations by nephrology fellows confronting"
            " real-world diagnostic dilemmas, refractory fluid overload, and"
            " conflicting treatment indications reviewed by endocrinology,"
            " nephrology, and cardiology chairs."
        ),
    },
    {
        "Time": "16:00 - 16:30",
        "Track": "General",
        "Title": "Interactive Clinical Quiz & Closing Ceremony",
        "Speaker": "Symposium Organizing Committee",
        "Room": "Main Auditorium",
        "Description": (
            "Audience participation quiz, awards presentation, and formal"
            " closing remarks."
        ),
    },
    {
        "Time": "17:00",
        "Track": "Break",
        "Title": "Afternoon Refreshments & CPD Endorsement",
        "Speaker": "-",
        "Room": "Auditorium Foyer",
        "Description": "",
    },
]

# ---------------------------------------------------------
# 5. LOGO & HEADER BANNER
# ---------------------------------------------------------
if found_logo:
  st.image(found_logo, use_container_width=True)

st.markdown(
    """
<div class="hero-banner">
    <div class="hero-badge">HCTM • Universiti Kebangsaan Malaysia</div>
    <div class="hero-title">5th UKM Renal Symposium</div>
    <div class="hero-subtitle">Breaking Silos: Integrated Care in Cardio-Kidney-Metabolic Health</div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 6. NAVIGATION TABS
# ---------------------------------------------------------
tab_agenda, tab_qa, tab_info = st.tabs(["📅 Programme", "💬 Live Q&A", "📍 Info"])

# --- TAB 1: SCIENTIFIC PROGRAMME ---
with tab_agenda:
  col_search, col_filter = st.columns([1.2, 1])
  with col_search:
    search_query = st.text_input(
        "Search",
        placeholder="Search topics or faculty...",
        label_visibility="collapsed",
    ).strip().lower()
  with col_filter:
    track_set = sorted(list({s["Track"] for s in SESSIONS}))
    selected_track = st.selectbox(
        "Track Filter", ["All Tracks"] + track_set, label_visibility="collapsed"
    )

  filtered = []
  for s in SESSIONS:
    if selected_track != "All Tracks" and s["Track"] != selected_track:
      continue
    if search_query:
      combined_text = f"{s['Title']} {s['Speaker']} {s['Description']}".lower()
      if search_query not in combined_text:
        continue
    filtered.append(s)

  st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

  if not filtered:
    st.info("No sessions match your search criteria.")
  else:
    for row in filtered:
      badge = render_badge(row["Track"])
      speaker_html = (
          f'<div class="session-speaker">👨‍⚕️ {row["Speaker"]}</div>'
          if row["Speaker"] and row["Speaker"] != "-"
          else ""
      )

      card_html = f"""<div class="session-card">
<div class="card-top">
<span class="session-time">⏰ {row['Time']}</span>
<span class="session-room">📍 {row['Room']}</span>
</div>
<div class="session-title">{row['Title']}</div>
{speaker_html}
<div>{badge}</div>
</div>"""

      st.markdown(card_html, unsafe_allow_html=True)

      if row.get("Description"):
        with st.expander("Session Synopsis & Clinical Objectives"):
          st.write(row["Description"])

# --- TAB 2: LIVE Q&A ---
with tab_qa:
  st.subheader("Audience Q&A & Live Polling")
  st.caption(
      "Submit questions directly to the panel chairs or upvote peer inquiries."
  )

  slido_url = "https://app.sli.do/event/ukmrenal2026"
  st.link_button("↗️ Open Q&A Fullscreen", slido_url, use_container_width=True)
  components.iframe(slido_url, height=540, scrolling=True)

# --- TAB 3: ESSENTIAL INFO & CPD ---
with tab_info:
  st.subheader("📲 Add to Home Screen")
  st.markdown("""
    Run this companion without the web browser address bar:
    
    * **iPhone / iPad (Safari):** Tap the **Share icon** (square with an up arrow `⎋`), scroll down, and tap **"Add to Home Screen"**.
    * **Android (Chrome):** Tap the **three dots menu (`⋮`)** in the top-right corner and tap **"Install App"** or **"Add to Home screen"**.
    """)

  st.divider()

  st.subheader("Symposium Guidelines")
  st.markdown("""
    **Event Venue:**  
    Auditorium Hospital Canselor Tuanku Muhriz (HCTM),  
    Jalan Yaacob Latif, Bandar Tun Razak, 56000 Cheras, Kuala Lumpur.

    ---
    **Dining & Exhibition:**  
    - Morning tea and lunch will be served at **The Gallery**.

    ---
    **Wi-Fi Access:**  
    - **Network (SSID):** `HCTM-Guest` / `UKM-Conference`  
    - **Password:** Available at the secretariat registration desk

    ---
    **CPD Accreditation:**  
    - Scan the official attendance verification QR code displayed on the main auditorium projection screen prior to the closing ceremony to claim your MMC / NSR CPD points.
    """)