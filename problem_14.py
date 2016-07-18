#!/usr/bin/env python

import sys


def main(number):
    # n = 1
    n = 1
    sequence = [n]
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    sequence.append(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        sequence.append(n)
    max_starting_number = n
    max_length = len(sequence)

    # n > 1
    for i in range(2, number):
        n = i
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3*n + 1
            sequence.append(n)
        sequence_length = len(sequence)
        if sequence_length > max_length:
            max_starting_number = i
            max_length = sequence_length

    return max_starting_number

if __name__ == '__main__':
    print(main(int(sys.argv[1])))
