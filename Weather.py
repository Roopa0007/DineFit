import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "https://api.open-meteo.com/v1/forecast"

def get_weather(city, latitude, longitude):
    """Fetch current temperature for a given city."""
    try:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
        response = requests.get(API_KEY, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["current_weather"]["temperature"]
    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")
        return None

def main():
    city_coords = {
        "London": (51.5072, -0.1276),
        "New York": (40.7128, -74.0060),
        "Tokyo": (35.6895, 139.6917),
        "Sydney": (-33.8688, 151.2093),
        "Paris": (48.8566, 2.3522)
    }

    weather_data = []
    for city, (lat, lon) in city_coords.items():
        temp = get_weather(city, lat, lon)
        if temp is not None:
            weather_data.append({"City": city, "Temperature (°C)": temp})

    if not weather_data:
        print("No data available to display.")
        return

    df = pd.DataFrame(weather_data)
    df.sort_values(by="Temperature (°C)", ascending=False, inplace=True)

    plt.figure(figsize=(8, 5))
    plt.bar(df["City"], df["Temperature (°C)"], color="#4682B4")
    plt.title("🌍 Current Temperature Comparison", fontsize=14, fontweight="bold")
    plt.xlabel("City", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
