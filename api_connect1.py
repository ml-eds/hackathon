#this module assures the connection with the API and supplies get and set functions for the api
import requests
import json
api_token = '6fec5bff-a4be-4912-b67d-2f60c08d1893'
api_url_base = 'http://ego-vehicle-api.azurewebsites.net/api/v1/vehicle/signals'

headers = {'content-type': 'application/json',
            'X-Api-Key': api_token}

#getter for the api
def get_api():
    response = requests.get(api_url_base, headers= headers)
    content = response.json()
    return content

#
#if a value from the extended API keys needs to be changed, the following short snippet by changing key to the desired value
#for key in content:
#    if key == 'key':
#        content['key'] = 'no'


def set_api(content):
    r = requests.patch(api_url_base, data=json.dumps(content), headers=headers)

#res = requests.get(api_url_base, headers=headers)
#print(res.json())