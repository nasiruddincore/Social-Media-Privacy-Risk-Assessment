import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Social Media Privacy Risk Framework", page_icon="🛡️", layout="wide")

# --- ABSOLUTE PATH RESOLUTION & SELF-HEALING DATA GENERATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "social_media_privacy_assessments.csv")

def ensure_dataset_exists():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        data = []
        for i in range(1000):
            p, pi, loc, con, conn, tag, sec, tp, se, df_fp = (
                random.randint(10, 90), random.randint(20, 100), random.randint(10, 90),
                random.randint(10, 80), random.randint(20, 100), random.randint(0, 80),
                random.randint(30, 100), random.randint(0, 90), random.randint(20, 90), random.randint(10, 90)
            )
            overall = int(p*0.1 + pi*0.15 + loc*0.15 + con*0.1 + conn*0.1 + tag*0.05 + sec*0.15 + tp*0.05 + se*0.1 + df_fp*0.05)
            lvl = "LOW" if overall <= 20 else ("MODERATE" if overall <= 40 else ("HIGH" if overall <= 70 else "CRITICAL"))
            data.append({
                "assessment_id": f"ASM-{1000+i}", "Profile Visibility": p, "Personal Information": pi,
                "Location Privacy": loc, "Posts & Content": con, "Connections": conn, "Tagging": tag,
                "Account Security": sec, "Third-Party Apps": tp, "Social Engineering": se, "Digital Footprint": df_fp,
                "overall_score": overall, "risk_level": lvl
            })
        pd.DataFrame(data).to_csv(CSV_PATH, index=False)

ensure_dataset_exists()

# --- 40+ QUESTIONNAIRE DATA STRUCTURE ---
QUESTIONS = [
    # A. Profile Visibility
    ("Profile Visibility", "Is your social media profile publicly visible?", ["Yes", "Friends Only", "No"], [10, 5, 0]),
    ("Profile Visibility", "Can search engines index your profile?", ["Yes", "Not Sure", "No"], [10, 5, 0]),
    ("Profile Visibility", "Is your friends/followers list public?", ["Yes", "Friends Only", "No"], [10, 5, 0]),
    ("Profile Visibility", "Do you use your full legal name as your primary handle?", ["Yes", "Partially", "No"], [10, 5, 0]),
    
    # B. Personal Information
    ("Personal Information", "Is your phone number publicly visible?", ["Yes", "Friends Only", "No"], [10, 5, 0]),
    ("Personal Information", "Is your personal email publicly visible?", ["Yes", "Friends Only", "No"], [10, 5, 0]),
    ("Personal Information", "Is your full birth date (including year) visible?", ["Yes", "Month/Day Only", "No"], [10, 5, 0]),
    ("Personal Information", "Is your home city or address visible?", ["Yes", "State/Country Only", "No"], [10, 5, 0]),
    ("Personal Information", "Is your current workplace publicly listed?", ["Yes", "Past Only", "No"], [10, 5, 0]),
    ("Personal Information", "Are your family relationships linked publicly?", ["Yes", "Friends Only", "No"], [10, 5, 0]),
    
    # C. Location Privacy
    ("Location Privacy", "Do you share your real-time location automatically?", ["Yes", "Sometimes", "No"], [10, 5, 0]),
    ("Location Privacy", "Do you geotag posts with specific venues or restaurants?", ["Always", "Sometimes", "Never"], [10, 5, 0]),
    ("Location Privacy", "Do you post travel plans before or during a trip?", ["Yes", "Sometimes", "After returning"], [10, 5, 0]),
    ("Location Privacy", "Do you post photos showing the exterior or layout of your home?", ["Yes", "Not Sure", "No"], [10, 5, 0]),
    
    # D. Posts & Content
    ("Posts & Content", "Are your historical posts globally public?", ["Yes", "Friends Only", "No"], [10, 5, 0]),
    ("Posts & Content", "Do you post photos featuring your workplace badge or ID card?", ["Yes", "Sometimes", "No"], [10, 5, 0]),
    ("Posts & Content", "Do your photos display vehicle license plates?", ["Yes", "Sometimes", "No"], [10, 5, 0]),
    ("Posts & Content", "Do you post pictures of sensitive documents (tickets, mail)?", ["Yes", "Sometimes", "No"], [10, 5, 0]),
    
    # E. Connections
    ("Connections", "Do you accept connection requests from unknown individuals?", ["Often", "Sometimes", "Never"], [10, 5, 0]),
    ("Connections", "Do you periodically audit and remove unknown followers?", ["Never", "Rarely", "Regularly"], [10, 5, 0]),
    ("Connections", "Can anyone send you direct messages?", ["Yes", "Filtered", "Connections Only"], [10, 5, 0]),
    ("Connections", "Do you verify the identity of duplicate or cloned friend requests?", ["Never", "Sometimes", "Always"], [10, 5, 0]),
    
    # F. Tagging & Mentions
    ("Tagging", "Can anyone tag you in photos or posts without approval?", ["Yes", "Friends Only", "No"], [10, 5, 0]),
    ("Tagging", "Do tagged posts appear on your profile automatically?", ["Yes", "Not Sure", "No"], [10, 5, 0]),
    ("Tagging", "Can unknown users mention or tag your account?", ["Yes", "Not Sure", "No"], [10, 5, 0]),
    ("Tagging", "Do you untag yourself from exposed or risky photos?", ["Never", "Sometimes", "Always"], [10, 5, 0]),
    
    # G. Account Security
    ("Account Security", "Do you use Multi-Factor Authentication (MFA)?", ["No", "SMS Only", "Authenticator App/Key"], [10, 5, 0]),
    ("Account Security", "Do you reuse your passwords across accounts?", ["Yes", "Not Sure", "No (Unique)"], [10, 5, 0]),
    ("Account Security", "Are login alerts for unrecognized devices enabled?", ["No", "Not Sure", "Yes"], [10, 5, 0]),
    ("Account Security", "Do you utilize a dedicated password manager?", ["No", "Browser Built-in", "Dedicated App"], [10, 5, 0]),
    ("Account Security", "Have you reviewed your active login sessions recently?", ["No", "Not Sure", "Yes"], [10, 5, 0]),
    
    # H. Third-Party Apps
    ("Third-Party Apps", "Do you log in to external sites using social accounts?", ["Often", "Sometimes", "Never"], [10, 5, 0]),
    ("Third-Party Apps", "Do you regularly review connected third-party apps and games?", ["Never", "Rarely", "Regularly"], [10, 5, 0]),
    ("Third-Party Apps", "Do you grant apps permission to access your contacts list?", ["Yes", "Sometimes", "No"], [10, 5, 0]),
    ("Third-Party Apps", "Have you revoked permissions for unused integrations?", ["No", "Not Sure", "Yes"], [10, 5, 0]),
    
    # I. Social Engineering
    ("Social Engineering", "Have you ever shared verification codes via direct messages?", ["Yes", "Not Sure", "Never"], [10, 5, 0]),
    ("Social Engineering", "Do you click links sent in unsolicited messages?", ["Often", "Sometimes", "Never"], [10, 5, 0]),
    ("Social Engineering", "Do you participate in public 'get to know me' social quizzes?", ["Yes", "Sometimes", "No"], [10, 5, 0]),
    ("Social Engineering", "Have you engaged with cloned or impersonated accounts?", ["Yes", "Not Sure", "No"], [10, 5, 0]),
    
    # J. Digital Footprint
    ("Digital Footprint", "Do you maintain unused or abandoned social accounts?", ["Yes", "Not Sure", "No"], [10, 5, 0]),
    ("Digital Footprint", "Have you audited your historical public posts?", ["Never", "Rarely", "Recently"], [10, 5, 0]),
    ("Digital Footprint", "Do you delete posts containing outdated personal info?", ["No", "Sometimes", "Yes"], [10, 5, 0]),
    ("Digital Footprint", "Have you searched your name or handle on search engines recently?", ["No", "Years ago", "Recently"], [10, 5, 0])
]

