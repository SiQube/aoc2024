from __future__ import annotations

import os.path

import numpy as np
import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    result = 0
    for line in inp.splitlines():
        levels = np.array(line.split(), dtype=int)
        diffs = levels[1:] - levels[:-1]
        if (
            (
                (sum(diffs > 0) == len(diffs)) and
                min(diffs) >= 0 and
                max(diffs) <= 3
            )
            or
            (
                (sum(diffs < 0) == len(diffs)) and
                min(abs(diffs)) >= 0 and
                max(abs(diffs)) <= 3
            )
        ):
            result += 1

    return result


_TESTS = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
_EXPECTED = 2


@pytest.mark.parametrize(
    ('input_str', 'expected'),
    (
        (_TESTS, _EXPECTED),
    ),
)
def test(input_str: str, expected: int) -> None:
    assert _solve(input_str) == expected


def main() -> int:
    with open(_INPUT) as fp:
        print(_solve(fp.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
