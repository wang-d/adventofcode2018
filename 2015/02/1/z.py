#!/usr/bin/env python
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        total = 0
        for line in inf:
            xs = line.strip().split('x')
            l, w, h = int(xs[0]), int(xs[1]), int(xs[2])
            sides = [ l * w, w * h, l * h ]
            total += 2 * sum(sides) + min(sides)
        print total

