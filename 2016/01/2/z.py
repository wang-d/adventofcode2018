#!/usr/bin/env python
import sys

direction = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
n_dir = len(direction)

def z (line):
    x, y=(0, 0)
    d_i=0
    steps = line.strip().split(", ")
    visited=set()
    for step in steps:
        if 'L' == step[0]:
            d_i = (d_i - 1) % n_dir
        elif 'R' == step[0]:
            d_i = (d_i + 1) % n_dir
        else:
            assert false
        x_k, y_k = direction[d_i]
        n=int(step[1:])
        for i in xrange(n):
            x += x_k
            y += y_k
            if (x, y) in visited:
                print abs(x) + abs(y)
                return
            else:
                visited.add((x, y))

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        for line in inf:
            z(line)
