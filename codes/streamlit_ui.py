import streamlit as st
import requests

from api import get_summary

# SNP: Single Nucleotide Polymorphism
# create title
st.title("SNP summary")

# create rs id input
rs_input = st.text_input("SNP rs id", "Enter rs number")

# display summary
try:
    summary = get_summary(rs_input)
except requests.exceptions.JSONDecodeError:
    st.error("Requests JSONDecodeError")
except Exception as e:
    st.error(f"An exception occurred: {e}")

# create submit button
if st.button("Submit", type="primary"):
    st.markdown(summary, unsafe_allow_html=True)  # create markdown for summary
