import requests


def get_info_from_ncbi(rs):
    # request json data
    return requests.get(f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs}",
                        timeout=30).json()  # return apis dictionary




if __name__ == "__main__":
    result = get_info_from_ncbi("6311")
    print(result)