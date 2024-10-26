
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

# Running the Project
Option 1: Run Locally
To start the system locally:

python weather_monitoring.py
Option 2: Docker Setup
Dockerfile
The Dockerfile sets up the environment for running the application:

dockerfile
Copy code
# Use Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the files
COPY . .

# Default command to run the application
CMD ["python", "weather_monitoring.py"]
docker-compose.yml
Use Docker Compose to manage services more easily:

version: '3.8'

services:
  weather-monitoring:
    build: .
    environment:
      - API_KEY=your_api_key_here  # Replace with your OpenWeatherMap API key
    restart: always
Run Docker Container
After setting up the Dockerfile and docker-compose.yml, start the project with:
docker-compose up --build
# Code Structure

WeatherMonitoringSystem/
├── weather_monitoring.py       # Main script for fetching, processing, and analyzing data
├── requirements.txt            # Lists all required dependencies
├── Dockerfile                  # Dockerfile to create a containerized environment
├── docker-compose.yml          # Docker Compose file for easier deployment
└── README.md                   # Project documentation and setup instructions
# Functionality Overview
Data Retrieval
The get_weather_data() function retrieves real-time weather data from OpenWeatherMap, processing the JSON response to extract weather parameters.

Data Processing
The process_weather_data() function converts temperatures from Kelvin to Celsius or Fahrenheit, based on user preference. The function also aggregates data for daily summaries.

Rollups and Aggregates
1. Daily Weather Summary
The system calculates average, maximum, minimum temperatures, and the dominant weather condition each day.
Dominant Weather Condition: Determined based on frequency and duration of each condition.
2. Alerting Thresholds
Alerts can be configured based on user-defined temperature limits or weather conditions.
For example, users can set an alert if the temperature exceeds 35°C for two consecutive updates.
Visualization
Using Matplotlib, the system can visualize:

Daily temperature trends.
Alert events for configured thresholds.

# Testing
Test Cases
System Setup: Verify that the system successfully starts and connects to OpenWeatherMap using the correct API key.
Data Retrieval: Simulate API calls and ensure weather data is retrieved and parsed correctly for selected locations.
Temperature Conversion: Test Kelvin to Celsius/Fahrenheit conversions to ensure accuracy.
Daily Summary: Simulate multiple days of data and verify the accuracy of calculated daily summaries.
Alerts: Set up thresholds and simulate data that exceeds them to check if alerts trigger appropriately.
Running Tests
You can run the above tests by configuring mock data and thresholds in weather_monitoring.py and observing the output and alert triggers.

# Design Choices
Data Aggregation with Pandas: Pandas provides efficient processing for calculating averages and min/max values for weather data.
SQLite for Data Persistence: Chosen for simplicity and compatibility with Docker.
Alert System: Alerts trigger when thresholds are crossed, providing real-time notifications and enhancing user awareness of weather changes.
Dependencies

# All necessary dependencies are included in requirements.txt:

requests
pandas
matplotlib

# Future Enhancements
Additional Weather Parameters: Expand to track parameters like humidity, wind speed, or atmospheric pressure.
Forecast-Based Summaries: Extend functionality to retrieve and summarize weather forecasts.
Web Interface: Implement a simple UI to view daily summaries, alert history, and visualize trends over time.
Acknowledgments
OpenWeatherMap for providing the weather data API.
Pandas for powerful data manipulation and analysis tools.
Matplotlib for visualization support.

