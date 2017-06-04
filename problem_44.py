#!/usr/bin/env python


def get_pentagonal_number(n):
    return n*(3*n-1)/2  # yapf: disable


def is_pentagonal_number(x):
    n = 1/6*(1 + (1+24*x)**(1/2))  # yapf: disable
    return n.is_integer()


def main():
    sequence = []
    for i in range(1, 3):
        sequence.append(get_pentagonal_number(i))
    while True:
        last_term = sequence[-1]
        for first_term in sequence[:-1]:
            sum_terms = last_term + first_term
            diff_terms = last_term - first_term
            if is_pentagonal_number(sum_terms) and is_pentagonal_number(diff_terms):  # yapf: disable
                return int(diff_terms)
        sequence.append(get_pentagonal_number(len(sequence)+1))  # yapf: disable


if __name__ == '__main__':
    print(main())
