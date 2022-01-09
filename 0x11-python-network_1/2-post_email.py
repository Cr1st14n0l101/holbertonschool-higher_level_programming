#!/usr/bin/python3
"""
Sends a POST request to the passed URL
with the email as a parameter,and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    post_data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(url=sys.argv[1], data=post_data) as response:
        print(response.read().decode('UTF-8'))
