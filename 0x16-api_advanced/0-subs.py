#!/usr/bin/python3
"""
0. How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """
    return the number of subscribers for a given subreddit
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Alx School 0x16 task 0)'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
