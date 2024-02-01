#!/usr/bin/python3
"""
Queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of total subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}

    # Perform the GET request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        # Subreddit not found
        return 0
    elif response.status_code != 200:
        # Other error (e.g., rate limit, server error)
        return 0

    try:
        # Try to parse the JSON response
        data = response.json()

        # Check if 'data' key is present and has 'subscribers' key
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0

    except ValueError:
        # JSON decoding failed
        return 0
