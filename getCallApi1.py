
import json # import json library
import requests # import requests library
url = 'https://api.dictionaryapi.dev/api/v2/entries/en/qa'
response = requests.get(url)
if(response.status_code ==200):
    print("Api returns 200") # 200 status code should be generated
assert response.status_code ==200 , "Api return invalid code"
# assert if the response code is not 200
resp_json = response.json()
if(resp_json[0]['word']=="QA"):
    print('word = '+'"QA"')
    # assert the "word should be equal to QA"
if(type(resp_json[0]['phonetics'])==list):
    print("Phonetics is an array of objects")
    # assert Phonetics is an array of objects
if(resp_json[0]['meanings'][0]['partOfSpeech']=="abbreviation"):
    print('meaning.partOfSpeech = '+'"abbreviation"')
   # assert meaning.partOfSpeech = "abbreviation"
if (resp_json[0]['meanings'][0]['definitions'][0]['definition'] == 'quality assurance.'):
    print("meaning.abbreviation.definition = " +"'quality assurance'")
    # assert meaning.abbreviation.definition = 'quality assurance'
