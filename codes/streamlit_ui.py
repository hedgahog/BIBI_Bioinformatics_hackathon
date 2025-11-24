import streamlit as st
import requests

from gemini_function import get_summary

# SNP: Single Nucleotide Polymorphism
# create title
st.title("SNP summary")

# create rs id input

rs_input = st.text_input("SNP rs id", "Enter rs number")

summary = None # initialize summary to 'None'

# display summary
if rs_input.isalpha():
    st.error("Put in numbers only")
try:
    summary = get_summary(rs_input)
except NameError:
    st.error("Invalid input")
except requests.exceptions.JSONDecodeError:
    st.error("Requests JSONDecodeError")
except Exception as e:
    st.error(f"An exception occurred: {e}")

# create submit button
if st.button("Enter", type="primary"):
    if summary:
        st.markdown(summary, unsafe_allow_html=True)  # create markdown for summary
    else:
        st.error("Invalid input: Does your id exist?")
