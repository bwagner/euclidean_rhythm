#!/usr/bin/env python
import pytest

from bjorklund import bjorklund, bjorklund2str, str2bjorklund


@pytest.mark.parametrize(
    "k, n, expected",
    [
        (1, 2, "[x .]"),
        (1, 3, "[x . .]"),
        (1, 4, "[x . . . ]"),
        (4, 12, "[x . . x . . x . . x . .]"),
        (2, 3, [1, 1, 0]),  # but Toussaint says  "[x . x]"
        (2, 5, "[x . x . .]"),
        (3, 4, [1, 1, 1, 0]),  # but Toussaint says 1 0 1 1
        (3, 5, "[x . x . x]"),
        (3, 7, "[x . x . x . .]"),
        (3, 8, "[x . . x . . x .]"),  # tresillo
        (4, 7, "[x . x . x . x]"),
        (4, 9, "[x . x . x . x . .]"),
        (4, 11, "[x . . x . . x . . x .]"),
        (5, 6, [1, 1, 1, 1, 1, 0]),  # but Toussaint says 1 0 1 1 1 1
        (5, 7, "[x . x x . x x]"),
        (5, 8, "[x . x x . x x .]"),  # cinquillo
        (5, 9, "[x . x . x . x . x]"),
        (5, 11, "[x . x . x . x . x . .]"),
        (5, 12, "[x . . x . x . . x . x .]"),
        (5, 13, "[x . . x . x . . x . x . .]"),
        (
            5,
            16,
            "[x . . x . . x . . x . . x . . .]",
        ),  # error in Toussaint who has one too many
        (7, 8, [1, 1, 1, 1, 1, 1, 1, 0]),  # but Toussaint says 1 0 1 1 1 1 1 1
        (7, 12, "[x . x x . x . x x . x .]"),
        (7, 16, "[x . . x . x . x . . x . x . x .]"),
        (9, 16, "[x . x x . x . x . x x . x . x .]"),
        (11, 24, "[x . . x . x . x . x . x . . x . x . x . x . x .]"),
        (13, 24, "[x . x x . x . x . x . x . x x . x . x . x . x .]"),
        (4, 9, " [x . x . x . x . .]"),
        (3, 12, [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]),
        (4, 12, [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]),
        (5, 13, [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]),
    ],
)
def test_bjorklund(k, n, expected):
    if isinstance(expected, str):
        expected = str2bjorklund(expected)
    assert bjorklund(k, n) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, 0], "[ x . ]"),
        ([1, 0, 0], "[ x . . ]"),
        ([1, 0, 0, 0], "[ x . . . ]"),
        ([1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], "[ x . . x . x . . x . x . . ]"),
        ([1, 0, 0, 1, 0, 0, 1, 0], "[ x . . x . . x . ]"),
        ([1, 0, 1, 1, 0, 1, 1, 0], "[ x . x x . x x . ]"),
    ],
)
def test_bjorklund2str(inp, expected):
    assert bjorklund2str(inp) == expected


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (
            "[x . x x . x . x . x x . x . x .]",
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
        ),
        ("[x x x x x x x x]", [1, 1, 1, 1, 1, 1, 1, 1]),
        ("[. . . . . . . .]", [0, 0, 0, 0, 0, 0, 0, 0]),
        ("[x . x . x . x .]", [1, 0, 1, 0, 1, 0, 1, 0]),
        ("[]", []),  # Edge case: empty string inside brackets
    ],
)
def test_str2bjorklund(input_string, expected_output):
    assert str2bjorklund(input_string) == expected_output


def test_exception():
    with pytest.raises(TypeError) as e:
        bjorklund(2, 1)
    assert "k (2) must be < n (1)" in str(e.value)
