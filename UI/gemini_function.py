# pip install requests google-genai
import json, requests
from google import genai




def json_to_dict(rs):
    #rs_num = rs[2:] if rs.lower().startswith("rs") else rs
    # request json data
    return requests.get(f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs}", timeout=30).json() # return python dictionary
    #return json.dumps(python_dic, ensure_ascii=True)




def SNP_to_genai(python_dic):
    client = genai.Client(api_key="AIzaSyCsjSHz0nMJmHuY45k5jizjpb1-0BwJv48")
    system_rules = (
      "Use ONLY the provided python dictionary text below. "
      "If a fact isn't present, reply 'Not in data'. "
      "Do NOT return compact python dictionary. Return an easy to read summary for novices"
    )

    prompt = (
      "Summarize this SNP from the python dictionary: rs, gene name, chromosome, GRCh38 position, "
      "alleles, clinical significance, and Diseases."
      "Format it in an pretty way for a novice to read"
    )



    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        config={"temperature": 0, "system_instruction": system_rules},
        contents=[{
            "role": "user",
            "parts": [
                {"text": prompt},
                {"text": str(python_dic)}
            ],
        }],
    )

    return(resp.text)
    # to do: turn into a functionso I can call it?

rs = "6311" # user input
if __name__ == "__main__":
    print(SNP_to_genai(json_to_dict(rs)))



