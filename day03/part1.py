from __future__ import annotations

import os.path
import re

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    result = 0
    for line in inp.splitlines():
        for mult in re.finditer(r'mul\((?P<num1>\d+),(?P<num2>\d+)\)', line):
            result += int(mult.group('num1')) * int(mult.group('num2'))

    return result


_TESTS = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
_EXPECTED = 161


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
