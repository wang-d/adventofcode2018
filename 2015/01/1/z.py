#!/usr/bin/env python
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        for line in inf:
            sum = 0
            for c in line.strip():
                if c == '(':
                    sum += 1
                elif c == ')':
                    sum -= 1
                else:
                    assert False
            print sum
