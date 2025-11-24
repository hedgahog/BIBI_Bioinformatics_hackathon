from easy_entrez import EntrezAPI
from easy_entrez.parsing import xml_to_string, namespaces
from easy_entrez.parsing import parse_dbsnp_variants
from pandas import DataFrame

entrez_api = EntrezAPI(
    'your-tool-name',
    'e@mail.com',
    # optional
    return_type='json'
)


def get_entrez_result(rs):
    result = entrez_api.fetch([rs], max_results=1, database='snp').data[0]
    return result
