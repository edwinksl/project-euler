#!/usr/bin/env python

import sys

from problem_10 import is_prime


def main(number):
    i = 1
    prime_numbers = [2]
    odd_number = 1
    while i < number:
        odd_number += 2
        if is_prime(odd_number, prime_numbers):
            prime_numbers.append(odd_number)
            i += 1
    return odd_number

if __name__ == '__main__':
    print(main(int(sys.argv[1])))
