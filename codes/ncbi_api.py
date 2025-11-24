import requests


def request_ncbi_rs(rs):
    # rs_num = rs[2:] if rs.lower().startswith("rs") else rs
    # request json data
    return requests.get(f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs}",
                        timeout=30).json()  # return apis dictionary
    # return json.dumps(python_dic, ensure_ascii=True)
