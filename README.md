
# 🌤 Weather Forecasting Web App using ML + AccuWeather API

This repository showcases a lightweight, district-level weather forecasting system built using Python, Meta’s Prophet time-series model, and real-time weather API validation from AccuWeather.

## 🚀 Features

- Train a model on historical weather data (e.g., temperature)
- Predict future weather (up to 10–15 days)
- Fetch and compare real-time weather forecasts using AccuWeather API
- Simple backend using Python (Flask-ready)
- Visualizations of prediction vs. actual data
- Easily extensible to new regions or longer timelines

---

## 🧠 Tech Stack

- Python
- Pandas, NumPy
- Prophet (Meta) for ML Forecasting
- AccuWeather API (10-day free, extended with paid plans)
- MongoDB (optional for storage)
- Flask (for web backend)
- Plotly/Matplotlib for charts

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-forecast-app.git
cd weather-forecast-app
```

### 2. Install dependencies

```bash
pip install pandas prophet requests flask matplotlib
```

> 📝 Prophet may require `pystan`. If issues occur, try:
```bash
pip install pystan==2.19.1.1
```

### 3. Add your dataset

Place your historical CSV in the root folder named `district_weather.csv`  
Ensure it has at least: `Date`, `Temperature`

### 4. Add AccuWeather API key

Create a `.env` or edit the script directly with your:
- `LOCATION_KEY` (from AccuWeather)
- `API_KEY` (from AccuWeather Developer Portal)

---

## 📊 Output Example

- 10-day forecast from Prophet
- 10-day live forecast from API
- Accuracy comparison (optional)
- PDF/Excel export options (if web UI used)

---

## 📌 Sample Code Snippet

```python
import pandas as pd
from prophet import Prophet
import requests

# Load historical weather data
df = pd.read_csv('district_weather.csv')
df.rename(columns={'Date': 'ds', 'Temperature': 'y'}, inplace=True)

# Train the forecasting model
model = Prophet(daily_seasonality=True)
model.fit(df)

# Make 10-day forecast
future = model.make_future_dataframe(periods=10)
forecast = model.predict(future)

# Fetch live forecast from AccuWeather
def get_live_forecast(location_key, api_key):
    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/10day/{location_key}?apikey={api_key}&metric=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("API Error:", response.status_code)
```

---

## 📁 Folder Structure

```
weather-forecast-app/
│
├── weather_forecast.py     # Main script
├── district_weather.csv    # Historical data
├── templates/              # Flask HTML templates (optional)
└── static/                 # For images/CSS (optional)
```

---

## 🔐 Notes

- This version does not share company-specific data or credentials.
- You can extend the model to include precipitation, humidity, etc.

---

## 📎 License

MIT – feel free to adapt and improve!

---

---

## 📌 Author

Chandresh Rajpoot – Data Analyst | ML Enthusiast | Python Developer  
*This project is a personal initiative and is not affiliated with my current employer.*
