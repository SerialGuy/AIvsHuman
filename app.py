# app.py
import streamlit as st
from predictor import predict_text

st.set_page_config(page_title="AI vs Human Text Detector", page_icon="🤖", layout="centered")

st.title("🤖 AI vs Human Text Detector")
st.markdown("Check if the given text was written by an **AI model** or a **human**.")

text_input = st.text_area("Enter text here", height=200)

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        prediction, confidence = predict_text(text_input)
        
        if prediction == 1:
            st.success("**Class**: 🤖 AI-Generated")
            st.info(f"**Confidence**: {confidence * 100:.2f}% (AI)")
        else:
            st.success("**Class**: 🧠 Human-Written")
            st.info(f"**Confidence**: {(1 - confidence) * 100:.2f}% (Human)")

