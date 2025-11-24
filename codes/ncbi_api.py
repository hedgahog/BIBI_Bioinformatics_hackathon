import requests


def get_info_from_ncbi(rs):
    # rs_num = rs[2:] if rs.lower().startswith("rs") else rs
    # request json data
    return requests.get(f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs}",
                        timeout=30).json()  # return apis dictionary
    # return json.dumps(python_dic, ensure_ascii=True)

def get_citations(citations):
    return requests.get(f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs}",
                        timeout=30).json()['citations']

if __name__ == "__main__":
    result = get_info_from_ncbi("6311")
    print(result['citations'])