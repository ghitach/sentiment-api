from flask import Flask, request, jsonify
from textblob import TextBlob
import nltk
import os

nltk.download('punkt')

app = Flask(__name__)

@app.route("/", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    commentaire = data.get("commentaire", "")

    try:
        # Traduction automatique vers l’anglais
        commentaire_en = str(TextBlob(commentaire).translate(to="en"))
    except Exception as e:
        commentaire_en = commentaire  # fallback

    blob = TextBlob(commentaire_en)
    polarity = blob.sentiment.polarity

    # Classification simple
    if polarity < -0.1:
        sentiment = "négatif"
    elif polarity <= 0.1:
        sentiment = "neutre"
    else:
        sentiment = "positif"

    return jsonify({"sentiment": sentiment})

# Port dynamique pour Render
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
