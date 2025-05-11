import pandas as pd
import requests
import os

# Function to download 2D image for a given CID
def download_image(cid, compound_name):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/PNG"
    response = requests.get(url)
    if response.status_code == 200:
        # Create a directory to store images if it doesn't exist
        os.makedirs("compound_images", exist_ok=True)
        # Save the image with compound name as filename
        with open(f"compound_images/{compound_name}.png", "wb") as f:
            f.write(response.content)
            print(f"Image downloaded for {compound_name}")
    else:
        print(f"Failed to download image for {compound_name}")

# Read the Excel file
df = pd.read_excel('Restcompound.xlsx')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    cid = row['CID']
    compound_name = row['Compound_Name']
    download_image(cid, compound_name)
