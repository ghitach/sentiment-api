from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def analyze():
    data = request.get_json()
    commentaire = data.get('commentaire')
    blob = TextBlob(commentaire)
    polarity = blob.sentiment.polarity

    if polarity < -0.1:
        sentiment = "négatif"
    elif polarity > 0.1:
        sentiment = "positif"
    else:
        sentiment = "neutre"

    return jsonify(sentiment)

