#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    resp = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(resp.text))
    print('\t- content:', resp.text)
