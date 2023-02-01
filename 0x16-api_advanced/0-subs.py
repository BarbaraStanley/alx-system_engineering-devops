#!/usr/bin/python3
"""  function that queries the Reddit API and returns the number of subscriber
(not active users, total subscribers) for a given subreddit"""


def number_of_subscribers(subreddit):
    """ returns number of subscribers in subreddit"""
    import requests
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/kemitche)"
    }
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    subs = r.json().get("data")
    return subs.get("subscribers")
