from __future__ import annotations

import itertools
import operator
import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    result = 0
    for line in inp.splitlines():
        left_side_s, right_side_s = line.split(':')
        left_side = int(left_side_s)
        _right_side = [int(num) for num in right_side_s.split()]
        possible_op = [operator.add, operator.mul, operator.concat]
        rep = len(_right_side) - 1
        for possible_comb in itertools.product(possible_op, repeat=rep):
            op_right_side_zip = zip(possible_comb, _right_side[1:])
            for op_id, (op, num) in enumerate(op_right_side_zip):
                if op_id == 0:
                    try:
                        right_side = op(_right_side[0], num)
                    except TypeError:
                        right_side = int(op(str(_right_side[0]), str(num)))
                else:
                    try:
                        right_side = op(right_side, num)
                    except TypeError:
                        right_side = int(op(str(right_side), str(num)))
                if right_side > left_side:
                    break
            if right_side == left_side:
                result += left_side
                break

    return result


_TESTS = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
_EXPECTED = 11387


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
