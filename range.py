""" import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('phytochemical_physicochemical_properties.xlsx')

# Define the molecular weight ranges from -10 to 5
start_range = -10
end_range = 5
step = 1

# Generate the ranges dynamically
ranges = [(i, i + step) for i in range(start_range, end_range)]

# Initialize a dictionary to store the counts for each range
count_dict = {f'{start}-{end}': 0 for start, end in ranges}

# Iterate over each row in the DataFrame and count the number of phytochemicals in each range
for weight in df['logd']:
    for start, end in ranges:
        if start <= weight < end:
            count_dict[f'{start}-{end}'] += 1

# Create a DataFrame from the count dictionary
result_df = pd.DataFrame(count_dict.items(), columns=['logd Range', 'Number of Phytochemicals'])

# Save the result to an Excel file
result_df.to_excel('logd.xlsx', index=False) """

import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('phytochemical_physicochemical_properties.xlsx')

# Define the molecular weight ranges from -10 to 5
start_range = -19
end_range = 10
step = 1

# Generate the ranges dynamically
ranges = [(i, i + step) for i in range(start_range, end_range)]

# Initialize a dictionary to store the counts for each range
count_dict = {f'{start}-{end}': 0 for start, end in ranges}

# Iterate over each row in the DataFrame and count the number of phytochemicals in each range
for weight in df['logd']:
    for start, end in ranges:
        if start <= weight < end:  # Exclude the upper bound when checking the range
            count_dict[f'{start}-{end}'] += 1

# Create a DataFrame from the count dictionary
result_df = pd.DataFrame(count_dict.items(), columns=['logd Range', 'Number of Phytochemicals'])

# Save the result to an Excel file
result_df.to_excel('logd_range_counts.xlsx', index=False)


