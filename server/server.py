from flask import Flask, request, jsonify
from flask_cors import CORS
import requests 
from bs4 import BeautifulSoup
# app instance
app = Flask(__name__)
CORS(app)
# use next.js frontend to fetch flask backend route and grab data sent,
# displaying it on frontend

# /api/home
@app.route("/api/home", methods=['GET', 'POST'])
def handle_request():
    # Code to process data sent from the front end
    message = ""
    data = request.get_json()
    link = data.get("link")
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title
        message = "Summary for " + title.text
    # Code to send a response to the front end
    response = {"message": message}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=8080)