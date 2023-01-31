#!/usr/bin/python3
"""  function that queries the Reddit API and returns the number of subscriber
(not active users, total subscribers) for a given subreddit"""


def number_of_subscribers(subreddit):
    """ returns number of subscribers in subreddit"""
    import requests
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url)

    if r.status_code != 200:
        return 0

    subs = r.json().get("data")
    return subs.get("subscribers")
