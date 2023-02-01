#!/usr/bin/python3
""" function that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit """

import requests


def recurse(subreddit, hot_list=[]):
    """ recursive function """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "count": count, "limit": 100}
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/kemitche)"
    }
    result = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if result.status_code != 200:
        print("None")
        return

    res = result.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
