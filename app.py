%%writefile app.py
import streamlit as st
import pandas as pd
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_resource 
def load_resources():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    df = pd.read_csv('resume_data.csv')
    return model, df

model, df = load_resources()

def clean_data(text):
    text = re.sub(r'http\S+\s*', ' ', text)  
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)
    text = re.sub(r'[^\x00-\x7f]', r' ', text) 
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

st.title("🚀 AI Resume Screener")
st.subheader("Match Resumes to Job Descriptions Instantly")

with st.sidebar:
    st.header("Job Settings")
    jd_input = st.text_area("Enter Job Description here:", height=300)
    num_results = st.slider("Number of candidates to show", 1, 10, 5)

if st.button("Start Screening"):
    if jd_input:
        with st.spinner("Processing..."):
        
            cleaned_jd = clean_data(jd_input)
            jd_embedding = model.encode([cleaned_jd])

            columns_to_combine = ['career_objective', 'skills', 'major_field_of_studies', 'responsibilities']
            df['combined_text'] = df[columns_to_combine].fillna('').agg(' '.join, axis=1)
            df['cleaned_resume'] = df['combined_text'].apply(clean_data)
            
            resume_embeddings = model.encode(df['cleaned_resume'].tolist())

            scores = cosine_similarity(jd_embedding, resume_embeddings)[0]
            df['match_score'] = scores

            top_ranked = df.sort_values(by='match_score', ascending=False).head(num_results)

            st.success(f"Top {num_results} Matches Found!")
            for i, row in top_ranked.iterrows():
                with st.expander(f"Rank {i+1}: Match Score {round(row['match_score']*100, 2)}%"):
                    st.write(f"**Skills:** {row['skills']}")
                    st.write(f"**Education:** {row['major_field_of_studies']}")
                    st.write(f"**Justification:** High semantic overlap with the job requirements.")
    else:
        st.warning("Please enter a Job Description first!")