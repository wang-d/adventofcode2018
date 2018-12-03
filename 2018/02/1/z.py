#!/usr/bin/env python
import sys

def count_chars(s):
    a={}
    for c in s:
        if c in a: a[c] += 1
        else: a[c] = 1
    return a

def has_n(char_count, n):
    for c in char_count:
        if char_count[c] == n:
            return True
    return False

if __name__ == '__main__':
    has_2 = 0
    has_3 = 0
    with open(sys.argv[1]) as inf:
        for line in inf:
            char_count=count_chars(line)
            if has_n(char_count, 2): has_2 += 1
            if has_n(char_count, 3): has_3 += 1
    print has_2, has_3, has_2 * has_3
    
