#!/usr/bin/python
# Script to set up basic Django structure

def prime_sieve(limit):
    multiples = set()
    for i in range(2, limit + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, limit + 1, i))

def largest_prime_factor(n):
    largest_factor = 1

    while n % 2 == 0:
        largest_factor = 2
        n = n // 2

    p = 3

    while n != 1:
        while n % p == 0:
            largest_factor = p
            n = n // p
        
        p += 2

    return largest_factor

def main():
    n = 600851475143
    print(list(prime_sieve(100)))
    print(largest_prime_factor(n))

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
