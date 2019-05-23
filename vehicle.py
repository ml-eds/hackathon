import changes
import requests
import bytes_to_dict
import dict_to_bytes
api_token = '6fec5bff-a4be-4912-b67d-2f60c08d1893'
api_url_base = 'http://ego-vehicle-api.azurewebsites.net/api/v1/vehicle/signals'

headers = {'Content-Type': 'application/json',
           'X-Api-Key': api_token}


response = requests.get(api_url_base, headers=headers)
print(response.status_code)
# Headers is a dictionary
print("response header", response.headers, "\n")
print(response.content)
content = response.content
#stri = content.decode()
#dicti = json.loads(stri)
dicti = bytes_to_dict.btod(content)
print(dicti)
print("\n")

dicti = changes.change_value(dicti, "turn_signal_left", "on")
payload = dict_to_bytes.dtob(dicti)
#print(type(payload))
requests.patch(api_url_base, {'ListOfVehicleSignalsToUpdate': {"turn_signal_left": "on"}})

res = requests.get(api_url_base, headers=headers)
print(res.status_code)
print("res", res.content)