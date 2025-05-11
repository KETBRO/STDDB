import pandas as pd

# Load the dataset
df = pd.read_csv('input as AI_from_online reducer.csv')

# Display the first few rows of the dataframe
df.head()

# Display a summary of the dataset
print(df.describe(include='all'))
print('\
Missing values in each column:')
print(df.isnull().sum())

# Display unique values count for non-numeric columns
columns = ['Disease', 'Plant', 'Phytochemical name', 'References']
for col in columns:
    print(f'Unique values in {col}:', df[col].nunique())

# Calculate the number of plants for each disease
disease_plant_count = df.groupby('Disease')['Plant'].nunique().reset_index(name='Number of Plants')

# Calculate the maximum number a phytochemical appears for a disease
phyto_disease_max = df.groupby(['Disease', 'Phytochemical name']).size().reset_index(name='Count')
max_phyto_per_disease = phyto_disease_max.groupby('Disease')['Count'].max().reset_index(name='Max Phyto Count for Disease')

# Calculate the maximum number a phytochemical appears in the whole dataset
max_phyto_overall = phyto_disease_max['Count'].max()

# Calculate the number of phytochemicals for a single disease
disease_phyto_count = df.groupby('Disease')['Phytochemical name'].nunique().reset_index(name='Number of Phytochemicals')

# Display the results
print(disease_plant_count)
print(max_phyto_per_disease)
print('Maximum number a phytochemical appears in the whole dataset:', max_phyto_overall)
print(disease_phyto_count)


# Calculate the top 20 phytochemicals that appear the most times in the dataset
phytochemical_counts = df['Phytochemical name'].value_counts().head(20).reset_index()
phytochemical_counts.columns = ['Phytochemical Name', 'Count']

# Calculate the top 20 plants that appear the most times in the dataset
plant_counts = df['Plant'].value_counts().head(20).reset_index()
plant_counts.columns = ['Plant Name', 'Count']

# Display the results
print(phytochemical_counts)
print(plant_counts)

# Prepare data for the top 5 phytochemicals that appear for each disease
phyto_disease = df.groupby(['Disease', 'Phytochemical name']).size().reset_index(name='Count')
top_phyto_per_disease = phyto_disease.sort_values(['Disease', 'Count'], ascending=[True, False]).groupby('Disease').head(5)

# Display the top 5 phytochemicals for each disease
print(top_phyto_per_disease)

# Save the generated tables to Excel
with pd.ExcelWriter('generated_tables.xlsx') as writer:
    disease_plant_count.to_excel(writer, sheet_name='Disease_Plant_Count')
    max_phyto_per_disease.to_excel(writer, sheet_name='Max_Phyto_Per_Disease')
    disease_phyto_count.to_excel(writer, sheet_name='Disease_Phyto_Count')
    phytochemical_counts.to_excel(writer, sheet_name='Top_20_Phytochemicals')
    plant_counts.to_excel(writer, sheet_name='Top_20_Plants')
    top_phyto_per_disease.to_excel(writer, sheet_name='Top_5_Phyto_Per_Disease')

print('All tables have been saved to generated_tables.xlsx')

