import pandas as pd

# Read the Excel file
df = pd.read_excel('phytochemical_physicochemical_properties.xlsx')

# Group the data by the 'family' column and count the number of plants in each family
family_counts = df.groupby('logd').size().reset_index(name='Phytochemical')

# Save the results to an Excel file
family_counts.to_excel('logd_not_for_range_counts.xlsx', index=False)