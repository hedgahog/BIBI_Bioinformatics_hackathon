import streamlit as st
import requests

from gemini_function import get_summary

# SNP: Single Nucleotide Polymorphism
# create title
st.title("SNP summary")

# create rs id input

rs_input = st.text_input("SNP rs id", "Enter rs number")

output = None  # initialize summary to 'None'

# display summary
if rs_input.isalpha():
    output = "Put in numbers only"
else:
    output = get_summary(rs_input)

# create submit button
if st.button("Enter", type="primary"):
    if output:
        st.markdown(output, unsafe_allow_html=True)  # create markdown for summary
    else:
        st.error("Invalid input: Does your id exist?")
