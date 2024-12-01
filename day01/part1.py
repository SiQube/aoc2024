from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    list_1, list_2 = [], []
    for line in inp.splitlines():
        s_1, s_2 = line.split()
        num_1, num_2 = int(s_1), int(s_2)
        list_1.append(num_1)
        list_2.append(num_2)

    ret = 0
    for num_1, num_2 in zip(sorted(list_1), sorted(list_2)):
        ret += abs(num_1 - num_2)

    return ret


_TESTS = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
_EXPECTED = 11


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
