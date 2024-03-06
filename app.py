from flask import Flask, jsonify, render_template, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
import requests

app = Flask(__name__)
app.secret_key = "AIzaSyDpTkljTjVCmddpR1AL7hFktdGJ5YGA_x8"
oauth = OAuth(app)

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
    
@app.route('/')
def index():
    return 'Welcome to Flask OAuth Google Login! <a href="/google/">Login with Google</a>'

@app.route('/google/')
def google():

    GOOGLE_CLIENT_ID = '14130293736-68kd4k5bmnvddmth3ah9d5q67mkkhb5t.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    print(redirect_uri)
    session['nonce'] = generate_token()
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    print(" Google User ", user)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
