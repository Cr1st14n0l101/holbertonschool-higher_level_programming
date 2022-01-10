#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest)"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    resp = requests.get(url)
    json_repr = resp.json()

    for i in range(10 if len(json_repr) >= 10 else len(json_repr)):
        sha = json_repr[i].get('sha')
        author_name = json_repr[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
