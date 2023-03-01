#!/usr/bin/python3
""" function that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit """

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ recursive function """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "count": count, "limit": 100}
    headr = {
            "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/kemitche)"
    }
    r = requests.get(url, headers=headr, params=params, allow_redirects=False)

    if r.status_code != 200:
        return

    res = r.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
