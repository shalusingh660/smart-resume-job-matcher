import re
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(pdf_file):
  """Extracts text from an uploaded PDF file."""
  text = ""
  with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
      extracted = page.extract_text()
      if extracted:
        text += extracted + "\n"
  return text


def clean_text(text):
  """Cleans text by removing special characters, numbers, and extra spaces."""
  text = re.sub(r"[^\w\s]", "", text)
  text = re.sub(r"\s+", " ", text)
  return text.lower()


def calculate_match_score(resume_text, jd_text):
  """Calculates cosine similarity between resume and job description."""
  cleaned_resume = clean_text(resume_text)
  cleaned_jd = clean_text(jd_text)

  vectorizer = TfidfVectorizer(stop_words="english")
  vectors = vectorizer.fit_transform([cleaned_resume, cleaned_jd])
  similarity = cosine_similarity(vectors[0:1], vectors[1:2])

  score = round(similarity[0][0] * 100, 2)
  return score


def find_missing_keywords(resume_text, jd_text):
  """Finds important keywords present in JD but missing from the resume."""
  cleaned_resume = clean_text(resume_text)
  cleaned_jd = clean_text(jd_text)

  # Use TF-IDF to extract important terms from JD and Resume
  vectorizer = TfidfVectorizer(stop_words="english", max_features=30)
  vectorizer.fit([cleaned_jd])
  jd_keywords = set(vectorizer.get_feature_names_out())

  # Words present in resume
  resume_words = set(cleaned_resume.split())

  # Find keywords in JD that are missing or less prominent in resume
  missing_keywords = [
      word for word in jd_keywords if word not in resume_words
  ]
  return missing_keywords[:10]  # Return top 10 missing keywords