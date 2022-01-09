#!/usr/bin/python3
"""
Sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
    response = urllib.request.urlopen(sys.argv[1])
    headers = response.getheaders()
    content_type = response.getheader('X-Request-Id')
    print(content_type)
