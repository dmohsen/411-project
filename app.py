from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/random_recipe')
def random_recipe():
    api_key = "6006ef8d6ad04e199119bdaa6f3809f9"
    url = "https://api.spoonacular.com/recipes/random"
    params = {"apiKey": api_key, "number": 1}

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        recipe = data['recipes'][0]
        # return a JSON with the recipe's title, id, and image
        return jsonify({
            "title": recipe['title'],
            "id": recipe['id'],
            "image": recipe['image']
        })
    else:
        return jsonify({"error": "Failed to fetch recipe"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
