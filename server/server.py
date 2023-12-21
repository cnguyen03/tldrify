from flask import Flask, request, jsonify
from flask_cors import CORS
import requests 
from bs4 import BeautifulSoup
from openai import OpenAI

from nltk.tokenize import word_tokenize

# app instance
app = Flask(__name__)
CORS(app)
# use next.js frontend to fetch flask backend route and grab data sent,
# displaying it on frontend

# OpenAI
my_key = open("API_KEY.txt", "r").read()
client = OpenAI(api_key=my_key)

# Steps to get app running 
# 1. Open new terminal, go to client directory and run source ~/.bashrc
# 2. Run the Next js server
    # npm run dev
# 3. Go to server directory and go into a venv
    # source venv/bin/activate
# 4. Run server.py
    # python3 server.py

# /api/home
@app.route("/api/home", methods=['GET', 'POST'])
def handle_request():
    # Code to process data sent from the front end
    message = ""
    content = ""
    data = request.get_json()
    link = data.get("link")
    # Send an html request to the link
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse the text and add it to message
        all_text = soup.get_text()
        words = word_tokenize(all_text)
        message = ' '.join(words)
        # Additional Processing of Message

        # Send message to OpenAI API
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": f"Please give me a TLDR of the following text: {message}"}
            ]
        )
        content = completion.choices[0].message.content
    else:
        message = f"Failed to retrieve the page. Status code: {response.status_code}"
    # Code to send a response to the front end
    response = {"message": content}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=8080)