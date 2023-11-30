from flask import Flask, request, render_template
import random


app = Flask(__name__)

API_URL = "https://www.dnd5eapi.co/api/magic-items/:index"


payload = {}
headers = {
  'Accept': 'application/json'
}


response = request.request("GET", API_URL, headers=headers, data=payload)


print(response.text)

# function to get item rarity from dropdown

# retrieve all data from the API and pick a random index num and return item with name, desc, rarity, url?

def get_api_data():
    response = request.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    api_data = get_api_data()

    if api_data:
        # Extract the ids from the API data
        ids = [post['id'] for post in api_data]

        # Generate a random index
        random_index = random.choice(ids)

        # Render the HTML template with the random index
        return render_template('index_with_api.html', random_index=random_index)

    else:
        return "Error fetching data from the API"

if __name__ == '__main__':
    app.run(debug=True)