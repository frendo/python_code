#!/usr/bin/python
# Script to set up basic Django structure


def main():
   
    total = 0

    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i    
            
    print (total)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
