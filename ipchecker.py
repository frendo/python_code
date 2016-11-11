#!/usr/bin/python
# Script to check external Ip address in background process

import time
import urllib.request
from bs4 import *


def get_external_ip(url):

    with urllib.request.urlopen(url) as response:
        html = response.read()
    ip = str(BeautifulSoup(html, "html.parser"))
    return ip


def check_ip(ip_seed, url):

    ip = get_external_ip(url)

    if ip == ip_seed:
        print('no change')
    else:
        print('new ip: ', ip)
        ip_seed = ip

    return ip_seed


def main():

    ip_seed = ''
    url = 'http://myexternalip.com/raw'
    ip_seed = get_external_ip(url)
    print('External ip: ', ip_seed)
    i = 0

    while i < 3:

        ip_seed = check_ip(ip_seed, url)

        time.sleep(5)
        i = i + 1


if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
