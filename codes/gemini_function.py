# pip install requests google-genai
import requests
import os
from google import genai

from ncbi_api import get_info_from_ncbi
from get_ensembl import get_info_from_ensembl
from entrez import get_entrez_result

api_key = os.environ["GEMINI_API_KEY"]


def get_summary(rs_input) -> str:
    try:
        ncbi_result = get_info_from_ncbi(rs_input)
        ensembl_result = get_info_from_ensembl(rs_input)
        entrez_result = get_entrez_result(rs_input)
        result = SNP_to_genai(ncbi_result, ensembl_result, entrez_result)
    except Exception as e:
        result = f"{e}\n\n **Please check the rs number and try again.**"
    return result


def SNP_to_genai(ncbi_result: dict, ensembl_result: str, entrez_result: str):
    client = genai.Client(api_key=api_key)
    system_rules = (
        "Use the provided dictionary and html text below first. "
        "You can combine the texts to provide a comprehensive summary"
        "If a fact isn't present, reply 'Not in data'. "
        "Do NOT return compact apis dictionary and html. Return an easy to read summary for bioinformaticians and scientists. "
    )

    prompt = (
        "Summarize this SNP from the dictionary: rs, gene name, chromosome, GRCh38 position, "
        "alleles, clinical significance, and Diseases."
        "Format it in an pretty and easy way to read"
        "At the end of the summary, include one line stating the data sources used "
        "(e.g., 'Data sources: NCBI, Ensembl, ClinVar')."
        "If there is list of citations, do deeper research on those researches and include any important findings in the summary, with source"
    )

    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        config={"temperature": 0, "system_instruction": system_rules},
        contents=[{
            "role": "user",
            "parts": [
                {"text": prompt},
                {"text": str(ncbi_result) + str(ensembl_result) + str(entrez_result)},
            ],
        }],
    )
    return (resp.text)


if __name__ == "__main__":
    rs = "2068824"  # user input
    try:
        summary = get_summary(rs)
    except Exception as e:
        print(e)
    print("Running Gemini_function.py")
    print(summary[:200])
    print(f"TYPE: {type(summary)}")
