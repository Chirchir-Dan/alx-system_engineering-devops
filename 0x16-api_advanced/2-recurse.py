#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list containing
the titles of all hot articles for a given subreddit..
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list containing
    the title of all hot articles for a given subreddit.

    Args:
        - subreddit: (string): The subreddit to query.
        - hot_list: (list): List to store title of the hot posts.
        - after: (optional): The 'after' parameter used for pagination
    Returns:
        - List of title of hot articles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])

    for post in posts:
        hot_list.append(post['data'].get('title'))

    after = data.get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list if hot_list else None
