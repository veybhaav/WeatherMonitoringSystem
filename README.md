
# Real-Time Data Processing System for Weather Monitoring
# Project Overview
This project is a real-time data processing system designed to monitor weather conditions for specific metro cities in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad). The system retrieves data from the OpenWeatherMap API at configurable intervals, processes and aggregates the data, and provides daily weather summaries. Users can set alert thresholds for temperature and other weather conditions, and the system can trigger alerts when these thresholds are crossed.

# Features
Real-Time Data Retrieval: Collects weather data from OpenWeatherMap API every 5 minutes (or user-configurable interval).
Data Processing: Converts temperatures from Kelvin to Celsius (with option for Fahrenheit).
Daily Weather Summaries: Calculates average, max, min temperatures, and dominant weather conditions for each city.
Threshold-Based Alerts: Alerts if temperature or specific weather conditions exceed user-defined thresholds.
Visualization: Displays daily trends and summaries (e.g., daily temperatures, alert history).

# Prerequisites
Python 3.x
OpenWeatherMap API Key: Sign up for a free API key from OpenWeatherMap.
Docker (for optional containerized setup)
SQLite3 (included with Python)

# Installation & Setup
Step 1: Clone the Repository
Clone this repository to your local system:
git clone https://github.com/your_username/WeatherMonitoringSystem.git
cd WeatherMonitoringSystem

Step 2: Install Dependencies
Install the required Python libraries:
pip install -r requirements.txt
Alternatively, you can use Docker to create a containerized environment. Follow the Docker Setup instructions below if preferred.

Step 3: Set Up API Key
To access weather data, replace "caa0a3e956165b252d08da71b7639280" in the weather_monitoring.py file with your API key from OpenWeatherMap:


API_KEY = "caa0a3e956165b252d08da71b7639280"

Step 4: Configurations
City Selection: Modify the list of cities in weather_monitoring.py if you want to monitor different locations.
API Call Interval: Adjust the API call frequency by changing the interval parameter in fetch_data_periodically function (default is 300 seconds).

