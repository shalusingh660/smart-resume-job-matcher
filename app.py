import streamlit as st
from utils import (
    calculate_match_score,
    extract_text_from_pdf,
    find_missing_keywords,
)

st.set_page_config(
    page_title="AI Resume Screener - Bharat Cares", layout="centered"
)

st.title("📄 AI-Powered Resume Screening & Job Matcher")
st.write(
    "Upload a candidate's resume and paste the job description to calculate"
    " the match percentage and get improvement tips."
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
          delta=(
              "High Match" if match_score >= 50 else "Low Match - Needs Work"
          ),
      )

      # Condition: If match is low (less than 50%), show missing feedback
      if match_score < 50:
        st.warning(
            "⚠️ **Low Match Detected!** Your resume is missing several key"
            " terms required for this role."
        )

        missing_skills = find_missing_keywords(resume_text, jd_input)

        if missing_skills:
          st.subheader("🔍 Missing Keywords / Skills to Add:")
          st.write(
              "Consider incorporating the following important keywords found in"
              " the Job Description into your resume:"
          )

          # Display as a clean bulleted list
          for skill in missing_skills:
            st.markdown(f"- ❌ **{skill.capitalize()}**")
        else:
          st.info(
              "Try adding more technical details or aligning your project"
              " descriptions closely with the job description."
          )
      else:
        st.success(
            "🎉 **Great Match!** Your resume aligns well with the job"
            " description."
        )

      # Expandable section to check extracted text
      with st.expander("View Extracted Resume Text"):
        st.write(resume_text)