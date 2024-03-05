#!/usr/bin/python3
"""
Get the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Print the titles of the first 10 hot posts
    listed for a given subreddit"""
    headers = {'User-Agent': 'My User Agent'}
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == '__main__':
    subreddit = input("Enter the subreddit name: ")
    print("{:d}".format(number_of_subscribers(subreddit)))
