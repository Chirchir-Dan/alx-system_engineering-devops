#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse the titles of hot articles,
and count the occurrences of specified keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and counts the occurrences of specified keywords.

    Args:
        - subreddit: The name of the subreddit to query.
        - word_list: List of keywords to count (case-insensitive).
        - after: The 'after' parameter for pagination (used for recursion).
        - word_count: Dictionary to store the count of each keyword.

    Returns:
        - None. The results are printed in descending order of counts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])

    # Normalize word_list to lowercase
    word_list = [word.lower() for word in word_list]

    # Count occurrences of each keyword in the titles
    for post in posts:
        title = post['data'].get('title', '').lower().split()
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + title.count(word)

    # Check if there is a next page
    after = data.get('after')
    if after is not None:
        return count_words(subreddit, word_list, after, word_count)

    # Once recursion ends, print the results
    if word_count:
        sorted_word_count = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")
