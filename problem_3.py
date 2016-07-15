#!/usr/bin/env python

import sys
import time


def get_prime_factors(number):
    prime_factors = {}
    prime_factor = 2
    cutoff = number**(1/2)
    while prime_factor <= cutoff:
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
    t_0 = time.time()
    result = get_largest_prime_factor(int(sys.argv[1]))
    t_f = time.time()
    t = t_f - t_0
    print('Largest prime factor = {}'.format(result))
    print('Time elapsed = {}s'.format(t))
