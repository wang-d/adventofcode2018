#!/usr/bin/env python
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        for line in inf:
            sum = 0
            for i, c in enumerate(line.strip()):
                if c == '(':
                    sum += 1
                elif c == ')':
                    sum -= 1
                else:
                    assert False
                if sum < 0:
                    print (i + 1)
                    break
