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