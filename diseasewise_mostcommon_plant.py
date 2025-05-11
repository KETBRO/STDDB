""" import pandas as pd

# Read the Excel file
df = pd.read_excel("disease_wise.xlsx")

# Convert the DataFrame to a list of lists
data = df.values.tolist()

# Flatten the list of lists
all_plants = [plant for sublist in data for plant in sublist]

# Count occurrences of each plant
plant_counts = pd.Series(all_plants).value_counts()

# Filter plants common for all diseases
common_plants = plant_counts[plant_counts == len(df.columns)]

print("Plants common for all diseases:")
print(common_plants.index.tolist())
 """

import pandas as pd


df = pd.read_excel("disease_wise.xlsx")

# Convert the DataFrame to a list of lists
data = df.values.tolist()

# Flatten the list of lists and remove empty values
all_plants = [plant for sublist in data for plant in sublist if plant]

# Count occurrences of each plant
plant_counts = pd.Series(all_plants).value_counts()

# Filter plants common for at least 4 diseases
common_plants = plant_counts[plant_counts >= 5]

print("Plants common for at least 4 diseases:")
print(common_plants.index.tolist())
