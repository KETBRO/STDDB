import pandas as pd

# Read the Excel file
df = pd.read_excel("Disease_plant_most_common_for_all_disease_python_input.xlsx")

# Count occurrences of each phytochemical
phytochemical_counts = df['Plant'].value_counts()

# Filter phytochemicals common for all diseases
common_phytochemicals = phytochemical_counts[phytochemical_counts == len(df['Disease'].unique())]

print("Plants common for all diseases:")
print(common_phytochemicals.index.tolist())
