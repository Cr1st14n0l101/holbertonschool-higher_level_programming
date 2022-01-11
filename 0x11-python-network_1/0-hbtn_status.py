#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('- type:', type(html))
        print('- content:', html)
        print('- utf8 content:', html.decode('UTF-8'))