CATEGORY_WEIGHTS = {
    "Profile Visibility": 0.10, "Personal Information": 0.15, "Location Privacy": 0.15,
    "Posts & Content": 0.10, "Connections": 0.10, "Tagging": 0.05,
    "Account Security": 0.15, "Third-Party Apps": 0.05, 
    "Social Engineering": 0.10, "Digital Footprint": 0.05
}

def calculate_category_scores(responses):
    cat_scores = {cat: 0 for cat in CATEGORY_WEIGHTS.keys()}
    cat_max = {cat: 0 for cat in CATEGORY_WEIGHTS.keys()}
    
    for (cat, q, opts, risks), ans in zip(QUESTIONS, responses):
        idx = opts.index(ans)
        cat_scores[cat] += risks[idx]
        cat_max[cat] += max(risks)
        
    for cat in cat_scores:
        if cat_max[cat] > 0:
            cat_scores[cat] = int((cat_scores[cat] / cat_max[cat]) * 100)
    return cat_scores

def calculate_overall_risk(cat_scores):
    return int(sum(cat_scores[cat] * weight for cat, weight in CATEGORY_WEIGHTS.items()))

def get_risk_level(score):
    if score <= 20: return "LOW", "#2ecc71"
    elif score <= 40: return "MODERATE", "#f39c12"
    elif score <= 70: return "HIGH", "#e67e22"
    else: return "CRITICAL", "#e74c3c"

