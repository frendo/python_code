#!/usr/bin/python
# Script to set up basic Django structure

def factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n//2

    p = 3
    while n != 1:
        while n % p == 0:
            factors.append(p)
            n = n // p
        p += 2
    return factors

def factor_append(factors, new):
    if len(factors) == 0: 
        return new
    for i in range(len(new)):
        if i > 0  and new[i] == new[i-1]:
            continue
        new_count = new.count(new[i])
        old_count = factors.count(new[i])
        if new_count > old_count:
            for j in range(new_count - old_count):
                factors.append(new[i])
    factors.sort()
    return factors

def smallest_evenly_divisble(num):
    F = []
    for i in range(1, num + 1):
        F = factor_append(F, factors(i))
    product = 1
    print (F)
    for i in F:
        product *= i

    return product

def main():
    print (smallest_evenly_divisble(20))

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
