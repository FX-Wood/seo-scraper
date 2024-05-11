import requests
from bs4 import BeautifulSoup

def get_scrape(uri: str):
    response = requests.get(uri)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        meta_tags = soup.find_all('meta')
        return [{ "name": tag.get('name'), "content": tag.get('content'), "property": tag.get('property')} for tag in meta_tags]
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
