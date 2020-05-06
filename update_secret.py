#!/usr/bin/python
# -*- coding: utf-8 -*-

from base64 import b64encode
from nacl import encoding, public
import json
import os
import requests as req
import sys


# GitHub OAuth token.
github_token = os.environ['PERSONAL_TOKEN']
# Path to the file storing refresh token.
path = sys.path[0] + r'/refresh_token.txt'


# Retrieves the public key.
def get_public_key():
    # Calls the endpoint.
    headers = {
        'Authorization': 'token ' + github_token,
        'Content-Type': 'application/json'
    }
    resp = req.get('https://api.github.com/repos/yunpengn/ping365/actions/secrets/public-key', headers=headers)
    if resp.status_code != 200:
        print('Unexpected resp when getting public key: {} {}'.format(resp.status_code, resp.text))
        exit(1)

    # Parses the response.
    data = json.loads(resp.text)
    return data['key_id'], data['key']


# Encrypts the given value with the public key.
def encrypt(public_key, plaintext):
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(plaintext.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


# Creates / updates the secret.
def set_secret(key_id, ciphertext):
    # Calls the endpoint.
    headers = {
        'Authorization': 'token ' + github_token,
        'Content-Type': 'application/json'
    }
    data = {
        'encrypted_value': ciphertext,
        'key_id': key_id
    }
    resp = req.put('https://api.github.com/repos/yunpengn/ping365/actions/secrets/APP_REFRESH_TOKEN', data=data, headers=headers)
    if resp.status_code != 200:
        print('Unexpected resp when setting secret: {} {}'.format(resp.status_code, resp.text))
        exit(1)

    # Success.
    return


# Sets the new refresh token.
if __name__ == "__main__":
    # Retrieves the value.
    if not os.path.isfile(path):
        print('{} is not a file.'.format(path))
        exit(1)
    file = open(path, 'r')
    refresh_token = file.read().replace('\n', '')
    print('Got the new refresh token.')

    # Gets the public key.
    key_id, public_key = get_public_key()
    print('Successully got the public key.')

    # Encrypts the token.
    ciphertext = encrypt(public_key, refresh_token)
    print('Successully encrypt the value.')

    # Updates the secret.
    set_secret(key_id, ciphertext)
    print('Complete.')
