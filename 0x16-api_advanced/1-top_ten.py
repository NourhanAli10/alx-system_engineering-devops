#!/usr/bin/python3
"""use reddit api to print the number the titles of
the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Reddit API endpoint for subreddit information"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'u/nourhan1414'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        children = data.get('children')
        for post in children:
            title = post['data']['title']
            print(title)
    elif response.status_code == 404:
        return None
