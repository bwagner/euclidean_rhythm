#!/usr/bin/env python

"""
https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf

Out of frustration failing to find an implementation online that generates
the exact rhythm necklaces as shown in Toussaint's paper, here goes a python
implementation that does, except for one error in Toussaint's paper, and
an apparently systematic difference when all but one are onsets:
In his rendering the one pause is indiscriminately at the 2nd position,
while the algorithm always moves the one pause to the end of the pattern.
So the difference in these cases merely consists of the necklace rotated
by two positions to the left.
"""


def bjorklund(k, n):
    if k >= n:
        raise TypeError(f"k ({k}) must be < n ({n})")
    start = [[1] for _ in range(k)]
    remainder = [[0] for _ in range(n - k)]
    while (lr := len(remainder)) > 1:
        for i in range(min(len(start), lr)):
            start[i].extend(remainder.pop(0))
        if not remainder:
            start, remainder = start[:lr], start[lr:]
    return [x for sl in start + remainder for x in sl]


def bjorklund2str(pattern):
    return "[ " + "".join(["x " if x else ". " for x in pattern]) + "]"


def str2bjorklund(str):
    return [1 if x == "x" else 0 for x in (str.strip("[ ]").split())]


if __name__ == "__main__":
    import sys

    def main():
        k = int(sys.argv[1])
        n = int(sys.argv[2])
        print(bjorklund2str(bjorklund(k, n)))

    main()
