#!/usr/bin/pyth n
# Template for py programs

import sys
import urllib.request
import json


def main():

    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input('Enter URL: ')

    print ('Retrieving: ' + url)

    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

    # print ('Received', len(data), 'characters')

    js = json.loads((data))

    # print ('Count:', len(js))

    # print ('Note:', js['note'])

    # print ('Comments:', js['comments'])

    mylist = js['comments']

    print ('Count list:', len(mylist))

    totalSum = 0

    for item in mylist:

        # print('Name:', item['name'])

        # print ('Count:', item['count'])

        totalSum = int(item['count']) + totalSum

    print ('Sum:', str(totalSum))

    # print (json.dumps(js, indent=4))

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
