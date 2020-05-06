#!/usr/bin/python
# -*- coding: utf-8 -*-

from base64 import b64encode
from nacl import encoding, public
import json
import os
import requests as req
import sys


# GitHub OAuth token.
github_token = os.environ['GITHUB_TOKEN']
# Path to the file storing refresh token.
path = sys.path[0] + r'/refresh_token.txt'


# Retrieves the public key.
def get_public_key():
	# Calls the endpoint.
	headers = {
        'Authorization': 'Bearer ' + github_token,
        'Content-Type': 'application/json'
    }
	resp = req.get('https://api.github.com/repos/yunpengn/ping365/actions/secrets/public-key', headers=headers)
	if resp.status_code != 200:
		print('Unexpected resp when getting public key: {}'.format(resp))

	# Parses the response.
	data = json.loads(resp.text)
	return data['key_id'], data['key']


# Encrypts the given value with the public key.
def encrypt(public_key, plaintext):
	return plaintext


# Creates / updates the secret.
def set_secret(key_id, ciphertext):
	return


# Sets the new refresh token.
if __name__ == "__main__":
	file = open(path, 'r')
	refresh_token = file.read().replace('\n', '')
