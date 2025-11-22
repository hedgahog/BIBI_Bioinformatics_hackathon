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
'''
# find up to 10 000 results for cancer in human
result = entrez_api.search('cancer AND human[organism]', max_results=10_000)

# data will be populated with JSON or XML (depending on the `return_type` value)
var = result.data
# fetching SNP
rs6311 = entrez_api.fetch(['rs6311'], max_results=1, database='snp').data[0]'''

#display result


# print(xml_to_string(rs6311))

''''# print gene name
namespaces = {'ns0': 'https://www.ncbi.nlm.nih.gov/SNP/docsum'}
genes = [
    name.text
    for name in rs6311.findall('.//ns0:GENE_E/ns0:NAME', namespaces)
]
# print(genes)'''

result = entrez_api.fetch(['rs6311', 'rs662138'], max_results=10, database='snp')

variant_positions = DataFrame([
    {
        'id': 'rs' + document_summary.get('uid'),
        'chromosome': chromosome,
        'position': position
    }
    for document_summary in result.data
    for chrom_and_position in document_summary.findall('.//ns0:CHRPOS', namespaces)
    for chromosome, position in [chrom_and_position.text.split(':')]
])

print(variant_positions)
variants = parse_dbsnp_variants(result)
print(variants.coordinates)
print(variants.alt_frequencies.head(5)) # printing first five

