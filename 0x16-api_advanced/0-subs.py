#!/usr/bin/python3
"""
The module defines a function that queries data from an API
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers for a given subreddit

    Args:
        subreddit (str): The name of the subreddit to be used

    Returns:
        (int): number of total subscribers, or 0 if invalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoud Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        return data['data']['subscribers']
    elif response.status_code == 404:
        # subreddit not found
        return 0
    else:
        return 0
