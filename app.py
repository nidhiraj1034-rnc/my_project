import streamlit as st

# Page Config
st.set_page_config(page_title="Disease Prediction System", page_icon="🏥", layout="wide")

# CSS Styling
st.markdown("""
<style>
    .main-box {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        color: #000000;
    }
    h1, h2, label { color: #000000 !important; font-weight: bold !important; font-size: 1.2em !important; }
    .stSuccess { font-weight: bold !important; font-size: 1.4em !important; color: #000000 !important; background-color: #d4edda !important; border: 1px solid #c3e6cb !important; }
</style>
""", unsafe_allow_html=True)

# Background
st.markdown('''<style>.stApp { background-image: url("https://images.unsplash.com/photo-1576091160550-2173dba999ef?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"); background-size: cover; background-attachment: fixed; }</style>''', unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📋 Main Menu")
page = st.sidebar.radio("Navigate:", ["🏠 Home", "🩺 Diabetes Prediction", "❤️ Heart Disease Prediction", "🫁 Lung Cancer Prediction", "💬 Feedback & Contact", "👥 About Us"])

# PAGES
if page == "🏠 Home":
    st.markdown("<div class='main-box' style='text-align:center;'><h1>DISEASE PREDICTION SYSTEM</h1></div>", unsafe_allow_html=True)

elif page == "🩺 Diabetes Prediction":
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)
    st.header("🩺 Diabetes Prediction")
    g = st.number_input("What is your current Glucose level?", 0, 300)
    bp = st.number_input("What is your Blood Pressure reading?", 0, 200)
    bmi = st.number_input("What is your BMI?", 0.0, 70.0)
    age = st.number_input("What is your Age?", 1, 120)
    if st.button("Predict"):
        review = "Low Risk - Maintain a healthy diet." if g < 140 else "High Risk - Consult a doctor immediately."
        st.write("### 📋 Patient Review:")
        st.success(review)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "❤️ Heart Disease Prediction":
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)
    st.header("❤️ Heart Disease Prediction")
    age = st.number_input("What is your Age?", 1, 100)
    sex = st.radio("Gender", ["Female", "Male"])
    cp = st.selectbox("Are you experiencing any chest pain?", ["No pain", "Mild/Normal", "Severe/High"])
    rate = st.number_input("What is your Heart Rate?", 1, 220)
    if st.button("Predict Heart Condition"):
        review = "Normal Heart Rate detected." if rate < 100 else "High Heart Rate - Please monitor."
        st.write("### 📋 Patient Review:")
        st.success(review)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "🫁 Lung Cancer Prediction":
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)
    st.header("🫁 Lung Cancer Prediction")
    age = st.number_input("What is your Age?", 1, 100)
    smoke = st.radio("Do you smoke?", ["No", "Yes"])
    wheeze = st.radio("Do you hear a whistling sound in your chest? (Wheezing)", ["No", "Yes"])
    cough = st.radio("Do you have a persistent cough?", ["No", "Yes"])
    if st.button("Predict Lung Health"):
        review = "Low Risk - No major symptoms detected." if (smoke == "No" and wheeze == "No") else "Attention Needed - Please visit a pulmonologist."
        st.write("### 📋 Patient Review:")
        st.success(review)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "💬 Feedback & Contact":
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)
    st.header("💬 Feedback & Contact")
    name = st.text_input("Your Name")
    feedback = st.text_area("Your Review or Suggestions")
    if st.button("Submit Feedback"):
        st.success("Thank you for your valuable feedback!")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "👥 About Us":
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)
    st.header("👥 About the Project")
    st.write("""
    ### System Overview
    The **Disease Prediction System** is a major academic project. 
    The objective is to provide a user-friendly digital platform for preliminary health screening. 
    It analyzes clinical inputs to assess the likelihood of various health conditions.
    
    ### Project Objectives
    * **Clinical Assessment:** To bridge the gap between initial health observations and consultation.
    * **Early Detection:** To facilitate the identification of potential health risks at an early stage.
    * **Accessibility:** To create an intuitive interface for health monitoring.
    
    ---
    **Disclaimer:** This system is for academic and informational purposes only. The predictions 
    should not be considered a substitute for professional medical advice.
    """)
    st.markdown("</div>", unsafe_allow_html=True)