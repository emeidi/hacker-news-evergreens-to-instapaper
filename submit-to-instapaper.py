#!/usr/bin/env python

#debug = False
debug = True

urlFile = './urls-articles.txt'

instapaperUser = 'user'
instapaperPassword = 'password'

def d(msg):
	if not debug:
		return
	
	print msg

# basic modules
import sys
import os

# http://docs.python-requests.org/en/latest/
import requests

links = open(urlFile)

for link in links:
	d('Adding ' + link + ' to Instapaper ...')
	
	# https://www.instapaper.com/api/simple
	url = 'https://www.instapaper.com/api/add'
	
	# http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests
	post = {'url':link}
	
	r = requests.post(url, auth=(instapaperUser, instapaperPassword), data=post)
	status = r.status_code
	
	if(status != 201):
		d('    ERROR: Instapaper returned unexpected HTTP ' + status + ' for URL ' + link + '. Continuing.')
		continue
	
	d('Succesfully registered link')
	d('')