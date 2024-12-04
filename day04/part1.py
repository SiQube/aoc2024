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

    def check_X(self, cur_x: int, cur_y: int) -> bool:
        if self.grid[(cur_y, cur_x)] == 'X':
            return True
        return False

    def check_right(self, cur_x: int, cur_y: int) -> int:
        if cur_x + 3 < self.max_x:
            if (
                self.grid[(cur_y, cur_x + 1)] == 'M' and
                self.grid[(cur_y, cur_x + 2)] == 'A' and
                self.grid[(cur_y, cur_x + 3)] == 'S'
            ):
                return 1
        return 0

    def check_left(self, cur_x: int, cur_y: int) -> int:
        if cur_x - 3 >= 0:
            if (
                self.grid[(cur_y, cur_x - 1)] == 'M' and
                self.grid[(cur_y, cur_x - 2)] == 'A' and
                self.grid[(cur_y, cur_x - 3)] == 'S'
            ):
                return 1
        return 0

    def check_up(self, cur_x: int, cur_y: int) -> int:
        if cur_y - 3 >= 0:
            if (
                self.grid[(cur_y - 1, cur_x)] == 'M' and
                self.grid[(cur_y - 2, cur_x)] == 'A' and
                self.grid[(cur_y - 3, cur_x)] == 'S'
            ):
                return 1
        return 0

    def check_down(self, cur_x: int, cur_y: int) -> int:
        if cur_y + 3 < self.max_y:
            if (
                self.grid[(cur_y + 1, cur_x)] == 'M' and
                self.grid[(cur_y + 2, cur_x)] == 'A' and
                self.grid[(cur_y + 3, cur_x)] == 'S'
            ):
                return 1
        return 0

    def check_diag_top_left(self, cur_x: int, cur_y: int) -> int:
        if (cur_y - 3 >= 0 and cur_x - 3 >= 0):
            if (
                self.grid[(cur_y - 1, cur_x - 1)] == 'M' and
                self.grid[(cur_y - 2, cur_x - 2)] == 'A' and
                self.grid[(cur_y - 3, cur_x - 3)] == 'S'
            ):
                return 1
        return 0

    def check_diag_top_right(self, cur_x: int, cur_y: int) -> int:
        if (cur_y - 3 >= 0 and cur_x + 3 < self.max_x):
            if (
                self.grid[(cur_y - 1, cur_x + 1)] == 'M' and
                self.grid[(cur_y - 2, cur_x + 2)] == 'A' and
                self.grid[(cur_y - 3, cur_x + 3)] == 'S'
            ):
                return 1
        return 0

    def check_diag_bottom_left(self, cur_x: int, cur_y: int) -> int:
        if (cur_y + 3 < self.max_y and cur_x - 3 >= 0):
            if (
                self.grid[(cur_y + 1, cur_x - 1)] == 'M' and
                self.grid[(cur_y + 2, cur_x - 2)] == 'A' and
                self.grid[(cur_y + 3, cur_x - 3)] == 'S'
            ):
                return 1
        return 0

    def check_diag_bottom_right(self, cur_x: int, cur_y: int) -> int:
        if (cur_y + 3 < self.max_y and cur_x + 3 < self.max_x):
            if (
                self.grid[(cur_y + 1, cur_x + 1)] == 'M' and
                self.grid[(cur_y + 2, cur_x + 2)] == 'A' and
                self.grid[(cur_y + 3, cur_x + 3)] == 'S'
            ):
                return 1
        return 0


def _solve(inp: str) -> int:
    result = 0
    grid = construct_grid(inp)
    for y in range(grid.max_y):
        for x in range(grid.max_x):
            if grid.check_X(x, y):
                result += grid.check_right(x, y)
                result += grid.check_left(x, y)
                result += grid.check_up(x, y)
                result += grid.check_down(x, y)
                result += grid.check_diag_top_left(x, y)
                result += grid.check_diag_top_right(x, y)
                result += grid.check_diag_bottom_left(x, y)
                result += grid.check_diag_bottom_right(x, y)

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
_EXPECTED = 18


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
