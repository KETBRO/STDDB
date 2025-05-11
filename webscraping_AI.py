from bs4 import BeautifulSoup
import requests

url = "https://tropicos.org/name/2717274"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad requests
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('li', class_='ng-star-inserted')

    for item in items:
        label_element = item.find('label')
        if label_element:
            label = label_element.text
            value = item.text.replace(label, '').strip()
            print(f"{label}: {value}")

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"An unexpected error occurred: {err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
