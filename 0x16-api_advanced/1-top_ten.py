#!/usr/bin/python3
"""
Retrieve top ten posts from a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.

    :param subreddit: The subreddit name.
    """
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for post in children:
                    post_details = post.get("data")
                    print(post_details.get("title"))
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(None)
        elif e.response.status_code == 403:
            print("Access to the subreddit is forbidden. Please check your permissions.")
        else:
            print("Error occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
