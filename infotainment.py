# this module is used to display the gamification score on the infotainment screen
import requests
from PIL import Image
import numpy as np
api_token = '6fec5bff-a4be-4912-b67d-2f60c08d1893'
api_url_base = 'http://ego-vehicle-api.azurewebsites.net/api/v1/vehicle/infotainment/text?x=300&y=300&size=64&black=1'
api_image = 'http://ego-vehicle-api.azurewebsites.net/api/v1/vehicle/infotainment'
headers = {'X-Api-Key': api_token}
header = {'X-Api-Key': api_token, 'content-type': 'image/jpeg'}


jpgfile = open('white_png_1514619.jpg', 'rb').read()


def set_api(str):
    r = requests.put(api_url_base, data=str, headers=headers)

def set_image():
    r3 = requests.delete(api_image, headers=headers)
    r2 = requests.put(api_image, data=jpgfile, headers=header)
    print(r2.status_code)

