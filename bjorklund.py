#!/usr/bin/env python

"""
https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf

Failing to find an implementation online that generates the exact
rhythm necklaces as shown in Toussaint's paper, here goes a python
implementation that does, except for one error in Toussaint's paper,
and an apparently systematic difference when all but one beat are onsets:
In his rendering the one rest is indiscriminately at the 2nd position,
while the algorithm always places the one rest at the end of the pattern.
So, the difference in these cases merely consists of the necklace rotated
by two positions to the left.
"""


def bjorklund(k, n):
    """Creates a rhythmic pattern based on the Bjorklund algorithm.

    Generates a rhythm by distributing a specified number of beats (k) across a
    total number of steps (n). The resulting pattern is returned as a list of ints
    1 (onset) and 0 (rest).

    Args:
        k (int): The number of beats to distribute in the rhythm.
        n (int): The total number of steps of the rhythm.

    Returns:
        list: A list of 1s and 0s representing the generated rhythm pattern,
        1 being an onset, 0 being rest.


    Raises:
        TypeError: If k is greater than n.

    Examples:
        >>> bjorklund(3, 8)
        [1, 0, 0, 1, 0, 0, 1, 0]
    """
    if k > n:
        raise TypeError(f"k ({k}) must be <= n ({n})")
    start = [[1] for _ in range(k)]
    remainder = [[0] for _ in range(n - k)]
    while (lr := len(remainder)) > 1:
        for i in range(min(len(start), lr)):
            start[i].extend(remainder.pop(0))
        if not remainder:
            start, remainder = start[:lr], start[lr:]
    return [x for sl in start + remainder for x in sl]


def bjorklund2str(pattern):
    """Convert a binary pattern into a string representation.

    This function takes a list of values 1 and 0 and transforms it into a
    formatted string, where 'x' represents a 1 (onset) and '.' represents a 0 (rest).

    Args:
        pattern (list of int): A list containing int values (1 or 0).

    Returns:
        str: A string representation of the binary pattern, formatted with 'x' and '.'.
    """
    return "[ " + "".join(["x " if x else ". " for x in pattern]) + "]"


def str2bjorklund(str):
    """
    Convert a string representation of a Bjorklund rhythm into a list of integers.
    The function interprets 'x' as 1 (onset) and any other character as 0 (rest).

    Args:
        str (str): A string containing characters 'x' and '.', representing rhythm
        of onsets and rests.

    Returns:
        list: A list of integers where 'x' is represented as 1 and all other characters as 0.

    Examples:
        >>> str2bjorklund("[ x x . ]")
        [1, 1, 0]
    """
    return [1 if x.lower() == "x" else 0 for x in (str.strip("[ ]").split())]


if __name__ == "__main__":
    import sys

    def main():
        k = int(sys.argv[1])
        n = int(sys.argv[2])
        print(bjorklund2str(bjorklund(k, n)))

    main()
