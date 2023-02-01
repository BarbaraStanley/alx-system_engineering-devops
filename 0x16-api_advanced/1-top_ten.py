#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """ function that queries api and prints titles of first 10 hot posts"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit":10}
    result = requests.get(url, params=params, allow_redirects=False)

    if result.status_code == 404:
        print("None")

    posts = result.json().get("data")
    [print(title.get("data").get("title")) for title in posts.get("children")]
