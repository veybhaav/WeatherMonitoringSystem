import requests
import sqlite3
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Constants
API_KEY = "caa0a3e956165b252d08da71b7639280"
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
ALERT_THRESHOLD = 35  # Temperature alert threshold in Celsius

# Database setup
def setup_database():
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                      city TEXT,
                      timestamp INTEGER,
                      temp REAL,
                      feels_like REAL,
                      condition TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                      city TEXT,
                      date DATE,
                      avg_temp REAL,
                      max_temp REAL,
                      min_temp REAL,
                      dominant_condition TEXT)''')
    conn.commit()
    conn.close()

# Fetch weather data
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={'caa0a3e956165b252d08da71b7639280'}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Convert Kelvin to Celsius
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

# Process data and store in database
def process_and_store_data(data, city):
    temp_celsius = kelvin_to_celsius(data["main"]["temp"])
    feels_like_celsius = kelvin_to_celsius(data["main"]["feels_like"])
    condition = data["weather"][0]["main"]
    timestamp = data["dt"]

    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather_data (city, timestamp, temp, feels_like, condition)
                      VALUES (?, ?, ?, ?, ?)''',
                   (city, timestamp, temp_celsius, feels_like_celsius, condition))
    conn.commit()
    conn.close()

    check_alerts(temp_celsius, city)

# Check for alerts
def check_alerts(temp, city):
    if temp > ALERT_THRESHOLD:
        print(f"ALERT: Temperature in {city} exceeded threshold with {temp:.2f} °C!")

# Fetch data periodically
def fetch_data_periodically(interval=300):
    while True:
        for city in CITIES:
            data = get_weather_data(city)
            if data:
                process_and_store_data(data, city)
        time.sleep(interval)

# Calculate daily summary
def calculate_daily_summary():
    today = datetime.now().date()
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()

    for city in CITIES:
        data = pd.read_sql_query(f"SELECT * FROM weather_data WHERE city='{city}'", conn)
        if not data.empty:
            avg_temp = data["temp"].mean()
            max_temp = data["temp"].max()
            min_temp = data["temp"].min()
            dominant_condition = data["condition"].mode()[0]

            cursor.execute('''INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (city, today, avg_temp, max_temp, min_temp, dominant_condition))

    conn.commit()
    conn.close()

# Plot temperature trends
def plot_temperature_trends(city):
    conn = sqlite3.connect("weather_data.db")
    data = pd.read_sql_query(f"SELECT * FROM weather_data WHERE city='{city}'", conn)

    if data.empty:
        print(f"No data available for {city}.")
        conn.close()
        return

    data["timestamp"] = pd.to_datetime(data["timestamp"], unit='s')
    plt.plot(data["timestamp"], data["temp"], label="Temperature")
    plt.title(f"Temperature Trends for {city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.show()
    conn.close()

# Run the setup
setup_database()

# Uncomment the below line to run data fetching periodically (every 5 minutes)
fetch_data_periodically(interval=300)

# Uncomment to calculate daily summaries (recommend running once per day)
calculate_daily_summary()

# Uncomment to plot temperature trends for a specific city (e.g., 'Delhi')
plot_temperature_trends("Delhi")
