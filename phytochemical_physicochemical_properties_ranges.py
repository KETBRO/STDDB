""" import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('phytochemical_physicochemical_properties.xlsx')

# Define the molecular weight ranges
ranges = [(0, 100), (101, 200), (301, 400)]

# Initialize a dictionary to store the counts for each range
count_dict = {f'{start}-{end}': 0 for start, end in ranges}

# Iterate over each row in the DataFrame and count the number of phytochemicals in each range
for weight in df['Molecular Weight']:
    for start, end in ranges:
        if start <= weight <= end:
            count_dict[f'{start}-{end}'] += 1

# Create a DataFrame from the count dictionary
result_df = pd.DataFrame(count_dict.items(), columns=['Molecular Weight Range', 'Number of Phytochemicals'])

# Save the result to an Excel file
result_df.to_excel('molecular_weight.xlsx', index=False) """

import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('phytochemical_physicochemical_properties.xlsx')

# Define the molecular weight ranges
ranges = [(0, 100), (101, 200), (201, 300), (301, 400), (401, 500), (501, 1000), (1001, 2000), (2001, 3000), (3001, 4000), (4001, 5000), (5001, 6500), (6501, 470000000)]

# Initialize a dictionary to store the counts for each range
count_dict = {f'{start}-{end}': 0 for start, end in ranges}

# Iterate over each row in the DataFrame and count the number of phytochemicals in each range
for weight in df['tpsa(Topological polar surface area)']:
    for start, end in ranges:
        if start <= weight <= end:
            count_dict[f'{start}-{end}'] += 1

# Create a DataFrame from the count dictionary
result_df = pd.DataFrame(count_dict.items(), columns=['tpsa Range', 'Number of Phytochemicals'])

# Save the result to an Excel file
result_df.to_excel('tpsa.xlsx', index=False)
