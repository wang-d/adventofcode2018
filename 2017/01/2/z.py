#!/usr/bin/env python
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        for line in inf:
            line=line.strip()
            n=len(line)
            assert (n % 2 == 0)
            half_n = n / 2
            sum=0
            for i, c in enumerate(line):
                j=(i + half_n) % n
                if c == line[j] :
                    sum += int(c)
            print sum
