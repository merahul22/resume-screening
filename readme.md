# 🧠 Resume Screening App

A smart, beginner-friendly Streamlit application that screens and ranks resumes against a job description using NLP-based text similarity.

---

## 🚀 Features

- 📄 Parse PDF and DOCX resumes
- 🧠 Score resumes based on cosine similarity with TF-IDF
- 📊 Display ranked results with download option
- 🌑 Dark mode UI for better readability
- ✅ Simple to set up and deploy

---

## 📁 Folder Structure

```
resume-screening/
├── app/
│   ├── main.py              # Streamlit App
│   ├── resume_parser.py     # Text extraction from resumes
│   └── scorer.py            # TF-IDF based scoring logic
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .streamlit/config.toml   # Dark mode theme setup
```

---

## 🧪 How to Run

```bash
# Clone the repo
https://github.com/your-username/resume-screening-app.git
cd resume-screening-app

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app/main.py
```

---
## 🧠 How It Works: TF-IDF + Cosine Similarity

This app ranks resumes based on how closely their content matches a job description using the following NLP techniques:

- **TF-IDF (Term Frequency – Inverse Document Frequency)**  
  Measures how important a word is to a document relative to all documents. It gives higher weight to unique, meaningful terms like “pandas” or “machine learning” and lower weight to common words like “the” or “and”.

- **Cosine Similarity**  
  Measures the angle between two TF-IDF vectors: one for the job description, one for the resume. A smaller angle (closer to 1) means higher similarity.

> Final score is shown as a percentage — higher means more relevant.



## 📌 Tech Stack
- Python
- Streamlit
- PyMuPDF (PDF parsing)
- docx2txt (DOCX parsing)
- scikit-learn (TF-IDF & similarity)
- Pandas

---

## 📬 Contact
Created by **Rahul Chourasiya**. Feel free to reach out via rajrahul6572@gmail.com.