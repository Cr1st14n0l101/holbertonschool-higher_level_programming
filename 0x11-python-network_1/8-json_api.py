#!/usr/bin/python3
"""
Sends a POST request to
a URL with the letter
as a parameter.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if argv[1] else ""
    try:
        resp = requests.post(url, data={'q': q})
        json_repr = resp.json()
        if json_repr:
            print(
                '[{}] {}'.format(json_repr.get('id'), json_repr.get('name'))
                )
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
