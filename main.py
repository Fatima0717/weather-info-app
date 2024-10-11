import requests

def get_weather():
    try:
        # Make a request to wttr.in
        response = requests.get('https://wttr.in?format=%C+%t')
        # Check if request is successful
        if response.status_code == 200:
            weather_info = response.text.strip()
            print(f"Weather Information: {weather_info}")
        else:
            print("Failed to retrieve weather data.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_weather()
