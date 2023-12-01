#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
import urllib.request

try:
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        body = response.read()

        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)
        print('\t- utf8 content:', body.decode('utf-8'))
except urllib.error.URLError as e:
    print('Error:', str(e.reason))
