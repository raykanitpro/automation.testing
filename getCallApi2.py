# import json library
import json # import json library
import requests # import requests library

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/qaisnotmagic'
# get response from api url
response = requests.get(url)
# test if the status code is invalid
if(response.status_code ==404):
    print("Api returns 404 status code")
assert response.status_code ==404 , "Api return valid code"
# assert Api returns 404 status code
resp_json = response.json()
if(resp_json['title'] =="No Definitions Found"):
    print('Title = ' + '"No Definitions Found"')
#assert Title is = "No Definitions Found"