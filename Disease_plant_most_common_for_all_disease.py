import pandas as pd

# Read the Excel file
df = pd.read_excel("Disease_plant_most_common_for_all_disease_python_input.xlsx")

# Group by Plant and count occurrences
plant_counts = df['Plant'].value_counts()

# Filter plants common for all diseases
common_plants = plant_counts[plant_counts == len(df['Disease'].unique())]

print("Plants common for all diseases:")
print(common_plants.index.tolist())
