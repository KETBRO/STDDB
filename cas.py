import pandas as pd
import requests

# Function to retrieve CAS RN for a given CID using PubChem API
def get_cas_rn(cid):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/CAS/TXT"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Not found"

# Read PubChem CIDs from Excel file
input_file = "pubchem_cids.xlsx"
output_file = "pubchem_cids_with_cas.xlsx"
df = pd.read_excel(input_file)

# Retrieve CAS RN for each CID
cas_rns = []
for cid in df['CID']:
    cas_rns.append(get_cas_rn(cid))

# Add CAS RNs to the DataFrame
df['CAS_RN'] = cas_rns

# Write results back to Excel file
df.to_excel(output_file, index=False)
