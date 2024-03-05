# #!/usr/bin/python3
# """sub.py"""
# import requests


# def number_of_subscribers(subreddit):
#     # Reddit API endpoint for subreddit information
#     url = f'https://www.reddit.com/r/{subreddit}/about.json'.format(subreddit)
#     headers = {'User-Agent': 'CustomUserAgent'}

#     response = requests.get(url, headers=headers, allow_redirects=False)
#     if response.status_code == 200:
#         data = response.json()
#         subscribers = data['data']['subscribers']
#         return subscribers
#     elif response.status_code == 400:
#         return 0
#     else:
#         return 0
#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0