#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
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
        'refresh_token': refresh_token,
        'client_id': id,
        'client_secret': secret,
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
    fo = open(path, 'r+')
    refresh_token = fo.read()
    fo.close()

    global num1
    localtime = time.asctime(time.localtime(time.time()))
    access_token = get_token(refresh_token)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }

    try:
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root',
                   headers=headers).status_code == 200:
            num1 += 1
            print "1调用成功" + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive',
                   headers=headers).status_code == 200:
            num1 += 1
            print "2调用成功" + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/drive/root',
                   headers=headers).status_code == 200:
            num1 += 1
            print '3调用成功' + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/users ',
                   headers=headers).status_code == 200:
            num1 += 1
            print '4调用成功' + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/me/messages',
                   headers=headers).status_code == 200:
            num1 += 1
            print '5调用成功' + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules'
                   , headers=headers).status_code == 200:
            num1 += 1
            print '6调用成功' + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules'
                   , headers=headers).status_code == 200:
            num1 += 1
            print '7调用成功' + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children'
                   , headers=headers).status_code == 200:
            num1 += 1
            print '8调用成功' + str(num1) + '次'
        if req.get(r'https://api.powerbi.com/v1.0/myorg/apps',
                   headers=headers).status_code == 200:
            num1 += 1
            print '8调用成功' + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders',
                   headers=headers).status_code == 200:
            num1 += 1
            print '9调用成功' + str(num1) + '次'
        if req.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories'
                   , headers=headers).status_code == 200:
            num1 += 1
            print '10调用成功' + str(num1) + '次'
            print ('此次运行结束时间为: ', localtime)
    except:
        print 'pass'
        pass


# Repeats for 3 times.
for _ in range(3):
    main()
