import requests



rs = "6311"  # user input


def get_info_from_ensembl(rs):
    # request json data
    r = requests.get(f"https://useast.ensembl.org/Homo_sapiens/Variation/Phenotype?v=rs{rs}", timeout=30)
    r.raise_for_status()
    return r.text

def get_rs():
    r = requests.get("https://rest.ensembl.org/variation/homo_sapiens/rs6311?content-type=application/json",
                 headers={"Content-Type": "application/json"})
    print(r.json())

if __name__ == "__main__":
    get_rs()
