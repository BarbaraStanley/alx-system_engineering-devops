#!/usr/bin/python3
"""  function that queries the Reddit API and returns the number of subscriber
(not active users, total subscribers) for a given subreddit"""


def number_of_subscribers(subreddit):
    """ returns number of subscribers in subreddit"""
    import requests
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit))

    if response.status_code != 200:
        return 0

    subs = response.json().get("data")
    return subs.get("subscribers")
