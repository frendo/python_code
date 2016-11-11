#!/usr/bin/pyth n
# Template for py programs

import sys
import urllib.request
import urllib.parse
import json


def main():

    serviceurl = 'http://python-data.dr-chuck.net/geojson?'

    while True:

        address = input('Enter Location:')

        if len(address) < 1:
            break

        url = serviceurl + urllib.parse.urlencode({'sensor': 'false',
                                                  'address': address})

        print ('Retrieving:', url)

        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')

        print ('Retrieved', len(data), 'characters')

        js = json.loads(data)

        """ print (json.dumps(js, indent=4)) """

        place_id = js["results"][0]["place_id"]

        print ('Place id:', place_id)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
