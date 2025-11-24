# BIBI_Bioinformatics_hackathon
Overview:
We built a simple streamlit interface that will accept any rs id. Our Gemini AI agent uses data from NCBI and Ensembl to generate an insightful summary. 
This summary is catered towards bioinformaticians and scientists.


Requirements:
streamlit
python (3.9-3.13 supports streamlit)
Gemini API

Installation:
Install streamlit in conda:
conda install streamlit

Install genai in conda:
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install conda-forge::google-genai

Or install genai as a package in your python editor.

Obtain Gemini API key as an environment variable: https://ai.google.dev/gemini-api/docs/api-key

Run the interface code in your terminal:
streamlit run streamlit_ui.py


