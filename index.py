from flask import Flask, request, render_template


app = Flask(__name__)

url = "https://www.dnd5eapi.co/api/magic-items/:index"


payload = {}
headers = {
  'Accept': 'application/json'
}


response = request.request("GET", url, headers=headers, data=payload)


print(response.text)

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

# function to get random item (magic) from api, dropdown menu on front end
@app.route('/items', methods=["GET", "POST"])
def items(indexNum):
    return 

# function to get item rarity from dropdown

# retrieve all data from the API and pick a random index num and return item with name, desc, rarity, url?