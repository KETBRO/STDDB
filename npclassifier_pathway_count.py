import pandas as pd
df = pd.read_excel("NP classifier for  AI data analysis.xlsx")
pathway_counts = df['field_super_class'].str.split(', ', expand=True)

# Stack the DataFrame to create a Series with multi-level index
pathway_counts_stacked = pathway_counts.stack()

# Count the occurrences of each pathway
pathway_counts = pathway_counts_stacked.value_counts()

# Save the result to an Excel file
pathway_counts.to_excel("super_class_counts.xlsx", header=False)





