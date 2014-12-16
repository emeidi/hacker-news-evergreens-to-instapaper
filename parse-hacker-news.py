#!/usr/bin/env python

#debug = False
debug = True

cacheDir = './cache'
htmlDumpFilenamesStartWith = 'item'
urlFile = './urls-articles.txt'

def d(msg):
	if not debug:
		return
	
	print msg

# basic modules
import sys
import os

# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html
from BeautifulSoup import BeautifulSoup

paths = []
for dirname, dirnames, filenames in os.walk(cacheDir):
	for filename in filenames:
		if(filename.startswith(htmlDumpFilenamesStartWith)):
			filepath = os.path.join(dirname, filename)
			paths.append(filepath)

#print files

links = []
for path in paths:
	d("Reading file '" + path + "' ...")
	
	file = open(path)
	html = file.read()
	
	soup = BeautifulSoup(html)
	tablecell = soup.find('td', { 'class':'title' })
	
	try:
		link = tablecell.find('a')
	except:
		d("    ERROR: No tablecell or anchor found. Skipping.")
		d("")
		continue
	
	try:
		href = link['href']
	except:
		d("    ERROR: No href attribute found. Skipping.")
		d("")
		continue
	
	links.append(href)

if os.path.exists(urlFile):
	d("ERROR: File '" + urlFile + "' already exists. Please remove file before calling this script. Aborting.")
	sys.exit(1)

file = open(urlFile,'w')

for link in links:
	print link
	
	file.write(link + "\n")