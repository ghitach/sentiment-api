from flask import Flask, request, jsonify
from textblob import TextBlob
import nltk
import os

# Télécharger les ressources nécessaires à TextBlob
nltk.download('punkt')

app = Flask(__name__)

@app.route("/", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    commentaire = data.get("commentaire", "")

    try:
        # Traduire en anglais pour une meilleure analyse
        commentaire_en = str(TextBlob(commentaire).translate(to="en"))
    except:
        # Si la traduction échoue, utiliser le texte brut
        commentaire_en = commentaire

    blob = TextBlob(commentaire_en)
    polarity = blob.sentiment.polarity

    if polarity < -0.1:
        sentiment = "négatif"
    elif polarity <= 0.1:
        sentiment = "neutre"
    else:
        sentiment = "positif"

    return jsonify({"sentiment": sentiment})

# Pour Render : utiliser le port fourni par la variable d'environnement
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
