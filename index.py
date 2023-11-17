# function to get item type (magic/non-magical) from api, dropdown menu on front end

# function to get item rarity from dropdown

# retrieve all data from the API and pick a random index num and return item with name, desc, rarity, url?

from flask import Flask
from flask import requests

app = Flask(__name__)

url = "https://www.dnd5eapi.co/api/magic-items/:index"


payload = {}
headers = {
  'Accept': 'application/json'
}


response = requests.request("GET", url, headers=headers, data=payload)


print(response.text)
