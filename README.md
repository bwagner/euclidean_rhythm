# Bjorklund

[https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)

Out of frustration failing to find an implementation online that generates
the exact rhythm necklaces as shown in Toussaint's paper, here goes a python
implementation that does, except for one error in Toussaint's paper, and
an apparently systematic difference when all but one are onsets:
In his rendering the one pause is indiscriminately at the 2nd position,
while the algorithm always moves the one pause to the end of the pattern.
So the difference in these cases merely consists of the necklace rotated
by two positions to the left.

# Usage

```console
./bjorklund.py onsets length
```

e.g.

```console
./bjorklund.py 3 8
```
produces:
```console
[ x . . x . . x . ]
```

There's also a script `euclidean.py` which merely produces the sequence of remainders when performing
[Euclid's Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)

# Contribute
```console
pre-commit install
```
if this fails
```
pip install pre-commit
```
(see [pre-commit](https://pre-commit.com/))
