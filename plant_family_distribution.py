import pandas as pd

# Read the Excel file
df = pd.read_excel('Plant_family_AI data_analysis.xlsx')

# Group the data by the 'family' column and count the number of plants in each family
family_counts = df.groupby('family').size().reset_index(name='Number_of_Plants')

# Save the results to an Excel file
family_counts.to_excel('family_counts.xlsx', index=False)
