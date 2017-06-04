#!/usr/bin/env python

import sys


def main(number):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(number + 1):
        sum_of_squares += i**2
        square_of_sum += i
    square_of_sum *= square_of_sum
    diff = square_of_sum - sum_of_squares
    return diff


if __name__ == '__main__':
    print(main(int(sys.argv[1])))
