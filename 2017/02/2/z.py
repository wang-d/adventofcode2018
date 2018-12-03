#!/usr/bin/env python
import sys

def divides(n, d):
    return d * (n / d) == n

def find_only_even_division(line):
    for i in xrange(len(line)):
        for j in xrange(i + 1, len(line)):
            if divides(line[j], line[i]):
                return line[j] / line[i]

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        sum = 0
        for line in inf:
            line = sorted([ int(c) for c in line.strip().split() ])
            sum += find_only_even_division(line)
        print sum

