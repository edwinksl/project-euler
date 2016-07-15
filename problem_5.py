#!/usr/bin/env python

import sys


def main(upper_bound):
    result = upper_bound
    while True:
        if not is_evenly_divisible(result, upper_bound):
            result += 1
        else:
            return result


def is_evenly_divisible(number, upper_bound):
    for i in range(1, upper_bound):
        if number % i != 0:
            return False
    return True

if __name__ == '__main__':
    print(main(int(sys.argv[1])))
