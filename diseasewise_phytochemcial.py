import pandas as pd
import os
import shutil

# Load the data from Excel file
df = pd.read_excel('diseasewise.xlsx')

# Group the data by Disease
grouped = df.groupby('Disease')

# Iterate over each group
for disease, group in grouped:
    # Create a folder for the disease if it doesn't exist
    disease_folder = os.path.join('.', disease)
    os.makedirs(disease_folder, exist_ok=True)
    
    # Copy files for each STDDBID
    for stdid in group['STDDBID']:
        source_file = f"{stdid}.sdf"
        if os.path.isfile(source_file):
            shutil.copy(source_file, disease_folder)
        else:
            print(f"File {source_file} not found for {disease}")
