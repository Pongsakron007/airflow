import requests
import json

api_url = "https://api.chnwt.dev/thai-gold-api/latest"

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    print("API is working. Data:")
    print(json.dumps(data, indent=2))
except requests.exceptions.RequestException as e:
    print(f"API is not reachable or an error occurred: {e}")
except json.JSONDecodeError:
    print("Failed to decode JSON from API response.")
