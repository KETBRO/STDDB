import pubchempy as pcp
import csv

# Output file path
output_file = "CID_CASRN_SynXref.csv"  # Modify this path as per your system

# Function to scrape CAS numbers from PubChem
def scrape_cas_number(output_file, compound_name):
    # Fetch compounds information
    compounds = pcp.get_compounds(compound_name, 'name', record_type='3d', as_dataframe=False)

    # Open the output file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['CID', 'CAS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Process each compound
        for compound in compounds:
            # Check if the compound has a CAS number
            if 'cas' in compound:
                writer.writerow({'CID': compound.cid, 'CAS': compound.cas})
            else:
                print(f"No CAS number found for {compound_name}")

# Main function
def main():
    compound_name = 'glucose'  # Change this to the compound name you want to fetch
    scrape_cas_number(output_file, compound_name)

if __name__ == "__main__":
    main()
