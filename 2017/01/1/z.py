#!/usr/bin/env python
import sys

def z(line):
    n=len(line)
    sum=0
    for i, c in enumerate(line):
        j=(i + 1) % n
        d=line[j]
        print i, j, c, d, sum
        if c == d:
            sum+=int(c)
    print sum

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        for line in inf:
            z(line.strip())
