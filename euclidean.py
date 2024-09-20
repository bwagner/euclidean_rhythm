#!/usr/bin/env python

import sys


def euclid_seq(n, k, s=None):
    if s is None:
        s = []
    if k == 0:
        return s[1:]  # we don't want the first which is always n
    return euclid_seq(k, n % k, s + [k])


def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(euclid_seq(n, k))


if __name__ == "__main__":
    main()
