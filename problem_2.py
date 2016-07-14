#!/usr/bin/env python

import sys


def main(number):
    a_1 = 1
    a_2 = 2
    a = a_1 + a_2
    result = 2
    while a < number:
        a_1 = a_2
        a_2 = a
        a = a_1 + a_2
        if a % 2 == 0:
            result += a
    return result

if __name__ == '__main__':
    print(main(int(sys.argv[1])))
