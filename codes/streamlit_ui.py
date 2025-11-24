import streamlit as st
import requests

from gemini_function import get_summary

# SNP: Single Nucleotide Polymorphism
# create title
st.title("SNP summary")

# create rs id input
rs_input = st.text_input("SNP rs id", "Enter rs number")

# display summary
summary = get_summary(rs_input)

# create submit button
if st.button("Submit", type="primary"):
    st.markdown(summary, unsafe_allow_html=True)  # create markdown for summary
