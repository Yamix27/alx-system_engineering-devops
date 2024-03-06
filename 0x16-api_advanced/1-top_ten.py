#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles fo the first 10 hot posts
    listed for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers={"User-Agent": "Python-program"},
                            allow_redirects=False)

    if response.status_code >= 300:
        print("None")
    else:
        [print(child.get("data").get("title"))
                for child in response.json().get("data").get("children")]
