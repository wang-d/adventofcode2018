#!/usr/bin/env python
import sys

if __name__ == '__main__':
    a={}
    with open(sys.argv[1]) as inf:
        for w in inf:
            w=w.strip()
            for i in xrange(len(w)):
                k=(w[:i],w[i + 1:])
                if k in a:
                    print k[0] + k[1]
                    exit(0)
                a[k] = w
