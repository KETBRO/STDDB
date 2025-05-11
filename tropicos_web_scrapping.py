import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "https://tropicos.org/name/2717274"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the ul element with the specified class
    ul_element = soup.find('ul', class_='ng-star-inserted')

    # Extract data from each li element within the ul
    data_dict = {}
    for li in ul_element.find_all('li', class_='ng-star-inserted'):
        label = li.find('label').text.strip(':')
        value = li.find('a').text.strip()
        data_dict[label] = [value]

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(data_dict)

    # Save the DataFrame to an Excel file
    df.to_excel('output.xlsx', index=False)

    print("Data successfully scraped and saved to 'output.xlsx'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
