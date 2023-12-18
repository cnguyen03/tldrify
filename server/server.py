from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)
# use next.js frontend to fetch flask backend route and grab data sent,
# displaying it on frontend

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "This is Calvin's messaage!",
        'people': ['Calvin', 'Iris']
    })


if __name__ == "__main__":
    app.run(debug=True, port=8080)