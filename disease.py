from Bio import Entrez
from xml.etree import ElementTree as ET


Entrez.email = "heatherho@gmail.com"   # <-- change this

def get_clinical_significance(rs_id: str):
    # Strip "rs" prefix if present
    rs_numeric = rs_id[2:] if rs_id.lower().startswith("rs") else rs_id

    # Fetch SNP record in XML
    handle = Entrez.efetch(db="snp", id=rs_numeric, rettype="xml", retmode="text")
    xml_data = handle.read()
    handle.close()

    # Parse XML
    root = ET.fromstring(xml_data)

    # Find all CLINICAL_SIGNIFICANCE tags
    diseases = [el.text for el in root.findall(".//CLINICAL_SIGNIFICANCE") if el.text]

    # Print results
    if diseases:
        print(f"{rs_id} clinical significance:")
        for d in set(diseases):
            print(" -", d)
    else:
        print(f"No clinical significance data found for {rs_id}.")

# Example usage
print(get_clinical_significance("rs6311"))

