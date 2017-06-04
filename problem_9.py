#!/usr/bin/env python

import sys


def main(constraint):
    for i in range(1, constraint+1):  # yapf: disable
        for j in range(i, constraint+1):  # yapf: disable
            k = constraint - i - j
            if i**2 + j**2 == k**2:
                return i*j*k  # yapf: disable


if __name__ == '__main__':
    print(main(int(sys.argv[1])))