def generate_recommendations(cat_scores):
    recs = []
    if cat_scores["Personal Information"] > 40:
        recs.append("🚨 **Immediate:** Remove phone number, email, and birth year from public view to mitigate doxxing risks.")
    if cat_scores["Account Security"] > 40:
        recs.append("🚨 **Immediate:** Enable authenticator-based Multi-Factor Authentication (MFA) and enforce unique passwords.")
    if cat_scores["Location Privacy"] > 40:
        recs.append("⚠️ **Important:** Disable real-time location sharing and delay publishing travel updates until after you return.")
    if cat_scores["Connections"] > 40:
        recs.append("⚠️ **Important:** Restrict direct messaging and stop accepting connection requests from unverified profiles.")
    if cat_scores["Third-Party Apps"] > 40:
        recs.append("💡 **Good Practice:** Review and revoke access tokens for unused third-party applications.")
    return recs

# --- UI LAYOUT ---
st.title("🛡️ Social Media Privacy Risk Assessment Framework")
st.markdown("Defensive cybersecurity platform to evaluate digital footprint exposure, review privacy configurations, and simulate security improvements.")

menu = st.sidebar.radio("Navigation", ["Privacy Analytics Dashboard", "Privacy Assessment Questionnaire"])

if menu == "Privacy Analytics Dashboard":
    st.header("📊 Aggregated Privacy Risk Intelligence")
    st.markdown("*(Data driven by synthetic educational assessments. Operates strictly on self-reported posture without scraping real user profiles.)*")
    
    df = pd.read_csv(CSV_PATH)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Assessments Logged", len(df))
    col2.metric("Average Risk Score", f"{df['overall_score'].mean():.1f}/100")
    col3.metric("Critical Exposure Accounts", len(df[df['risk_level'] == 'CRITICAL']))
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Risk Level Distribution")
        fig_pie = px.pie(df, names='risk_level', color='risk_level', 
                         color_discrete_map={"LOW":"#2ecc71", "MODERATE":"#f39c12", "HIGH":"#e67e22", "CRITICAL":"#e74c3c"})
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with c2:
        st.subheader("Average Category Vulnerability")
        cat_avgs = df[[c for c in df.columns if c in CATEGORY_WEIGHTS.keys()]].mean().reset_index()
        cat_avgs.columns = ['Category', 'Avg Risk Score']
        fig_bar = px.bar(cat_avgs, x='Category', y='Avg Risk Score', color='Avg Risk Score', color_continuous_scale='Reds')
        st.plotly_chart(fig_bar, use_container_width=True)

elif menu == "Privacy Assessment Questionnaire":
    st.header("📝 Personal Privacy Audit & Scoring Engine")
    st.info("**Privacy by Design:** This framework evaluates your configuration posture, not your sensitive data. Do NOT input actual phone numbers, passwords, or PII. All processing occurs locally.")
    
    with st.form("assessment_form"):
        user_responses = []
        current_cat = ""
        
        for cat, q, opts, risks in QUESTIONS:
            if cat != current_cat:
                st.markdown(f"### 📂 {cat}")
                current_cat = cat
            ans = st.radio(q, opts, horizontal=True)
            user_responses.append(ans)
            
        submitted = st.form_submit_button("Generate Privacy Risk Score")
        
    if submitted:
        cat_scores = calculate_category_scores(user_responses)
        overall = calculate_overall_risk(cat_scores)
        level, color = get_risk_level(overall)
        
        st.markdown("---")
        st.header("🎯 Assessment Results & Findings")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"<h1 style='text-align: center; color: {color}; font-size: 4rem;'>{overall}/100</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center; color: {color};'>{level} RISK LEVEL</h3>", unsafe_allow_html=True)
            
            st.markdown("### Personalized Security Recommendations")
            for rec in generate_recommendations(cat_scores):
                st.write(rec)
                
        with col2:
            st.subheader("Category Risk Radar Analysis")
            df_radar = pd.DataFrame(dict(r=list(cat_scores.values()), theta=list(cat_scores.keys())))
            fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True, range_r=[0,100])
            fig.update_traces(fill='toself', fillcolor='rgba(231, 76, 60, 0.4)', line_color='red')
            st.plotly_chart(fig, use_container_width=True)
            
        st.markdown("---")
        st.header("🔄 Privacy Improvement Simulator")
        st.write("Simulate hardening your configuration settings to calculate potential risk reduction:")
        
        sim_scores = cat_scores.copy()
        if st.checkbox("Simulate hiding public PII (Phone/Email/DOB/Workplace)"): 
            sim_scores["Personal Information"] = 0
        if st.checkbox("Simulate enforcing strict Account Security (MFA & Password Manager)"): 
            sim_scores["Account Security"] = 0
        if st.checkbox("Simulate disabling real-time Location sharing & travel check-ins"): 
            sim_scores["Location Privacy"] = 0
        if st.checkbox("Simulate restricting unknown Connections & DM requests"): 
            sim_scores["Connections"] = 0
            
        new_overall = calculate_overall_risk(sim_scores)
        new_level, new_color = get_risk_level(new_overall)
        
        st.success(f"**Simulated New Score:** {new_overall}/100 ({new_level}) — A risk reduction of **{overall - new_overall} points**!")