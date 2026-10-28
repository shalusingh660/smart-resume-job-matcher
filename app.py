import streamlit as st
from utils import calculate_match_score, extract_text_from_pdf

st.set_page_config(
    page_title="AI Resume Screener - Bharat Cares", layout="centered"
)

st.title("📄 AI-Powered Resume Screening & Job Matcher")
st.write(
    "Upload a candidate's resume and paste the job description to calculate"
    " the match percentage."
)

# Input: Job Description
st.subheader("1. Job Description")
jd_input = st.text_area(
    "Paste the Job Description here:",
    placeholder="e.g., Looking for a Python developer with experience in"
    " Streamlit...",
)

# Input: Resume Upload
st.subheader("2. Candidate Resume")
uploaded_file = st.file_uploader("Upload Resume (PDF format)", type=["pdf"])

if st.button("Evaluate Match"):
  if not jd_input:
    st.warning("Please enter a Job Description.")
  elif not uploaded_file:
    st.warning("Please upload a resume PDF.")
  else:
    with st.spinner("Analyzing resume and computing match score..."):
      # Extract text from uploaded PDF
      resume_text = extract_text_from_pdf(uploaded_file)

      # Calculate score
      match_score = calculate_match_score(resume_text, jd_input)

      st.success("Analysis Complete!")

      # Display Score metric
      st.metric(
          label="Job Match Score",
          value=f"{match_score}%",
          delta="High Match" if match_score > 50 else "Low Match",
      )

      # Expandable section to check extracted text
      with st.expander("View Extracted Resume Text"):
        st.write(resume_text)