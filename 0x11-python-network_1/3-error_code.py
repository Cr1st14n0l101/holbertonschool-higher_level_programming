#!/usr/bin/python3
"""
Sends a request to the URL and
displays the body of the response
(decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url=sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.getcode())
