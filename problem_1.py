#!/usr/bin/env python

import sys


def main(number):
    result = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

if __name__ == '__main__':
    print(main(int(sys.argv[1])))
