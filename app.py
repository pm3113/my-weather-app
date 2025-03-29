from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "53f78d66e35449c1ffabc031ad6e2c6f"  # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city").strip()  # Get city input and remove spaces

        if city:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)
            data = response.json()  

            if response.status_code == 200:
                weather_data = data  # Store weather data
            else:
                error_message = f"Error: {data.get('message', 'City not found!')}"  

    return render_template("index.html", weather=weather_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
