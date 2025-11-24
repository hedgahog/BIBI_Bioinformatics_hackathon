import streamlit as st

from gemini_function import get_summary

# SNP: Single Nucleotide Polymorphism
# create title
st.title("SNP summary")

st.text(body="Get a summary of a SNP given its rs id")

# create rs id input

rs_input = st.text_input(label="Enter rs number", placeholder="6311")

output = None  # initialize summary to 'None'

# display summary
if rs_input.isalpha():
    output = "Put in numbers only"
elif rs_input == "":
    output = "Input cannot be empty"
else:
    with st.spinner('Fetching SNP summary... Gemini is processing a response...'):
        output = get_summary(rs_input)


def hyperlinks():
    st.markdown("**Shortcut links to external databases**", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(spec=3)

    with col1:
        st.link_button("NCBI", url=f"https://www.ncbi.nlm.nih.gov/snp/?term=rs{rs_input}", icon="🔗",
                       use_container_width=True)
    with col2:
        st.link_button("Ensembl",
                       url=f"https://www.ensembl.org/Homo_sapiens/Variation/Explore?db=core;v=rs{rs_input};vdb=variation",
                       icon="🧬", use_container_width=True)
    with col3:
        st.link_button("ClinVar", url=f"https://www.ncbi.nlm.nih.gov/clinvar/?term={rs_input}", icon="🧫",
                       use_container_width=True)


# create submit button
if st.button("Enter", type="primary"):
    hyperlinks()
    if output:
        st.markdown(output, unsafe_allow_html=True)  # create markdown for summary
    else:
        st.error("Invalid input: Does your id exist?")
