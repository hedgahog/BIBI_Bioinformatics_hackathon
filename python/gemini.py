# pip install requests google-genai
import get_ensembl, requests
from google import genai

client = genai.Client(api_key = "")

rs = "rs6311" # user input
rs_num = rs[2:] if rs.lower().startswith("rs") else rs
# request json data and parsing into a Python dictionary
data = requests.get(f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs_num}", timeout=30).json()

system_rules = (
  "Use ONLY the provided JSON text below. "
  "If a fact isn't present, reply 'Not in JSON'. "
  "Do NOT return compact JSON. Return an easy to read summary for novices"

)

prompt = (
  "Summarize this SNP from the JSON text: rs, gene name, chromosome, GRCh38 position, "
  "alleles, clinical significance, and Diseases."
  "Format it in an pretty way for a novice to read"
)

json_str = json.dumps(data, ensure_ascii=False) # converting to json

resp = client.models.generate_content(
    model="gemini-2.0-flash-001",
    config={"temperature": 0, "system_instruction": system_rules},
    contents=[{
        "role": "user",
        "parts": [
            {"text": prompt},
            {"text": "----- BEGIN JSON -----\n" + json_str + "\n----- END JSON -----"}
        ],
    }],
)

print(resp.text)
# to do: turn into a function so I can call it?


