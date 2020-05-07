#!/usr/bin/python3
"""Queries the Reddit API
returns list of the titles of the hot articles for given subreddit.
if not valid subreddit return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns list of hot article titles of given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "Hello There 1.0"}
    response = requests.get(url, headers=user_agent, allow_redirects=False,
                            params={"after": after})
    if response.status_code != 200:
        return None
    else:
        children = response.json()["data"]["children"]
        hot_list.append([title["data"]["title"] for title in children])
        after = response.json()["data"]["after"]
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
