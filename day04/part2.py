from __future__ import annotations

import os.path
from typing import NamedTuple

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def construct_grid(inp: str) -> Grid:
    grid_dict = {}
    for y, line in enumerate(inp.splitlines()):
        for x, letter in enumerate(line):
            grid_dict[(int(y), int(x))] = letter

    return Grid(grid_dict, x + 1, y + 1)


class Grid(NamedTuple):
    grid: dict[tuple[int, int], str]
    max_x: int
    max_y: int

    def check_A(self, cur_x: int, cur_y: int) -> bool:
        if self.grid[(cur_y, cur_x)] == 'A':
            return True
        return False

    def check_top_left(self, cur_x: int, cur_y: int, letter: str) -> bool:
        if self.grid[(cur_y - 1, cur_x - 1)] == letter:
            return True
        return False

    def check_top_right(self, cur_x: int, cur_y: int, letter: str) -> bool:
        if self.grid[(cur_y - 1, cur_x + 1)] == letter:
            return True
        return False

    def check_bottom_left(self, cur_x: int, cur_y: int, letter: str) -> bool:
        if self.grid[(cur_y + 1, cur_x - 1)] == letter:
            return True
        return False

    def check_bottom_right(self, cur_x: int, cur_y: int, letter: str) -> bool:
        if self.grid[(cur_y + 1, cur_x + 1)] == letter:
            return True
        return False

    def check_legit(self, cur_x: int, cur_y: int) -> int:
        if (
            cur_x - 1 >= 0 and
            cur_y - 1 >= 0 and
            cur_x + 1 < self.max_x and
            cur_y + 1 < self.max_y
        ):
            return True
        return False

    def check_two_top_m(self, cur_x: int, cur_y: int) -> int:
        if (
            self.check_top_left(cur_x, cur_y, 'M') and
            self.check_top_right(cur_x, cur_y, 'M') and
            self.check_bottom_right(cur_x, cur_y, 'S') and
            self.check_bottom_left(cur_x, cur_y, 'S')
        ):
            return 1
        return 0

    def check_two_left_m(self, cur_x: int, cur_y: int) -> int:
        if (
            self.check_top_left(cur_x, cur_y, 'M') and
            self.check_top_right(cur_x, cur_y, 'S') and
            self.check_bottom_right(cur_x, cur_y, 'S') and
            self.check_bottom_left(cur_x, cur_y, 'M')
        ):
            return 1
        return 0

    def check_two_right_m(self, cur_x: int, cur_y: int) -> int:
        if (
            self.check_top_left(cur_x, cur_y, 'S') and
            self.check_top_right(cur_x, cur_y, 'M') and
            self.check_bottom_right(cur_x, cur_y, 'M') and
            self.check_bottom_left(cur_x, cur_y, 'S')
        ):
            return 1
        return 0

    def check_two_bottom_m(self, cur_x: int, cur_y: int) -> int:
        if (
            self.check_top_left(cur_x, cur_y, 'S') and
            self.check_top_right(cur_x, cur_y, 'S') and
            self.check_bottom_right(cur_x, cur_y, 'M') and
            self.check_bottom_left(cur_x, cur_y, 'M')
        ):
            return 1
        return 0


def _solve(inp: str) -> int:
    result = 0
    grid = construct_grid(inp)
    for y in range(grid.max_y):
        for x in range(grid.max_x):
            if grid.check_legit(x, y) and grid.check_A(x, y):
                result += grid.check_two_top_m(x, y)
                result += grid.check_two_left_m(x, y)
                result += grid.check_two_right_m(x, y)
                result += grid.check_two_bottom_m(x, y)

    return result


_TESTS = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
_EXPECTED = 9


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
