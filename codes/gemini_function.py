# pip install requests google-genai
import requests
import os
from google import genai

from ncbi_api import request_ncbi_rs
from get_ensembl import get_html

api_key = os.environ["GEMINI_API_KEY"]


def get_summary(rs_input) -> str:
    try:
        result = SNP_to_genai(request_ncbi_rs(rs_input), get_html(rs_input))
    except requests.exceptions.JSONDecodeError as e:
        result = f"Requests JSONDecodeError: {e}"
    return result


def SNP_to_genai(python_dic, html):
    client = genai.Client(api_key=api_key)
    system_rules = (
        "Use the provided apis dictionary and html text below first. "
        "You can combine the texts to provide a comprehensive summary"
        "If a fact isn't present, reply 'Not in data'. "
        "Do NOT return compact apis dictionary and html. Return an easy to read summary for bioinformaticians and scientists. "
    )

    prompt = (
        "Summarize this SNP from the apis dictionary: rs, gene name, chromosome, GRCh38 position, "
        "alleles, clinical significance, and Diseases."
        "Format it in an pretty and easy way to read"
    )

    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        config={"temperature": 0, "system_instruction": system_rules},
        contents=[{
            "role": "user",
            "parts": [
                {"text": prompt},
                {"text": str(python_dic) + str(html)},
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
