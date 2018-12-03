#!/usr/bin/env python
import sys

move_table = {
    (1, 'R') : 2,
    (1, 'D') : 4,
    (2, 'L') : 1,
    (2, 'R') : 3,
    (2, 'D') : 5,
    (3, 'L') : 2,
    (3, 'D') : 6,
    (4, 'U') : 1,
    (4, 'R') : 5,
    (4, 'D') : 7,
    (5, 'U') : 2,
    (5, 'L') : 4,
    (5, 'R') : 6,
    (5, 'D') : 8,
    (6, 'U') : 3,
    (6, 'L') : 5,
    (6, 'D') : 9,
    (7, 'U') : 4,
    (7, 'R') : 8,
    (8, 'U') : 5,
    (8, 'L') : 7,
    (8, 'R') : 9,
    (9, 'U') : 6,
    (9, 'L') : 8
}

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        n = 5
        for line in inf:
            for c in line.strip():
                k = n, c
                if k in move_table:
                    n = move_table[k]
            print n
