#!/usr/bin/python3
"""
Sends a request to the URL
and displays the body of
the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    try:
        resp = requests.get(argv[1])
    except requests.exceptions.HTTPError as e:
        print('Error code:', e.response.status_code)
