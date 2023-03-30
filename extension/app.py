from flask import Flask, request
import numpy as np
import joblib
from extractor import main

app = Flask(__name__)
MODEL_PATH = "RandomForestClassifier.pkl"

@app.route("/")
def index():
    return "Welcome to the phishing website detection API!"

@app.route("/detect", methods=["POST"])
def detect_phishing_website():
    url = request.json["url"]
    html = request.json["html"]
    print(url, html)
    features = main(url, html)
    features = np.array(features).reshape((1, -1))
    print(features)
    model = joblib.load(MODEL_PATH)
    prediction = int(model.predict(features)[0])
    print(prediction)
    return {"prediction": prediction}

if __name__ == "__main__":
    app.run(debug=True)
