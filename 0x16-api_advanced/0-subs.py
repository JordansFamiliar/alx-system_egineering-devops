#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """Returns the number of total subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0\
        (by /u/Large_Alternative_30)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            print(f"Unexpected JSON format: {data}")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return 0
    except ValueError as ve:
        print(f"Error decoding JSON: {ve}")
        return 0
