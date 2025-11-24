# pip install requests google-genai
import json, requests
from google import genai

def get_summary(rs_input):
    return SNP_to_genai(json_to_dict(rs_input), get_html(rs_input))

def get_html(rs):
    # rs_num = rs[2:] if rs.lower().startswith("rs") else rs
    # request json data
    r = requests.get(f"https://useast.ensembl.org/Homo_sapiens/Variation/Phenotype?v=rs{rs}", timeout=30)
    params = {"phenotypes": 1}  # include disease/phenotype data
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    # r = requests.get(url, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    return r.text


def json_to_dict(rs):
    # rs_num = rs[2:] if rs.lower().startswith("rs") else rs
    # request json data
    return requests.get(f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs}",
                        timeout=30).json()  # return apis dictionary
    # return json.dumps(python_dic, ensure_ascii=True)


def SNP_to_genai(python_dic, html):
    client = genai.Client(api_key="")
    system_rules = (
        "Use ONLY the provided apis dictionary and html text below. "
        "You can combine both texts to provide a comprehensive summary"
        "If a fact isn't present, reply 'Not in data'. "
        "Do NOT return compact apis dictionary and html. Return an easy to read summary for novices"
    )

    prompt = (
        "Summarize this SNP from the apis dictionary: rs, gene name, chromosome, GRCh38 position, "
        "alleles, clinical significance, and Diseases."
        "Format it in an pretty way for a novice to read"
        "Tell user which data type(html versus apis dict) each piece of information is from"
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


rs = "2068824"  # user input
'''if __name__ == "__main__":
    print(SNP_to_genai(json_to_dict(rs)))'''
# Commented out because it was called everytime
#print(SNP_to_genai(json_to_dict(rs), get_html(rs)))
