import json
import requests

api_token = '6fec5bff-a4be-4912-b67d-2f60c08d1893'
api_url_base = 'http://ego-vehicle-api.azurewebsites.net/api/v1'

headers = {'Content-Type': 'application/json',
           'X-Api-Key': api_token}


response = requests.get(api_url_base, headers=headers)
print(response.status_code)
# Headers is a dictionary
print(response.headers)
# Get the content-type from the dictionary.
#print(response.headers["content-type"])

