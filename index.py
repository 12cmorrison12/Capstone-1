from flask import Flask, render_template
import requests

app = Flask(__name__)

# D&D 5e API endpoint for items
API_ENDPOINT = "https://www.dnd5eapi.co/api/equipment/"

def get_random_item():
    # Get a random item from the D&D 5e API
    response = requests.get(API_ENDPOINT)
    data = response.json()
    return data

@app.route("/")
def index():
    # Render the home page
    return render_template("index.html")

@app.route("/random_item")
def random_item():
    # Get a random item and render the template with item details
    item = get_random_item()
    return render_template("random_item.html", item=item)

if __name__ == "__main__":
    app.run(debug=True)
