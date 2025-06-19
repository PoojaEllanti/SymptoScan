import streamlit as st
from utils import load_data, match_symptoms

# Set up the app
st.set_page_config(page_title="SymptoScan", page_icon="🩺", layout="centered")

# Custom styles
st.markdown("""
    <style>
    .title {
        font-size: 2.8em;
        text-align: center;
        color: #2c3e50;
        font-weight: bold;
    }
    .subtitle {
        font-size: 1.3em;
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 30px;
    }
    .card {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .match {
        font-weight: bold;
        color: #16a085;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">🩺 SymptoScan</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Smart Symptom Checker</div>', unsafe_allow_html=True)

# Input area
st.markdown("### 👉 Enter your symptoms below (comma-separated)")
user_input = st.text_input("E.g. fever, cough, headache", "")

# Analyze Button
if st.button("🔍 Analyze Symptoms"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter at least one symptom.")
    else:
        user_symptoms = [s.strip().lower() for s in user_input.split(",")]
        data = load_data()
        results = match_symptoms(user_symptoms, data)

        if results:
            st.success("✅ We found some possible conditions:")
            for res in results:
                st.markdown(f"""
                    <div class="card">
                        <h4>{res['condition']} 🩺</h4>
                        <p class="match">Match Confidence: {res['match_percent']}%</p>
                        <p><strong>Advice:</strong> {res['advice']}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("😕 No matching condition found. Try more common or specific symptoms.")

# Footer
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ for global health awareness</center>",
    unsafe_allow_html=True
)
