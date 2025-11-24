# TODO: I put gemini_function.py into UI folder because I can't figure out how to call it from a different folder
from json import JSONDecodeError
import requests

import streamlit as st
import requests
from gemini_function import get_html, json_to_dict, SNP_to_genai
# SNP: Single Nucleotide Polymorphism
# create title

st.title("SNP summary")

# create rs id input
rs_input = st.text_input("SNP rs id","Enter rs number")

# create summary

try:
    summary = SNP_to_genai(json_to_dict(rs_input),get_html(rs_input))
except requests.exceptions.JSONDecodeError:
    st.error("Requests JSONDecodeError")


# create submit button
if st.button("Submit", type = "primary"):
    st.markdown(summary, unsafe_allow_html=True) # create markdown for summary






