import pandas as pd
import pubchempy as pcp
import re

def get_cas_numbers_from_cids(cids):
    cas_rns = []
    names = []
    for cid in cids:
        try:
            compound = pcp.Compound.from_cid(cid)
            if compound.synonyms:
                for syn in compound.synonyms:
                    match = re.match(r'(\d{2,7}-\d\d-\d)', syn)
                    if match:
                        cas_rns.append(match.group(1))
                        names.append(compound.iupac_name)
        except Exception as e:
            print(f"Error processing CID {cid}: {str(e)}")
    return cas_rns, names

# Read CIDs from Excel file
input_excel_file = "pubchem_cids.xlsx"  # Replace with your input Excel file path
df = pd.read_excel(input_excel_file)

# Fetch CAS numbers and names for each CID and print/save them
cas_numbers_list = []
names_list = []
for cid_row in df['CID']:
    cids = [int(cid_row)]
    cas_numbers, names = get_cas_numbers_from_cids(cids)
    cas_numbers_list.append(cas_numbers)
    names_list.append(names)
    for name in names:
        print(f"Compound name: {name}")

# Add CAS numbers and names to DataFrame
df['CAS Numbers'] = cas_numbers_list
df['Compound Names'] = names_list

# Save the DataFrame to Excel
output_excel_file = "output.xlsx"  # Replace with your output Excel file path
try:
    df.to_excel(output_excel_file, index=False)
    print(f"Data saved to {output_excel_file}")
except Exception as e:
    print(f"Error saving data to Excel: {str(e)}")
