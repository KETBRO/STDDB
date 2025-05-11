import requests
from bs4 import BeautifulSoup

def get_plant_id(plant_name):
    # URL of the search results page
    search_url = f"https://powo.science.kew.org/results?q={plant_name}"
    
    # Send a GET request to the search results page
    response = requests.get(search_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first search result link
        result_link = soup.find('a', class_='search-result__link')
        
        if result_link:
            # Extract the URL of the first search result
            plant_url = result_link['href']
            
            # Send a GET request to the plant page
            plant_response = requests.get(plant_url)
            
            if plant_response.status_code == 200:
                # Parse the plant page HTML content
                plant_soup = BeautifulSoup(plant_response.text, 'html.parser')
                
                # Find the element containing the plant ID
                id_element = plant_soup.find('div', class_='indent').find('span', class_='badge badge-secondary')
                
                # Extract the plant ID
                if id_element:
                    plant_id = id_element.text.strip()
                    return plant_id
                else:
                    return "Plant ID not found."
            else:
                return "Error: Failed to fetch the plant page."
        else:
            return "Error: Plant link not found."
    else:
        return "Error: Failed to fetch the search results page."

# Search for the ID of "Neolitsea pallens"
plant_name = "Neolitsea+pallens"  # URL encoded name
plant_id = get_plant_id(plant_name)

print(f"The ID of Neolitsea pallens is: {plant_id}")
