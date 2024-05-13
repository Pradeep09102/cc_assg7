import requests
api_url = 'https://api.covidactnow.org/v2/states.json?apiKey=254b42b4fac144718664aca60b349b51'
response = requests.get(api_url)
data = response.json()
print(data)