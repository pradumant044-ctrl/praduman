from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "7ac7c6854c361890024d6d4b5f719e08"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.json.get("city")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return jsonify({"error": "City not found"})

    return jsonify({
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)