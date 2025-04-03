from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autoriser les appels depuis UiPath

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        sentiment = "positif"
    elif polarity < -0.2:
        sentiment = "négatif"
    else:
        sentiment = "neutre"

    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
