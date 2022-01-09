#!/usr/bin/python3
"""
Sends a request to the URL
and displays the body of
the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get(argv[1])
    if resp.status_code >= 400:
        print('Error code:', resp.status_code)
    else:
        print(resp.text)
