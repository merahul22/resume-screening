import streamlit as st
from resume_parser import parse_resume
from scorer import score_resume

import os
import pandas as pd
st.set_page_config(
    page_title="Resume Screening App",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🧠 Resume Screening App")

uploaded_jd = st.text_area("Paste Job Description")
uploaded_files = st.file_uploader("Upload Resumes (PDF/DOCX)", accept_multiple_files=True)

if uploaded_files and uploaded_jd:
    results = []
    for file in uploaded_files:
        text = parse_resume(file)
        score = score_resume(uploaded_jd, text)
        results.append({"Filename": file.name, "Score": score})

    df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
    st.dataframe(df)
    st.download_button("Download Results as CSV", df.to_csv(index=False), "results.csv")
st.markdown("""
---
Made with ❤️ by [Rahul Chourasiya](https://www.linkedin.com/in/rahul-chourasiya-b80882254/)  
📧 [rajrahul6572@gmail.com](mailto:rajrahul6572@gmail.com) | 🐙 [GitHub](https://github.com/merahul22) | 📸 [Instagram](https://www.instagram.com/me_rahul23/?hl=en)
""")