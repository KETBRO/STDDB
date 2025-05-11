""" import pandas as pd

# Read the Excel file
df = pd.read_excel('Plant_native_to_Ai_data_analysis.xlsx')
print(df.columns)

# Split the 'Geographic_Distribution' column by commas and count the number of plants for each distribution
distribution_counts = df['Geographic_Distribution'].str.split(',').apply(lambda x: len(x)).value_counts()

print("Number of Plants for Each Distribution:")
print(distribution_counts) """

import pandas as pd

# Read the Excel file
df = pd.read_excel('Plant_native_to_Ai_data_analysis.xlsx')

# Split the 'Geographic_Distribution' column by commas and count the number of plants for each distribution
geographic_distribution_counts = df['Geographic_Distribution'].str.split(',').explode().str.strip().value_counts()

# Create a DataFrame for the results
results_df = pd.DataFrame({'Geographic_Distribution': geographic_distribution_counts.index, 'Number_of_Plants': geographic_distribution_counts.values})

# Save the results to an Excel file
results_df.to_excel('distribution_counts_with_names.xlsx', index=False)

