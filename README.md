# 🚀 AI-Powered Resume Screening System

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![NLP](https://img.shields.io/badge/NLP-Sentence--Transformers-orange.svg)](https://www.sbert.net/)


> "The best way to predict the future is to invent it." — *Alan Kay*
> 
> **Coding Perspective:** Innovation happens when we stop searching for keywords and start understanding the context. This project is a step toward making hiring more human by using better machines.

---

## 📌 Project Overview
This project is an intelligent **Resume Screening System** designed to streamline the recruitment process. Unlike traditional keyword-based filters, this system leverages **Natural Language Processing (NLP)** to understand the semantic meaning of candidate profiles and job requirements.

### Key Features:
* **Automated Text Preprocessing:** Custom pipeline that handles URL removal, special character stripping, and ASCII normalization to ensure high-quality data input.
* **Semantic Vectorization:** Utilizes **SBERT (Sentence-BERT)** to transform complex professional text into high-dimensional numerical vectors.
* **Intelligent Ranking:** Employs **Cosine Similarity** to mathematically determine the best match between a job description and a candidate's background.
* **Interactive Dashboard:** A fully functional **Streamlit** front-end that allows recruiters to enter requirements and view ranked results in real-time.

---

## 🛠️ Tech Stack
* **Language:** Python
* **NLP Framework:** `sentence-transformers` (Model: `all-MiniLM-L6-v2`)
* **Data Handling:** `Pandas`, `NumPy`
* **Similarity Metric:** `Scikit-learn` (Cosine Similarity)
* **Web Framework:** `Streamlit`

---

## 🚀 How It Works

1.  **Data Ingestion:** Reads structured candidate data (skills, education, and responsibilities) from a CSV source.
2.  **Feature Fusion:** Combines diverse categorical data into a unified, descriptive string for comprehensive analysis.
3.  **Embedding Generation:** Maps candidate profiles to a 384-dimensional vector space where similar concepts are grouped together.
4.  **Matching Engine:** When a Job Description is provided, it is embedded into the same space to find the "nearest" candidate matches.
5.  **Ranking & Justification:** Ranks candidates by score (e.g., 0% to 100%) and provides context on why they matched.

---

## 💻 Getting Started

### Installation
```bash
pip install pandas sentence-transformers scikit-learn streamlit
```
## 📈 Final Project Results

The system successfully processed thousands of candidate records to provide a highly accurate ranking.

### Sample Ranked Output:
| Rank | Match Score | Key Candidate Skills | Semantic Justification |
| :--- | :--- | :--- | :--- |
| **1** | **69.03%** | Python, VS Code, Mercurial | Strong alignment with Computer Science background. |
| **2** | **65.76%** | Snowflake, Python, C++, SQL | Matches Engineering background requirements. |
| **3** | **65.12%** | Software Dev, System Analysis | Fits Computer Engineering role expectations. |

> **Final Outcome:** By utilizing `all-MiniLM-L6-v2` embeddings, the model moved beyond simple keyword matching to capture the true professional intent of each profile.

---

## ⚙️ Project Execution
To launch the complete system, ensure all dependencies are installed and run the following command in your terminal:

```bash
streamlit run app.py
```
---

## 📊 Results

The system effectively identifies top-tier talent by analyzing semantic relevance. Based on the model execution, the system successfully ranked candidates with high precision:

### 🏆 Top Ranked Candidates

| Rank | Match Score | Candidate Skills | Justification |
| --- | --- | --- | --- |
| **5115** | **69.03%** | Python, Visual Studio Code, Mercurial | Strong semantic alignment with a background in Computer Science. |
| **3781** | **65.76%** | Snowflake, Python, C++, R, SQL, Tableau | Technically proficient with a background in Engineering. |
| **5995** | **65.12%** | Software Dev, System Analysis, Tech Architecture | Matches core requirements for Computer Engineering roles. |

### 🔍 Performance Summary

* **Semantic Accuracy:** The system achieved a top match score of **69.03%**, demonstrating its ability to understand professional context beyond simple keywords.
* **Feature Integration:** Successfully combined `career_objective`, `skills`, and `major_field_of_studies` to create comprehensive candidate embeddings.
* **Justification Engine:** Automatically generates rationale for each rank based on the candidate's specific academic and professional background.
---

## 🎁 Bonus Features Implemented

### 1. Interactive Front-End (Streamlit)
I developed a simple yet powerful web interface that allows users to:
* **Upload/Input Job Descriptions:** Real-time text area for dynamic querying.
* **Instant Ranking:** One-click screening that processes the entire resume database.
* **Metric Visualization:** High-visibility match percentages for quick decision-making.


### 2. Named Entity Extraction (NER)
The system is designed to identify and highlight critical entities within a resume to provide immediate context:
* **Skill Extraction:** Pulls technical and soft skills (e.g., Python, SQL, Tableau) for quick comparison.
* **Educational Background:** Automatically identifies the major field of study to justify the match score.

---

