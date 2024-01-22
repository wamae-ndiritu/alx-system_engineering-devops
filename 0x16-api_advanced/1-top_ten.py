#!/usr/bin/python3
"""
Queries Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Get the titles of the first 10 hot posts listed for
    a given subreddit

    Args:
        subreddit (str): the name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            print(post['data']['title'])
    elif response.status_code == 404:
        print(None)
    else:
        print(None)
