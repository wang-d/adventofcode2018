#!/usr/bin/env python
import sys

keypad = [
    "  1",
    " 234",
    "56789",
    " ABC",
    "  D"
    ]

move_table = { 'U' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1), 'D' : (1, 0) }

if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        r, c = 2, 0
        assert ('5' == keypad[r][c])
        for line in inf:
            for move in line.strip():
                r_k, c_k = move_table[move]
                r2 = r + r_k
                c2 = c + c_k
                try:
                    assert (r2 >= 0)
                    assert (c2 >= 0)
                    assert (' ' != keypad[r2][c2])
                    r, c = r2, c2
                except:
                    pass
            print keypad[r][c]
