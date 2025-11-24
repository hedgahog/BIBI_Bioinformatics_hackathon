import streamlit as st
import requests

from gemini_function import get_summary



def run_streamlit():
    # SNP: Single Nucleotide Polymorphism
    # create title
    st.title("SNP summary")

    st.text(body = "Get a summary of a SNP given its rs id")

    # create rs id input

    rs_input = st.text_input(label = "Enter rs number", placeholder = "6311")

    output = None  # initialize summary to 'None'

    # display summary
    if rs_input.isalpha():
        output = "Put in numbers only"
    else:
        with st.spinner('Fetching SNP summary... Gemini is processing a response...'):
            output = get_summary(rs_input)

    # create submit button
    if st.button("Enter", type="primary"):
        if output:
            st.markdown(output, unsafe_allow_html=True)  # create markdown for summary
        else:
            st.error("Invalid input: Does your id exist?")
