#!/usr/bin/pyth n
# Program to scrap web page thinks using BeautifulSoup4
#for tag in tags:
#    print (tag.get('href', None))

from bs4 import *
import urllib.request
import sys

def get_tags(url, tags):

	with urllib.request.urlopen(url) as response:
		html = response.read()
	soup = BeautifulSoup(html, "html.parser")
	# Retrieve all of the anchor tags
	tags = soup('span')

	return tags

def process_urls(url):

    tags = ''
    span_count = 0
    span_sum = 0
    tags = get_tags(url,tags)

    for tag in tags:
        span_sum = span_sum + int(tag.string)
        span_count = span_count + 1

    print ('Count ', span_count)
    print ('Sum', span_sum)

def main():

    if len(sys.argv) > 2:
        url = int(sys.argv[1])
    else:
        url = input('Enter URL: ')

    process_urls(url)

if __name__ == '__main__':
  main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
