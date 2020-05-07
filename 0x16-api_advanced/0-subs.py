#!/usr/bin/python3
"""Queries the Reddit API
returns the number of subscribers for a given subreddit.
if invalid subreddit is given return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers or 0"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "Hello There 1.0"}
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json()["data"]["subscribers"]
