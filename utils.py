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

  # Convert to percentage
  score = round(similarity[0][0] * 100, 2)
  return score