# 📄 AI-Powered Resume Screening & Job Matching System

An intelligent recruitment support application developed as an AI/ML project submission for the **AICTE Internship** in association with **Bharat Cares**. 

This system automates the preliminary resume screening process by comparing candidate resumes against a given Job Description (JD) using Natural Language Processing (NLP) and Machine Learning, helping reduce hiring bias and saving valuable evaluation time.

---

## 🚀 Features
* **PDF Text Extraction:** Seamlessly extracts and parses raw text from uploaded candidate resumes.
* **TF-IDF Vectorization:** Converts textual data into numerical feature vectors.
* **Cosine Similarity Matching:** Computes an accurate match percentage score between the resume and the job description.
* **Interactive Web Dashboard:** Clean, user-friendly interface built with **Streamlit** for instant evaluation and results.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend/UI:** Streamlit
* **Machine Learning & NLP:** Scikit-Learn, NLTK
* **Document Processing:** pdfplumber

---

## 📂 Project Structure
```text
resume_screener/
│
├── app.py              # Main Streamlit web application
├── utils.py            # Text extraction, cleaning, and matching algorithms
├── requirements.txt    # Project dependencies
└── .gitignore          # Ignored cache and environment files