import sys
import os
import json
import requests

# Path where you want the project to be created
path = "D:/Dev"

print(path)

def create():
    folderName = str(sys.argv[1])

    os.makedirs(path + folderName)
    # Call GitHub Create Repo API
    github_create(folderName)

    print(folderName)

def github_create(folderName):
    # Get your Github API Token from https://github.com/settings/tokens
    api_token = keys.api_token_main #enter your api token
    user = keys.user_main #enter your github_username


    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'token ' + api_token
            }
    data = {
            "name": folderName,
            "description": "Initializing the project.",
            "homepage": "https://user_name.github.io/"+folderName,
            "private": 'true',
            "auto_init": 'true'
            }

    data_json = json.dumps(data)

    response = requests.post('https://api.github.com/' + 'user/repos', auth=(user,api_token), data=data_json)
    print(response)
    print('Project has been initialized and a new repository created '+folderName)
    #print(response.text)

    # Parse a JSON string
    json_response = json.loads(response.text)

    # Command to clone the repo
    print('git clone '+json_response['clone_url'])

if _name_ == "_main_":
    create()