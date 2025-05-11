import requests
import pandas as pd
import csv
f=open('smile_NP_Result.csv', 'w', newline='') 
csvwriter = csv.writer(f)
csvwriter.writerow(['smile','class_result','superclass_results','pathway_results','isglycoside'])
df2=pd.read_csv("smile_NP.csv")
simles=df2['smile']

for smile in simles:
    class_result=None
    superclass_results=None
    pathway_results=None
    isglycoside=None
    # URL of the website
    try:
        url = "https://npclassifier.gnps2.org/classify?smiles="+smile
        response = requests.get(url)
        jsondata=response.json()
        print(jsondata)
        class_result=jsondata['class_results']
        superclass_results=jsondata['superclass_results']
        pathway_results=jsondata['pathway_results']
        isglycoside =jsondata['isglycoside']
        print(jsondata)
    except:
        pass
    # Send a GET request to the URL
    csvwriter.writerow([smile,class_result,superclass_results,pathway_results,isglycoside])
f.close()