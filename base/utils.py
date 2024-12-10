import requests
from datetime import datetime
from decouple import config


def fetch_weather_data(location="New York"):
    API_KEY = config('api_key')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    data = response.json()
    return {
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    }

def is_busy_time():
    """
    Determines if the current time is considered busy based on 
    - Time of day
    - Day of the week
    - Simulated reservation count
    """
    # Simulate reservation data
    current_hour = datetime.now().hour
    current_day = datetime.now().weekday()  # Monday=0, Sunday=6
    
    # Hypothetical thresholds
    peak_hours = range(18, 22)  # Busy between 6 PM and 10 PM
    weekend_days = [5, 6]  # Saturday and Sunday are busier
    reservation_count = 30

    # Determine busyness
    is_peak_time = current_hour in peak_hours
    is_weekend = current_day in weekend_days
    is_high_reservations = reservation_count > 20
    
    return is_peak_time or is_weekend or is_high_reservations

