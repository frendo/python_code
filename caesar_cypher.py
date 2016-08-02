#!/usr/bin/python
# Script to set up basic Django structure

import string

def main():
    
    text_str = ('g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr' 
               'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj')
    secret_key = 2

    alphabet = list(string.ascii_lowercase)
    alphabet_str = ''.join(alphabet)
    alphabet_bytearray = bytearray()
    alphabet_bytearray.extend(alphabet_str.encode())
    
    alphabet_cyrpt = alphabet[secret_key:] + alphabet[:secret_key]
    alphabet_cyrpt_str  = ''.join(alphabet_cyrpt)
    alphabet_cyrpt_bytearray = bytearray()
    alphabet_cyrpt_bytearray.extend(alphabet_cyrpt_str.encode())
   
    table = bytearray.maketrans(alphabet_bytearray, alphabet_cyrpt_bytearray)
    
    print(text_str.translate(table))

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
