#!/usr/bin/python3
"""sub.py"""
import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    username = 'nourhan1414'
    refresh_token = "89041561833551-aB7ymnQsR1I6Oigfk63YrTnI-XYOsA"
    user_pass_dict = {'user': username,'api_type': 'json'}
    headers = {'user-agent': '/u/nourhan1414 API Python',
               'Authorization': f'Bearer {refresh_token}'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': ' u/IZMmFoTgvneF469yS8ZVjA'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 400:
        return 0
    else:
        return 0
