#!/usr/bin/env python

import sys
import time


def get_prime_factors(number):
    prime_factors = {}

    # Check if 2 is a prime factor
    while True:
        if number % 2 == 0:
            if 2 not in prime_factors:
                prime_factors[2] = 1
            else:
                prime_factors[2] += 1
            number //= 2
        else:
            break

    # Check if odd number is a prime factor
    odd_number = 3
    while odd_number <= number:
        if number % odd_number == 0:
            if odd_number not in prime_factors:
                prime_factors[odd_number] = 1
            else:
                prime_factors[odd_number] += 1
            number //= odd_number
        else:
            odd_number += 2
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
