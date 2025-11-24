from easy_entrez import EntrezAPI
from xml.etree import ElementTree as ET

entrez_api = EntrezAPI(
    'your-tool-name',
    'e@mail.com',
    # optional
    return_type='json'
)


def get_entrez_result(rs):
    result = entrez_api.fetch([rs], max_results=1, database='snp').data[0]
    return result


if __name__ == "__main__":
    xml_string = ET.tostring(get_entrez_result("6311"), encoding='unicode')
    print(xml_string)
