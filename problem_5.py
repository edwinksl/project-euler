#!/usr/bin/env python

import sys

from problem_3 import get_prime_factors


def main(upper_bound):
    factors = {}
    for i in range(2, upper_bound + 1):
        prime_factors = get_prime_factors(i)
        for j in prime_factors:
            if j not in factors:
                factors[j] = prime_factors[j]
            else:
                if prime_factors[j] > factors[j]:
                    factors[j] = prime_factors[j]
    result = 1
    for prime_factor, exponent in factors.items():
        result *= prime_factor**exponent
    return result


if __name__ == '__main__':
    print(main(int(sys.argv[1])))
