import requests
import json


response = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode&format=json&lang=en&type=twopart')

if response.status_code == 200:
    data = response.json()  # Parse JSON content of the response
    joke = data['setup'] + ";" + data['delivery'] # Access the joke field in the JSON data
    whole = response.text
    print(joke)
else:
    print('Error:', response.status_code)
