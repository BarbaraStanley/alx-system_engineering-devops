#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """ function that queries api and prints titles of first 10 hot posts"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    header = {
            "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/kemitche)"
    }
    r = requests.get(url, headers=header, params=params, allow_redirects=False)

    if r.status_code != 200:
        print("None")
        return

    posts = r.json().get("data")
    [print(title.get("data").get("title")) for title in posts.get("children")]
