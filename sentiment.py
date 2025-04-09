from flask import Flask, request, jsonify
from textblob import TextBlob
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def analyze():
    data = request.get_json()
    commentaire = data.get("commentaire", "")
    sentiment = TextBlob(commentaire).sentiment.polarity

    if sentiment > 0.1:
        label = "positif"
    elif sentiment < -0.1:
        label = "négatif"
    else:
        label = "neutre"

    return jsonify({"sentiment": label})

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
