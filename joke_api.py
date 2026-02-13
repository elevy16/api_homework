import requests
import json


# Function to print JSON nicely (from the tutorial)
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# Call the JokeAPI
try:
    response = requests.get("https://v2.jokeapi.dev/joke/Programming", timeout=5)

    # Check if the request was successful
    if response.status_code == 200:
        print("✅ Successfully connected to JokeAPI!")
        print(f"Status Code: {response.status_code}\n")

        # Get the joke data
        joke_data = response.json()

        # Print the full response (nicely formatted)
        print("Full API Response:")
        jprint(joke_data)

        # Extract and print just the joke
        print("\n" + "=" * 50)
        print("THE JOKE:")
        print("=" * 50)
        if joke_data['type'] == 'single':
            print(joke_data['joke'])
        else:
            # Some jokes have setup and delivery
            print(f"Setup: {joke_data['setup']}")
            print(f"Punchline: {joke_data['delivery']}")
        print("=" * 50)

    else:
        print(f"❌ Error: Got status code {response.status_code}")

except requests.exceptions.Timeout:
    print("❌ The request timed out. Try again later.")
except requests.exceptions.RequestException as e:
    print(f"❌ Something went wrong: {e}")