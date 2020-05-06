#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import requests as req
import sys
import time


# A counter.
num1 = 0
# Path to the file storing refresh token.
path = sys.path[0] + r'/refresh_token.txt'


# Uses the current token to retrieve new token and updates the storage.
def get_token(refresh_token):
    # Calls OAuth2 endpoint.
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': os.environ['APP_REFRESH_TOKEN'],
        'client_id': os.environ['APP_ID'],
        'client_secret': os.environ['APP_SECRET'],
        'redirect_uri': 'http://localhost:53682/',
    }
    resp = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data, headers=headers)
    data = json.loads(resp.text)

    # Stores the new refresh token to be used for the next time.
    with open(path, 'w+') as f:
        f.write(data['refresh_token'])

    # Returns the current access token.
    return data['access_token']


def main():
    # The global counter.
    global num1

    # The common header to be used.
    headers = {
        'Authorization': get_token(),
        'Content-Type': 'application/json'
    }

    try:
        # Calls all the different APIs.
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 1st call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 2nd call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/drive/root', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 3rd call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/users ', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 4th call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/me/messages', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 5th call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 6th call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 7th call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 8th call success".format(num1))
        if req.get(r'https://api.powerbi.com/v1.0/myorg/apps', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 9th call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 10th call success".format(num1))
        if req.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories', headers=headers).status_code == 200:
            num1 += 1
            print("#{}: 11th call success".format(num1))
        
        # Reports the timing.
        local_time = time.asctime(time.localtime(time.time()))
        print('Executed at {}'.format(local_time))
    except:
        print('Something goes wrong. Pass it.')
        pass

# Repeats for 3 times.
for _ in range(3):
    main()
