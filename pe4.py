#!/usr/bin/python
# Script to set up basic Django structure

def is_palindrome(num):
    if (str(num)==str(num)[::-1]):
        return True
    else:
        return False

def find_max_palindrome(min=100, max=999):
    max_palindrome = 0
    for a in range(min, max + 1):
        for b in range(a + 1, max + 1):
            prod = a * b
            if (prod > max_palindrome and str(prod)==(str(prod)[::-1])):
                max_palindrome = prod
    return max_palindrome

def main():
    print(is_palindrome(99))
    print (find_max_palindrome())

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
