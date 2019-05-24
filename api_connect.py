from postmen import Postmen, PostmenException

api_token = '6fec5bff-a4be-4912-b67d-2f60c08d1893'
region = 'sandbox'
api_url_base = 'http://ego-vehicle-api.azurewebsites.net/api/v1'
api = Postmen(api_token, region)
# headers = {'Content-Type': 'application/json',
#            'X-Api-Key': api_token}
#
#
# response = requests.get(api_url_base, headers=headers)
# print(response.status_code)
# # Headers is a dictionary
# print(response.headers)
# # Get the content-type from the dictionary.
# #print(response.headers["content-type"])

try:
    # as an example we request all the labels

    result = api.get('labels')
    print("RESULT:")
    pp.pprint(result)
except PostmenException as e:
    # if error occurs we can access all
    # the details in following way

    print("ERROR")
    print(e.code())  # error code
    print(e.message())  # error message
    pp.pprint(e.details())  # details