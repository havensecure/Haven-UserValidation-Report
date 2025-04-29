import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

# === PAGE CONFIG & GLOBAL STYLES ===
st.set_page_config(
    page_title="Haven Mobile App | Cybersecurity Insights",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
    <style>
      /* Dark background */
      .reportview-container, .stApp {
          background-color: #000; color: #fff;
      }
      .main .block-container { padding: 0 1rem; }
      /* Header box */
      .header-box {
          background: linear-gradient(90deg, #4B0082, #8A2BE2);
          padding: 2rem 1rem; border-radius: 12px; text-align: center;
      }
      .header-box h1 { font-size: 2rem; margin-bottom: 0.2rem; }
      .header-box p  { font-size: 1rem; color: #ddd; margin-top: 0; }
      /* Metric cards */
      .stMetric > div {
          background: #111 !important; border-radius: 8px; padding: 1rem 0.5rem;
      }
      @media only screen and (max-width: 600px) {
        .header-box h1 { font-size: 1.5rem; }
      }
    </style>
""", unsafe_allow_html=True)

# === LOAD DATA ===
df = pd.read_csv("Haven_Survey_Formatted_For_Form_updated.csv")

# === HEADER ===
st.markdown("""
  <div class="header-box">
    <h1>🛡️ Haven Mobile App – Investor Insights</h1>
    <p>Deep dive into real user feedback on fit, pricing, features, trust & early-adopter appetite.</p>
  </div>
""", unsafe_allow_html=True)
st.write("")

# === KEY METRICS ===
total  = len(df)
install= (df["If this app existed, how likely are you to install it on your phone?"]=="Definitely").sum()
pay    = (df["Would you be willing to pay for this app if it offered strong protection?"]!="No, I only use free tools").sum()
beta   = (df["Want early access or to be part of our beta program?"]=="Yes").sum()

st.subheader("📊 Key Survey Highlights")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Responses", f"{total:,}")
c2.metric("High Install Intent", f"{install:,}", f"{install/total:.0%}")
c3.metric("Willing to Pay", f"{pay:,}", f"{pay/total:.0%}")
c4.metric("Beta Access Interest", f"{beta:,}", f"{beta/total:.0%}")

st.success("**Insight:** Strong install intent + payment willingness + eager beta community = rock-solid early validation.")
st.write("---")

# === FEATURE DEMAND ===
st.subheader("🔧 Top Requested Features")
raw = df["Which of these features would personally convince you to use it?"].dropna()
items = [i for sub in raw.str.split(", ") for i in sub]
cnt = pd.Series(Counter(items)).sort_values().reset_index()
cnt.columns = ["Feature","Votes"]

fig = px.bar(
    cnt, x="Votes", y="Feature", orientation="h",
    color="Votes", color_continuous_scale=px.colors.sequential.Inferno,
    template="plotly_dark", title="Feature Demand"
)
fig.update_layout(paper_bgcolor="#000", plot_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.info("Phishing alerts, dark-web monitoring & security scoring top the list.")
st.write("---")

# === PERCEIVED VALUE ===
st.subheader("💡 Perceived Value")
fig = px.pie(
    df, names="How valuable does that sound to you?",
    hole=0.4, template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.Cividis,
    title="User-Rated Value"
)
fig.update_traces(textinfo="percent+label")
fig.update_layout(paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.success("> 80% say “valuable” or “extremely valuable” — strong product-market resonance.")
st.write("---")

# === PRICING & WILLINGNESS ===
st.subheader("💰 Pricing & Payment Appetite")
p1, p2 = st.columns(2)
with p1:
    price = df["What pricing would feel fair for this kind of app?"].value_counts().reset_index()
    price.columns = ["Tier","Count"]
    fig = px.bar(
        price, x="Count", y="Tier", orientation="h",
        color="Count", color_continuous_scale=px.colors.sequential.Inferno,
        template="plotly_dark", title="Preferred Price Point"
    )
    fig.update_layout(paper_bgcolor="#000")
    st.plotly_chart(fig, use_container_width=True)
with p2:
    fig = px.pie(
        df, names="Would you be willing to pay for this app if it offered strong protection?",
        hole=0.4, template="plotly_dark",
        color_discrete_sequence=px.colors.sequential.Cividis,
        title="Willingness to Pay"
    )
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(paper_bgcolor="#000")
    st.plotly_chart(fig, use_container_width=True)
st.info("Majority comfortable at \$5–\$10/mo — validates subscription model.")
st.write("---")

# === SECURITY CONCERNS ===
st.subheader("⚠️ Top Security Concerns")
conc = df["What concerns you most when using your phone or laptop?"].value_counts().reset_index()
conc.columns = ["Concern","Count"]
fig = px.bar(
    conc, x="Count", y="Concern", orientation="h",
    color="Count", color_continuous_scale=px.colors.sequential.Inferno,
    template="plotly_dark", title="Primary User Worries"
)
fig.update_layout(paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.warning("Phishing, identity theft & breaches lead concerns.")
st.write("---")

# === TRUST FACTORS ===
st.subheader("🔐 Key Trust Drivers")
trust = df["What would make you trust a cybersecurity app enough to use it daily?"].value_counts().reset_index()
trust.columns = ["Factor","Count"]
fig = px.bar(
    trust, x="Count", y="Factor", orientation="h",
    color="Count", color_continuous_scale=px.colors.sequential.Cividis,
    template="plotly_dark", title="What Builds Trust?"
)
fig.update_layout(paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.success("Privacy-first design, transparency & proven protection = must-have trust pillars.")
st.write("---")

# === INSTALL INTENT ===
st.subheader("📲 Installation Likelihood")
inst = df["If this app existed, how likely are you to install it on your phone?"].value_counts().reset_index()
inst.columns = ["Intent","Count"]
fig = px.bar(
    inst, x="Count", y="Intent", orientation="h",
    color="Count", color_continuous_scale=px.colors.sequential.Inferno,
    template="plotly_dark", title="Install Intent"
)
fig.update_layout(paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.info("Strong install signals — green light for go-to-market.")
st.write("---")

# === BETA PROGRAM ===
st.subheader("🚀 Beta-Tester Appetite")
fig = px.pie(
    df, names="Want early access or to be part of our beta program?",
    hole=0.4, template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.Cividis,
    title="Beta Interest"
)
fig.update_traces(textinfo="percent+label")
fig.update_layout(paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.success("A ready-to-go group of champions for our early launch.")
st.write("---")

# === MARKET SIZING & TAM VALIDATION ===
st.subheader("🌐 Market Sizing & TAM Validation")

# Metrics panels
colT, colM, colS, colO = st.columns(4)
colT.metric("🌍 TAM", "4.5 B Users", "Global smartphone base – GSMA ’24")
colM.metric("💼 Cybersecurity Spend", "$60 B", "Consumer segment – Gartner ’24")
colS.metric("🔒 SAM", "900 M Users", "20% high-risk segment – Statista + Survey")
colO.metric("🚀 SOM (Yr 1)", "9 M Users", "1% of SAM; \$45 M ARR")

# Detailed insight + plan
st.markdown("""
**Insights:**  
- **Huge runway**: Only ~20% of smartphone users actively seek enhanced protection.  
- **Rapid growth**: Consumer cybersecurity is growing at **10% CAGR**—momentum on our side.  
- **Early traction target**: 1% of SAM (9 M users) in **Year 1** yields \$45 M ARR at \$5/mo.

**3-Phase GTM Plan to Capture SOM:**  
1. **Q3–Q4 2025: Launch & Awareness**  
   - Beta pilot with 100 K power users (existing waitlist).  
   - PR & security-blog partnerships to drive 1 M site visits.  
   - Paid social ads targeting high-risk cohorts (CPSU < \$3).

2. **Q1–Q2 2026: Conversion & Scale**  
   - Convert 20% of engaged visitors → 200 K installs.  
   - In-app referral program to boost viral K-factor > 1.  
   - Partnership promotions: telcos & device OEMs to white-label Haven.

3. **Q3 2026 Onward: Expansion & Retention**  
   - Roll out multi-platform (iOS/Android + desktop) to expand SAM by +50 M.  
   - Enterprise edition targeting SMBs for additional revenue stream.  
   - Continuous optimization: A/B pricing, feature upsells, loyalty rewards.

> **By end-of-2026**, we project **2 M paying subscribers** (~\$120 M ARR).  
> **Year 3 SOM** (5% of SAM = 45 M users) represents **\$2.7 B ARR** potential.

*Data sources: GSMA Intelligence ’24, Gartner ’24, Statista 2025, Haven April ’25 Survey*
""")
st.write("---")


# === CONCLUSION ===
st.subheader("📢 Conclusion & Investment Opportunity")
st.markdown("""
- **Unmet Need:** Privacy-first personal cybersecurity  
- **Validated Demand:** User-prioritized feature roadmap  
- **Monetization:** Strong subscription willingness  
- **Traction:** Eager beta community  

**Haven Mobile App is positioned for rapid, defensible growth in the expanding cybersecurity market.**
""")
st.markdown(
    "<p style='text-align:center;color:#DDD;'>Crafted with ❤️ by the Haven Team</p>",
    unsafe_allow_html=True
)
