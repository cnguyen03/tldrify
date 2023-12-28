from flask import Flask, request, jsonify
from flask_cors import CORS
import requests 
from bs4 import BeautifulSoup

from nltk.tokenize import word_tokenize

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# app instance
app = Flask(__name__)
CORS(app)
# use next.js frontend to fetch flask backend route and grab data sent,
# displaying it on frontend

# OpenAI
# my_key = open("API_KEY.txt", "r").read()
# client = OpenAI(api_key=my_key)

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
    # Additional processing of message
    # sentences, words = process_text(text)
    # Get summary
    summary = summarize(text, 0.05)

    # Send message to OpenAI API
    # completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #         {"role": "user", "content": f"Please give me a TLDR of the following text: {message}"}
    #     ]
    # )
    # content = completion.choices[0].message.content

    # Code to send a response to the front end
    response = {"message": summary}
    return jsonify(response)
def parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # parse the text and add it to message
        all_text = soup.get_text()
        # tokenize text to words
        words = word_tokenize(all_text)
        message = ' '.join(words)
        return message
    else: 
        return "Invalid URL"

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary


if __name__ == "__main__":
    app.run(debug=True, port=8080)