import requests

# TODO: interface has phenotype by html doesn't

rs = "6311"  # user input


def get_html(rs):
    # request json data
    r = requests.get(f"https://useast.ensembl.org/Homo_sapiens/Variation/Phenotype?v=rs{rs}", timeout=30)
    params = {"phenotypes": 1}  # include disease/phenotype data
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    # r = requests.get(url, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    return r.text

def get_phenotype(rs):
    r = requests.get(f"https://useast.ensembl.org/Homo_sapiens/Variation/Phenotype?v=rs{rs}", timeout=30)
    return r.text

def get_rs():
    # rsID 변이에 대한 phenotype 정보를 가져오려면 variation endpoint를 먼저 사용
    r = requests.get("https://rest.ensembl.org/variation/homo_sapiens/rs6311?content-type=application/json",
                 headers={"Content-Type": "application/json"})
    print(r.json())

if __name__ == "__main__":
    get_rs()
