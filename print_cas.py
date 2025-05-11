import pandas as pd
import requests

# Function to retrieve CAS RN for a given CID using PubChem API
def get_cas_rn(cid):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/CAS/TXT"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            cas_rn = response.text.strip()
            if cas_rn:  # Check if CAS RN is not empty
                return cas_rn
            else:
                return "CAS no not found"
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception: {str(e)}"

# Read PubChem CIDs from Excel file
input_file = "pubchem_cids.xlsx"
output_file = "pubchem_cids_with_cas.xlsx"
df = pd.read_excel(input_file)

# Retrieve CAS RN for each CID and print
for index, row in df.iterrows():
    cid = row['CID']
    cas_rn = get_cas_rn(cid)
    print(f"CID: {cid}, CAS RN: {cas_rn}")

# Optional: Write results back to Excel file
df.to_excel(output_file, index=False)
