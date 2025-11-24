import requests

# TODO: interface has phenotype by html doesn't

rs = "6311"  # user input


def get_html(rs):
    # rs_num = rs[2:] if rs.lower().startswith("rs") else rs
    # request json data
    r = requests.get(f"https://useast.ensembl.org/Homo_sapiens/Variation/Phenotype?v=rs{rs}", timeout=30)
    params = {"phenotypes": 1}  # include disease/phenotype data
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    # r = requests.get(url, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    return r.text


print(get_html("6311"))
