import requests

# URL of the API with the API key
api_url = "https://api.covidactnow.org/v2/states.json?apiKey=254b42b4fac144718664aca60b349b51"

# Send a GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Print the data for now
    print(data)
else:
    print("Failed to fetch data from the API. Status code:", response.status_code)
