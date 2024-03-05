import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Make a GET request to the Reddit API without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

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

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"{subreddit} has {subscribers} subscribers.")
