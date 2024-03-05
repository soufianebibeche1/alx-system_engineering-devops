#!/usr/bin/python3
""" Recursively retrieve posts from a subreddit. """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Recursively retrieve posts from a subreddit's hot section."""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 404:
        return None
    if after is None:
        return hot_list
    for post in resp.json().get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    after = resp.json().get("data").get("after")
    recurse(subreddit, hot_list, after)
    return hot_list
