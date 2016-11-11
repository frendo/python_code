#!/usr/bin/python
# Program to scrap xml page links using xml etree

import urllib.request
import xml.etree.ElementTree as ET
import sys


def process_urls(url):

    print ('Retrieving URL: ', url)

    with urllib.request.urlopen(url) as response:

        xmlData = response.read()

        print ('Received', len(xmlData), 'characters.')

        tree = ET.fromstring(xmlData)

    xml_cnt = 0

    comments = tree.findall('comments/comment')

    print ('Comment count: ', len(comments))

    for items in comments:

        xml_cnt = xml_cnt + int(items.find('count').text)

    print ('Total count:', xml_cnt)

    xml_cnt = 0

    counts_xpath = tree.findall('.//count')

    for cnts in counts_xpath:

        xml_cnt = xml_cnt + (int(cnts.text))

    print ('Total count (xpath method):', xml_cnt)


def main():

    url = ''

    if len(sys.argv) > 1:

        url = sys.argv[1]

    else:

        url = input('Enter URL: ')

    process_urls(url)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
