#!/usr/bin/env python

import sys

"""
Unused for bjorklund. Just for showing the sequence
of remainders when performing Euclid's algorithm.
"""


def euclid_seq(n, k, s=None):
    if s is None:
        s = []
    return s[1:] if k == 0 else euclid_seq(k, n % k, s + [k])


def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(euclid_seq(n, k))


if __name__ == "__main__":
    main()
