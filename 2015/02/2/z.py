#!/usr/bin/env python
import sys

def perimeter(x,y):
    return 2 * (x + y)

def volume(l, w, h):
    return l * w * h

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        total = 0
        for line in inf:
            xs = line.strip().split('x')
            l, w, h = int(xs[0]), int(xs[1]), int(xs[2])
            total += min([perimeter(l, w), perimeter(l, h), perimeter(w, h)]) + volume(l, w, h)
        print total

