#!/usr/bin/python3
"""returns a list containing the titles of all hot artices for
a given subreddit"""


import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """returns a list containing the titles of all hot articles
            for a given subreddit"""

                url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
                    response = requests.get(url, params={"count": count, "after": after},
                            headers={"User-Agent": "Python-program"},
                            allow_redirects=False)

                    if response.status_code >= 400:
                        return None

                    list = hot_list + [child.get("data").get("title")
                            for child in response.json()
                            .get("data")
                            .get("children")]

                    data = response.json()
                                            if not data.get("data").get("after"):
                                                return list

                                            return recurse(subreddit, list, data.get("data").get("count"),
                                                    data.get("data").get("after"))
