#!/usr/bin/python3
"""sub.py"""
import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'api'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    subscribers = data.get('subscribers')
    return subscribers

