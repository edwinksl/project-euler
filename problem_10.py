#!/usr/bin/env python

import sys


def main(number):
    prime_numbers = [2]
    for i in range(2,number):
        if is_prime(i,prime_numbers):
            prime_numbers.append(i)
    return sum(prime_numbers)


def is_prime(number, prime_numbers):
    for i in prime_numbers:
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    result = main(int(sys.argv[1]))
    print(result)
