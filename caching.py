"""
### Example of using caching in Python ###

This script demonstrates how to cache the results of a function using the cachetools library.

In this example, we create a simple weather API client that fetches weather data for a given city using the wttr.in API.

We use the cachetools library to cache the results of the API calls for a certain amount of time to avoid making redundant API calls.
"""
import requests
from cachetools import cached, TTLCache

# Create a cache with a time-to-live of 300 seconds (5 minutes)
weather_cache = TTLCache(maxsize=1, ttl=300)

# Decorator to cache the results of the function from the first call
@cached(weather_cache)
def get_weather(city):
    print(f"Fetching weather data for {city}...")
    response = requests.get(f"http://wttr.in/{city}?format=j1")
    return response.json()

# Fetch weather for a city (API call is made)
city1_weather = get_weather("New York")

# Fetch weather for the same city (API call is not made)
city1_weather_cached = get_weather("New York")

# Fetch weather for a different city (API call is made)
city2_weather = get_weather("San Diego")

print("City 1 weather:",
      city1_weather['current_condition'][0]['FeelsLikeC'], "celsius")
print("City 1 weather cached:",
      city1_weather_cached['current_condition'][0]['FeelsLikeC'], "celsius")
print("City 2 weather:",
      city2_weather['current_condition'][0]['FeelsLikeC'], "celsius")
