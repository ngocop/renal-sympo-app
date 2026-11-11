import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# 1. PAGE SETUP (Mobile Viewport)
# ---------------------------------------------------------
st.set_page_config(
    page_title="5th UKM Renal Symposium 2026",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# 2. STYLING (Blue Clinical Theme & Responsive Cards)
# ---------------------------------------------------------
st.markdown("""
<style>
    .block-container {
        padding-top: 3.5rem;
        padding-bottom: 3.5rem;
        max-width: 600px;
    }
    .hero-banner {
        background: linear-gradient(135deg, #094067 0%, #176087 100%);
        border-radius: 12px;
        padding: 20px 18px;
        color: white;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(9, 64, 103, 0.15);
    }
    .hero-title {
        font-size: 1.35rem;
        font-weight: 800;
        margin: 0;
        color: #ffffff;
    }
    .hero-subtitle {
        font-size: 0.82rem;
        color: #e0f2fe;
        margin-top: 4px;
        line-height: 1.4;
    }
    .session-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 14px 16px;
        margin-bottom: 12px;
        border-left: 5px solid #0284c7;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .card-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 6px;
    }
    .session-time {
        font-weight: 700;
        color: #0369a1;
        font-size: 0.88rem;
    }
    .session-room {
        font-size: 0.78rem;
        color: #64748b;
        background: #f1f5f9;
        padding: 2px 8px;
        border-radius: 6px;
    }
    .session-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #0f172a;
        margin: 4px 0;
        line-height: 1.35;
    }
    .session-speaker {
        font-size: 0.86rem;
        color: #334155;
        margin-bottom: 8px;
    }
    .badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 600;
    }
    .badge-plenary { background: #f3e8ff; color: #7e22ce; }
    .badge-ckm { background: #e0f2fe; color: #0369a1; }
    .badge-break { background: #fef3c7; color: #92400e; }
    .badge-cardio { background: #fee2e2; color: #b91c1c; }
    .badge-pharma { background: #ccfbf1; color: #0f766e; }
    .badge-diet { background: #dcfce7; color: #15803d; }
    .badge-default { background: #f1f5f9; color: #475569; }
</style>
""", unsafe_allow_html=True)

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
# 3. SCIENTIFIC PROGRAMME (ENGLISH CLINICAL DESCRIPTIONS)
# ---------------------------------------------------------
SESSIONS = [
    {
        "Time": "07:30 - 08:15",
        "Track": "General",
        "Title": "Delegate Registration & Welcome Breakfast",
        "Speaker": "Organizing Secretariat",
        "Room": "Auditorium Foyer",
        "Description": "Delegate check-in, symposium kit distribution, and morning refreshments."
    },
    {
        "Time": "08:15 - 08:30",
        "Track": "General",
        "Title": "Arrival of VIPs & Guests of Honour",
        "Speaker": "Faculty Administration",
        "Room": "Main Auditorium",
        "Description": "Reception of invited dignitaries, faculty deans, and honorary guests."
    },
    {
        "Time": "08:30 - 09:15",
        "Track": "Plenary",
        "Title": "Official Opening Ceremony: 5th UKM Renal Symposium",
        "Speaker": "Prof. Dato' Dr. Marina Mat Baki (Dean, Faculty of Medicine)",
        "Room": "Main Auditorium",
        "Description": "Official opening address and inauguration of the 5th UKM Renal Symposium."
    },
    {
        "Time": "09:15 - 09:45",
        "Track": "Cardio-Kidney-Metabolic",
        "Title": "The Rise of CKM: Why We Must Break Clinical Silos",
        "Speaker": "Prof. Dr. Abdul Halim Abdul Gafor (Senior Consultant Nephrologist)",
        "Room": "Main Auditorium",
        "Description": "Rethinking multisystem care to bridge cardiology, nephrology, and endocrinology, focusing on unified screening, early risk interception, and coordinated organ protection."
    },
    {
        "Time": "09:45 - 10:15",
        "Track": "Metabolic & Diabetes",
        "Title": "The 'M' in CKM: Redefining Metabolic Control",
        "Speaker": "Prof. Dr. Christopher Lim (Senior Consultant Nephrologist)",
        "Room": "Main Auditorium",
        "Description": "Modernizing glycemic and metabolic targets in chronic kidney disease beyond traditional HbA1c metrics, emphasizing insulin resistance, body composition, and cardiorenal outcomes."
    },
    {
        "Time": "10:15 - 10:30",
        "Track": "Break",
        "Title": "Morning Tea & Exhibition Viewing",
        "Speaker": "-",
        "Room": "Auditorium Foyer",
        "Description": "Networking interval and exhibition booth visits."
    },
    {
        "Time": "10:30 - 11:00",
        "Track": "Cardiology & Renal",
        "Title": "The 'C' in CKRM: Pathophysiological Cardiorenal Crosstalk & Metabolic Involvement",
        "Speaker": "Assoc. Prof. Dr. Hamat Hamdi Che Hassan (Consultant Cardiologist)",
        "Room": "Main Auditorium",
        "Description": "Detailed dissection of reciprocal hemodynamic, neurohormonal, and inflammatory signaling between failing kidneys and myocardium in the presence of metabolic dysfunction."
    },
    {
        "Time": "11:00 - 11:30",
        "Track": "Cardiology & Renal",
        "Title": "Practical Challenges in Treating Heart Failure in Advanced CKD",
        "Speaker": "Dr. Hafidz Abd Hadi (Consultant Cardiologist)",
        "Room": "Main Auditorium",
        "Description": "Overcoming clinical hurdles in guideline-directed medical therapy (GDMT) titration, loop diuretic resistance, intravascular volume assessment, and cardiorenal syndrome in stage 4-5 CKD."
    },
    {
        "Time": "11:30 - 12:00",
        "Track": "Pharmacotherapy",
        "Title": "Polypharmacy in the CKM Spectrum",
        "Speaker": "Ms. Pau Kiew Bing (Clinical Pharmacist)",
        "Room": "Main Auditorium",
        "Description": "Deprescribing strategies, avoiding adverse drug-drug interactions, dose adjustments across fluctuating eGFR, and ensuring adherence in multimorbid cardiorenal patients."
    },
    {
        "Time": "12:00 - 12:30",
        "Track": "Clinical Nephrology",
        "Title": "Managing AKI Alerts and Hyperkalemia in CKM",
        "Speaker": "Assoc. Prof. Dr. Ruslinda Mustafar (Senior Consultant Nephrologist)",
        "Room": "Main Auditorium",
        "Description": "Distinguishing transient hemodynamic eGFR dips from true acute tubular injury, along with practical protocols for modern potassium binders to maintain RAASi and mineralocorticoid receptor antagonist therapy."
    },
    {
        "Time": "12:30 - 13:15",
        "Track": "Industry Symposium",
        "Title": "Lunch Symposium (DKSH): Navigating the Cardio-Kidney-Metabolic Spectrum with Novel nsMRAs",
        "Speaker": "Prof. Dr. Abdul Halim Abdul Gafor",
        "Room": "Main Auditorium",
        "Description": "Clinical trial evidence and real-world implementation of non-steroidal mineralocorticoid receptor antagonists in slowing kidney disease progression and mitigating cardiovascular events."
    },
    {
        "Time": "13:15 - 14:00",
        "Track": "Break",
        "Title": "Lunch & Midday Prayers",
        "Speaker": "-",
        "Room": "Dining Hall / Surau",
        "Description": "Complimentary buffet lunch and midday prayer break."
    },
    {
        "Time": "14:00 - 14:30",
        "Track": "Nutrition & Dietetics",
        "Title": "Optimizing Nutrition and Prevention of Sarcopenia: Challenges in CKM",
        "Speaker": "Prof. Dr. Barakatun Nisak Mohd Yusof (President, Malaysian Dietitians' Association)",
        "Room": "Main Auditorium",
        "Description": "Balancing protein restriction for kidney preservation against protein-energy wasting, sarcopenia prevention, and personalized dietary prescriptions in combined diabetic kidney disease and heart failure."
    },
    {
        "Time": "14:30 - 15:00",
        "Track": "Clinical Nephrology",
        "Title": "Conservative Kidney Management (CKM) in Advanced Cardiorenal Failure",
        "Speaker": "Assoc. Prof. Dr. Rozita Mohd (Senior Consultant Nephrologist)",
        "Room": "Main Auditorium",
        "Description": "Comprehensive non-dialytic supportive care pathways, symptom management (fatigue, dyspnea, edema), advance care planning, and quality-of-life optimization in frail older patients."
    },
    {
        "Time": "15:00 - 16:00",
        "Track": "Case Discussion",
        "Title": "Real-World Complex Scenarios: Multidisciplinary Panel Discussion",
        "Speaker": "Panelists: Assoc. Prof. Dr. Norasyikin, Dr. Lydia, Assoc. Prof. Dr. Hamat Hamdi (Cases presented by Nephrology Trainees)",
        "Room": "Main Auditorium",
        "Description": "Interactive case presentations by nephrology fellows confronting real-world diagnostic dilemmas, refractory fluid overload, and conflicting treatment indications reviewed by endocrinology, nephrology, and cardiology chairs."
    },
    {
        "Time": "16:00 - 16:30",
        "Track": "General",
        "Title": "Interactive Clinical Quiz & Closing Ceremony",
        "Speaker": "Symposium Organizing Committee",
        "Room": "Main Auditorium",
        "Description": "Audience participation quiz, awards presentation, and formal closing remarks."
    },
    {
        "Time": "17:00",
        "Track": "Break",
        "Title": "Afternoon Refreshments & CPD Endorsement",
        "Speaker": "-",
        "Room": "Auditorium Foyer",
        "Description": "Evening tea, delegate dispersal, and MMC/NSR CPD point validation."
    }
]

# Display logo centered at the top
st.image("logo.png", use_container_width=True)

# ---------------------------------------------------------
# 4. HERO BANNER
# ---------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">5th UKM Renal Symposium</div>
    <div class="hero-subtitle">Breaking Silos: Integrated Care in Cardio-Kidney-Metabolic Health • HCTM</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. NAVIGATION TABS
# ---------------------------------------------------------
tab_agenda, tab_qa, tab_info = st.tabs(["📅 Programme", "💬 Live Q&A", "📍 Info & CPD"])

# --- TAB 1: SCIENTIFIC PROGRAMME ---
with tab_agenda:
    col_search, col_filter = st.columns([1.2, 1])
    with col_search:
        search_query = st.text_input("Search", placeholder="Search topics or faculty...", label_visibility="collapsed").strip().lower()
    with col_filter:
        track_set = sorted(list({s["Track"] for s in SESSIONS}))
        selected_track = st.selectbox("Track Filter", ["All Tracks"] + track_set, label_visibility="collapsed")

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
            badge = render_badge(row['Track'])
            st.markdown(f"""
            <div class="session-card">
                <div class="card-top">
                    <span class="session-time">⏰ {row['Time']}</span>
                    <span class="session-room">📍 {row['Room']}</span>
                </div>
                <div class="session-title">{row['Title']}</div>
                <div class="session-speaker">👨‍⚕️ {row['Speaker']}</div>
                <div>{badge}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if row["Description"]:
                with st.expander("Session Synopsis & Clinical Objectives"):
                    st.write(row["Description"])

# --- TAB 2: LIVE Q&A ---
with tab_qa:
    st.subheader("Audience Q&A & Live Polling")
    st.caption("Submit questions directly to the panel chairs or upvote peer inquiries.")
    
    slido_url = "https://app.sli.do/event/jTJgeikbEWuQGg2gBT8Rai"
    st.link_button("↗️ Open Q&A Fullscreen", slido_url, use_container_width=True)
    components.iframe(slido_url, height=540, scrolling=True)

# --- TAB 3: ESSENTIAL INFO & CPD ---
with tab_info:
    st.subheader("Symposium Information")
    st.markdown("""
    **Event Venue:**  
    Auditorium Hospital Canselor Tuanku Muhriz (HCTM),  
    Jalan Yaacob Latif, Bandar Tun Razak, 56000 Cheras, Kuala Lumpur.

    ---
    **Wi-Fi Access:**  
    - **Network (SSID):** `HCTM-Guest` / `UKM-Conference`  
    - **Password:** Available at the secretariat registration desk

    ---
    **CPD Accreditation:**  
    - Scan the official attendance verification QR code displayed on the main auditorium projection screen prior to the closing ceremony to claim your MMC / NSR CPD points.
    """)