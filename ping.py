#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import requests as req
import sys
import time


# A counter.
count = 0
# Path to the file storing refresh token.
path = sys.path[0] + r'/refresh_token.txt'


# Uses the current token to retrieve new token and updates the storage.
def get_token():
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
    global count

    # The common header to be used.
    headers = {
        'Authorization': get_token(),
        'Content-Type': 'application/json'
    }

    try:
        print('==================================')
        endpoints = [
            'https://graph.microsoft.com/v1.0/drive/root',
            'https://graph.microsoft.com/v1.0/me/drive',
            'https://graph.microsoft.com/v1.0/me/drive/root',
            'https://graph.microsoft.com/v1.0/me/drive/root/children',
            'https://graph.microsoft.com/v1.0/users',
            'https://graph.microsoft.com/v1.0/me/messages',
            'https://graph.microsoft.com/v1.0/me/mailFolders',
            'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
            'https://graph.microsoft.com/v1.0/me/outlook/masterCategories',
            'https://api.powerbi.com/v1.0/myorg/apps'
        ]

        # Calls all the different APIs.
        for endpoint in endpoints:
            resp = req.get(endpoint, headers=headers)
            if resp.status_code == 200:
                count += 1
                print("#{}: API call to {} success".format(count, endpoint))
            else:
                print("#{}: invalid resp to {}: {}".format(count, endpoint, resp))
        
        # Reports the timing.
        local_time = time.asctime(time.localtime(time.time()))
        print('Execution finishes at {}'.format(local_time))
        print('==================================\n')
    except:
        print('Something goes wrong. Pass it.')
        pass

# Repeats for 3 times.
for _ in range(3):
    main()
