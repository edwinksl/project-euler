#!/usr/bin/env python

import sys


def get_prime_factors(number):
    prime_factors = {}
    prime_factor = 2
    while prime_factor <= number:
        if number % prime_factor == 0:
            if prime_factor not in prime_factors:
                prime_factors[prime_factor] = 1
            else:
                prime_factors[prime_factor] += 1
            number //= prime_factor
        else:
            prime_factor += 1
    return prime_factors


def get_largest_prime_factor(number):
    prime_factors = get_prime_factors(number).keys()
    return sorted(prime_factors, reverse=True)[0]

if __name__ == '__main__':
    print(get_largest_prime_factor(int(sys.argv[1])))
