import requests

api_token = '6fec5bff-a4be-4912-b67d-2f60c08d1893'
api_url_base = 'http://ego-vehicle-api.azurewebsites.net/api/v1/vehicle'

response = requests.get(api_url_base)

print(response.status_code)
# Headers is a dictionary
print(response.headers)
# Get the content-type from the dictionary.
#print(response.headers["content-type"])
startscore = 1000
breaks = 0
acceleration = 0
steering = 0
distance_to_object = 0
distancetravel  = 0
powerconsumption = 0

