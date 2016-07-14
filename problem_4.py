#!/usr/bin/env python

import sys

def main():
    result = 1
    for i in range(1, 1000):
        for j in range(i, 1000):
            temp_result = i*j
            temp_str = str(temp_result)
            if temp_str == temp_str[::-1] and temp_result > result:
                result = temp_result
    return result

if __name__ == '__main__':
    print(main())
