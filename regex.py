#!/usr/bin/python
# Script to set up basic Django structure

import re

def main():

    file = open('gibb.txt', 'r')
    ix = []
    
    for line in file:
        letter = re.findall('[a-z]', line)
        if letter:
            #print (re.findall('[a-z]', line))
            ix.extend(letter)

    print (''.join(ix))

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
