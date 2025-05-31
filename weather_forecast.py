import pandas as pd
from prophet import Prophet
import requests
import json
import datetime

# Step 1: Load and prepare historical data
df = pd.read_csv('district_weather.csv')  # Ensure columns: Date, Temperature
df = df.rename(columns={'Date': 'ds', 'Temperature': 'y'})  # Prophet expects 'ds' and 'y'

# Step 2: Initialize and train the model
model = Prophet(daily_seasonality=True)
model.fit(df)

# Step 3: Forecast next 10 days
future = model.make_future_dataframe(periods=10)
forecast = model.predict(future)

# Step 4: Print the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

# Step 5: Fetch live data from AccuWeather API
def get_live_forecast(location_key, api_key):
    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/10day/{location_key}?apikey={api_key}&metric=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        forecast_data = response.json()
        return [
            {
                "date": item["Date"],
                "min_temp": item["Temperature"]["Minimum"]["Value"],
                "max_temp": item["Temperature"]["Maximum"]["Value"],
                "description": item["Day"]["IconPhrase"]
            }
            for item in forecast_data["DailyForecasts"]
        ]
    else:
        print(f"API call failed with status code {response.status_code}")
        return []

# Example usage
location_key = '123456'  # Replace with your actual location key
api_key = 'your_accuweather_api_key'
live_data = get_live_forecast(location_key, api_key)

for day in live_data:
    print(day)
