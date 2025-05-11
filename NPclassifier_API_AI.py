import requests
import pandas as pd
import csv

# Open the CSV file in write mode with UTF-8 encoding
with open('smile_NP_Result.csv', 'w', newline='', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    # Write the header row
    csvwriter.writerow(['smile', 'class_result', 'superclass_results', 'pathway_results', 'isglycoside'])
    
    # Read the SMILES from the input CSV file
    df2 = pd.read_csv("smile_NP.csv")
    smiles = df2['smile']
    
    # Iterate over each SMILES string
    for smile in smiles:
        class_result = None
        superclass_results = None
        pathway_results = None
        isglycoside = None
        
        try:
            # Construct the URL with the SMILES string
            url = "https://npclassifier.gnps2.org/classify?smiles=" + smile
            # Send a GET request to the URL
            response = requests.get(url)
            # Parse JSON response
            jsondata = response.json()
            
            # Check if keys exist in the JSON response
            if 'class_results' in jsondata:
                class_result = jsondata['class_results']
            if 'superclass_results' in jsondata:
                superclass_results = jsondata['superclass_results']
            if 'pathway_results' in jsondata:
                pathway_results = jsondata['pathway_results']
            if 'isglycoside' in jsondata:
                isglycoside = jsondata['isglycoside']
        except Exception as e:
            print(f"Error processing {smile}: {e}")
        
        # Write the results to the CSV file
        csvwriter.writerow([smile, class_result, superclass_results, pathway_results, isglycoside])
