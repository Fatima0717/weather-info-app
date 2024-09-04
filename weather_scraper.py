import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get('https://wttr.in?format=%C+%t')

# Check if request is successful
if response.status_code == 200:
    print(f"Weather Information: {response.text.strip()}")
else:
    print("Failed to retrieve data.")
