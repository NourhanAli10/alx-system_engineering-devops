#!/usr/bin/python3
"""sub.py"""
import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'.format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 400:
        return 0
    else:
        return 0
