from flask import Flask, request, jsonify
from flask_cors import CORS
import requests 
from bs4 import BeautifulSoup

from nltk.tokenize import word_tokenize

from transformers import pipeline
# app instance
app = Flask(__name__)
CORS(app)
# use next.js frontend to fetch flask backend route and grab data sent,
# displaying it on frontend

# AI Pipeline
summarizer = pipeline("summarization")

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
    data = request.get_json()
    link = data.get("link")
    # Parse page for text
    text = parse(link) 

    max_chunk = 900
    text = text.replace('.', '.<eos>')
    text = text.replace('?', '?<eos>')
    text = text.replace('!', '!<eos>')

    sentences = text.split('<eos>')
    current_chunk = 0 
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    res = summarizer(chunks, max_length=500, min_length=30, do_sample=False)
    text = ' '.join([summ['summary_text'] for summ in res])

    response = {"message": text}
    return jsonify(response)

def parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # parse the text and add it to message
        paragraphs = soup.find_all(['p', 'h1'])
        all_text = [paragraph.text for paragraph in paragraphs]
        # tokenize text to words
        words = word_tokenize(' '.join(all_text))
        message = ' '.join(words)
        return message
    else: 
        return "Invalid URL"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
