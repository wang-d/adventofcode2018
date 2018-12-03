#!/usr/bin/env python
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        sum = 0
        for line in inf:
            line = [ int(c) for c in line.strip().split() ]
            smallest = min(line)
            largest = max(line)
            sum += largest - smallest
        print sum

