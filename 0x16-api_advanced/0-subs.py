#!/usr/bin/python3
"""sub.py"""
import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the number of subscribers from the response
        subscribers = data['data']['subscribers']
        
        return subscribers
    elif response.status_code == 404:
        # Invalid subreddit returns a 404 status code
        return 0
    else:
        # Handle other errors
        return 0



# import requests

# def number_of_subscribers(subreddit):
#     url = f'https://www.reddit.com/r/{subreddit}/about.json'
#     headers = {'User-Agent': 'CustomUserAgent'}

#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         data = response.json()
#         subscribers = data['data']['subscribers']
#         return subscribers
#     elif response.status_code == 400:
#         return(0)

