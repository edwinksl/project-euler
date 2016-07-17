#!/usr/bin/env python

from problem_18 import get_max_path_sum


def get_args():
    args = []
    with open('resources/p067_triangle.txt', 'r') as f:
        for line in f:
            numbers = [int(i) for i in line.split()]
            args.append(numbers)
    return args


def main():
    return get_max_path_sum(get_args())

if __name__ == '__main__':
    print(main())
