#!/usr/bin/python3
"""
Module: reddit_subscribers

This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit. If the subreddit is invalid, the function
returns 0.

Functions:
    number_of_subscribers(subreddit): Returns the number of subscribers for the
    given subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.

    If the subreddit is invalid, returns 0.
    """
    # Define the URL for the subreddit's about page in the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my-reddit-app/0.1'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # Return 0 for invalid subreddit or any other error
            return 0
    except requests.RequestException:
        # Return 0 if there is a network-related error
        return 0
