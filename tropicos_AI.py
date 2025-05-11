from taxize import classification

# List of plant scientific names
plant_names = ['Quercus robur', 'Iris oratoria', 'Arachis paraguariensis']

# Retrieve taxonomic information
tax_info = classification(plant_names, db='itis')

# Extract the taxonomic information such as class, subclass, order, and phylum
for result in tax_info:
    print(f"Scientific Name: {result['name']}")
    print(f"Class: {result.get('class', 'N/A')}")
    print(f"Subclass: {result.get('subclass', 'N/A')}")
    print(f"Order: {result.get('order', 'N/A')}")
    print(f"Phylum: {result.get('phylum', 'N/A')}")
    print("----------------------------")
