#!/usr/bin/python3
"""
Using reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    result = requests.get(url, params=params, headers=headers,
                           allow_redirects=False)

    if result.status_code == 200:
        data = result.json().get("data").get("after")
        if data is not None:
            after = data
            recurse(subreddit, hot_list)
        titles = result.json().get("data").get("children")
        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return (None)
