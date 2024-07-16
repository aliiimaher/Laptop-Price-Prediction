import requests
from bs4 import BeautifulSoup
import random

url = 'https://kavirmotor.com/subCategory/14'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    listings = soup.find_all('div', class_='text-center text-xs hover:font-bold hover:shadow p-2 pb-4 flex h-max items-center justify-center grid grid-cols-2')
    
    # Extract names and models
    data = []
    for listing in listings:
        name_div = listing.find('div', class_='col-span-2 ltr truncate text-sm')
        model_div = listing.find('div', class_='col-span-2 ltr truncate mt-2 text-black/50 font-bold')
        
        if name_div and model_div:
            name = name_div.text.strip()
            model = model_div.text.strip()
            data.append((name, model))
    
    random.shuffle(data)
    
    for name, model in data:
        print(f"Name: {name}, Model: {model}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
