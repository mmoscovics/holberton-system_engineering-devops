#!/usr/bin/python3
"""Queries the Reddit API
prints the titles of the first 10 hot posts listen for given subreddit.
if not valid subreddit print None.
"""
import requests


def top_ten(subreddit):
    """Prints 10 hot post titles of given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "Hello There 1.0"}
    limit = {"limit": 10}
    response = requests.get(url, headers=user_agent, allow_redirects=False,
                            params=limit)
    if response.status_code != 200:
        print("None")
    else:
        children = response.json()["data"]["children"]
        for title in children:
            print(title["data"]["title"])
