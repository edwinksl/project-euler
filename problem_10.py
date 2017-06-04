#!/usr/bin/env python

import sys
import time


def is_prime(number, prime_numbers):
    cutoff = int(number**(1/2))  # yapf: disable
    for i in prime_numbers:
        if number % i == 0:
            return False
        if i >= cutoff:
            return True


def get_prime_numbers(number):
    prime_numbers = [2]
    for i in range(3, number, 2):
        if is_prime(i, prime_numbers):
            prime_numbers.append(i)
    return prime_numbers


def main(number):
    return sum(get_prime_numbers(number))


if __name__ == '__main__':
    t_0 = time.time()
    result = main(int(sys.argv[1]))
    t_f = time.time()
    t = t_f - t_0
    print('Sum = {}'.format(result))
    print('Time taken = {} s'.format(t))
