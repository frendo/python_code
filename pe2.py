#!/usr/bin/python
# Script to set up basic Django structure

from math import sqrt

def fibo(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def main():
    total = 0 
    a, b = 0, 1
    
    while True:
        if b <= 4000000:
            a, b = b, a + b
            print(b) 
            if b % 2 == 0:
                total = total + b
        else:
            break

    print ('Total of evens:' + str(total))

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
