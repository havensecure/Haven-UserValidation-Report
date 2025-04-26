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

# Inject dark background & branded fonts
st.markdown(
    """
    <style>
      /* overall background */
      .reportview-container, .stApp {
          background-color: #000000;
          color: #FFFFFF;
      }
      /* header accent box */
      .header-box {
          background: linear-gradient(90deg, #4B0082, #8A2BE2);
          padding: 2rem;
          border-radius: 12px;
          text-align: center;
      }
      .header-box h1 {
          margin: 0;
          font-size: 2.5rem;
      }
      .header-box p {
          margin: 0.5rem 0 0;
          font-size: 1.1rem;
          color: #DDDDDD;
      }
      /* metric cards */
      .stMetric > div {
          background-color: #111111 !important;
          border-radius: 8px;
          padding: 1rem;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# === LOAD DATA ===
df = pd.read_csv("Haven_Survey_Formatted_For_Form.csv")

# === HEADER ===
st.markdown(
    """
    <div class="header-box">
      <h1>🛡️ Haven Mobile App – Investor Insights</h1>
      <p>Deep dive into real user feedback on fit, pricing, features, trust and early-adopter appetite.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")

# === KEY METRICS ===
total = len(df)
install = (df["If this app existed, how likely are you to install it on your phone?"]=="Definitely").sum()
pay = (df["Would you be willing to pay for this app if it offered strong protection?"]!="No, I only use free tools").sum()
beta = (df["Want early access or to be part of our beta program?"]=="Yes").sum()

st.markdown("## 📊 Key Survey Highlights")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Responses", f"{total:,}")
m2.metric("High Install Intent", f"{install:,}")
m3.metric("Willing to Pay", f"{pay:,}")
m4.metric("Beta Access Interest", f"{beta:,}")

st.success("**Insight:** High install intent + pay willingness + beta eagerness = rock-solid early validation.")
st.write("---")

# === FEATURE DEMAND ===
st.markdown("## 🔧 Top Requested Features")
raw = df["Which of these features would personally convince you to use it?"].dropna()
items = [i for sub in raw.str.split(", ") for i in sub]
cnt = pd.Series(Counter(items)).sort_values().reset_index()
cnt.columns = ["Feature","Votes"]

fig = px.bar(
    cnt, x="Votes", y="Feature",
    orientation="h",
    color="Votes",
    color_continuous_scale=px.colors.sequential.Inferno,
    template="plotly_dark",
    title="Feature Demand"
)
fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000", plot_bgcolor="#000",
                  font_color="#EEE")
st.plotly_chart(fig, use_container_width=True)
st.info("Phishing alerts, dark-web monitoring & security score lead the pack—exactly our core pillars.")
st.write("---")

# === PERCEIVED VALUE ===
st.markdown("## 💡 Perceived Value")
fig = px.pie(
    df,
    names="How valuable does that sound to you?",
    hole=0.4,
    color_discrete_sequence=px.colors.sequential.Cividis,
    template="plotly_dark",
    title="User-Rated Value"
)
fig.update_traces(textinfo="percent+label", textfont_color="#FFF")
fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.success("> 80% say 'valuable' or better—strong product-market resonance.")
st.write("---")

# === PRICING & WILLINGNESS ===
st.markdown("## 💰 Pricing & Payment Appetite")
c1, c2 = st.columns(2)

with c1:
    price = df["What pricing would feel fair for this kind of app?"].value_counts().reset_index()
    price.columns = ["Tier","Count"]
    fig = px.bar(
        price, x="Count", y="Tier",
        orientation="h",
        color="Count", color_continuous_scale=px.colors.sequential.Inferno,
        template="plotly_dark",
        title="Preferred Price Point"
    )
    fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    fig = px.pie(
        df,
        names="Would you be willing to pay for this app if it offered strong protection?",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Cividis,
        template="plotly_dark",
        title="Payment Willingness"
    )
    fig.update_traces(textinfo="percent+label", textfont_color="#FFF")
    fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000")
    st.plotly_chart(fig, use_container_width=True)

st.info("Most comfortable at \$5–\$10/mo—validates our subscription model.")
st.write("---")

# === CONCERNS ===
st.markdown("## ⚠️ Top Security Concerns")
conc = df["What concerns you most when using your phone or laptop?"].value_counts().reset_index()
conc.columns = ["Concern","Count"]
fig = px.bar(
    conc, x="Count", y="Concern",
    orientation="h",
    color="Count", color_continuous_scale=px.colors.sequential.Inferno,
    template="plotly_dark",
    title="Primary User Worries"
)
fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.warning("Phishing, identity theft & breaches top list—Haven solves exactly that.")
st.write("---")

# === TRUST FACTORS ===
st.markdown("## 🔐 Key Trust Drivers")
trust = df["What would make you trust a cybersecurity app enough to use it daily?"].value_counts().reset_index()
trust.columns = ["Factor","Count"]
fig = px.bar(
    trust, x="Count", y="Factor",
    orientation="h",
    color="Count", color_continuous_scale=px.colors.sequential.Cividis,
    template="plotly_dark",
    title="What Builds Trust?"
)
fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.success("Privacy-first, transparency & proven protection = must-have trust pillars.")
st.write("---")

# === INSTALL INTENT ===
st.markdown("## 📲 Installation Likelihood")
inst = df["If this app existed, how likely are you to install it on your phone?"].value_counts().reset_index()
inst.columns = ["Intent","Count"]
fig = px.bar(
    inst, x="Count", y="Intent",
    orientation="h", color="Count", color_continuous_scale=px.colors.sequential.Inferno,
    template="plotly_dark",
    title="Install Intent"
)
fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.info("Strong install signals = green light for go-to-market.")
st.write("---")

# === BETA PROGRAM ===
st.markdown("## 🚀 Beta-Tester Appetite")
fig = px.pie(
    df,
    names="Want early access or to be part of our beta program?",
    hole=0.4,
    color_discrete_sequence=px.colors.sequential.Cividis,
    template="plotly_dark",
    title="Beta Interest"
)
fig.update_traces(textinfo="percent+label", textfont_color="#FFF")
fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="#000")
st.plotly_chart(fig, use_container_width=True)
st.success("A ready-to-go group of champions for our early launch.")
st.write("---")

# === CONCLUSION ===
st.markdown("## 📢 Conclusion & Investor Opportunity")
st.markdown(
    """
    - **Unmet Need**: Privacy-first personal cybersecurity  
    - **Validated Demand**: User-driven feature roadmap  
    - **Monetization**: Strong willingness to pay  
    - **Traction**: Eager beta community  

    **Haven Mobile App is uniquely positioned for explosive, defensible growth.**
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:#DDDDDD;'>Crafted with ❤️ by the Haven Team</p>",
    unsafe_allow_html=True
)
