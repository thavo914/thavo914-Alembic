import requests
import json
from datetime import date
url = f'https://api.nasa.gov/planetary/apod?api_key=XfTPMvNOEBfSbdy3kCJxbC3tdZ5QSBtdc6hSGmQf'
response = requests.get(url).json()
print(response)
today_image = response['hdurl']
r = requests.get(today_image)
with open(f'todays_image_{date.today()}.png', 'wb') as f:
 f.write(requests.get(today_image).content)