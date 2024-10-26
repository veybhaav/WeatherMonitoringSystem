
# Real-Time Data Processing System for Weather Monitoring
# Project Overview
# This project is a real-time data processing system designed to monitor weather conditions for specific metro cities in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad). The system retrieves data from the OpenWeatherMap API at configurable intervals, processes and aggregates the data, and provides daily weather summaries. Users can set alert thresholds for temperature and other weather conditions, and the system can trigger alerts when these thresholds are crossed.

# Features
Real-Time Data Retrieval: Collects weather data from OpenWeatherMap API every 5 minutes (or user-configurable interval).
Data Processing: Converts temperatures from Kelvin to Celsius (with option for Fahrenheit).
Daily Weather Summaries: Calculates average, max, min temperatures, and dominant weather conditions for each city.
Threshold-Based Alerts: Alerts if temperature or specific weather conditions exceed user-defined thresholds.
Visualization: Displays daily trends and summaries (e.g., daily temperatures, alert history).
