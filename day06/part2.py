from __future__ import annotations

import os.path
from typing import NamedTuple

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Guard(NamedTuple):
    start_pos: tuple[int, int]
    cur_pos: tuple[int, int]

    def get_direction(self, direction_s: str) -> tuple[int, int]:
        if direction_s == 'v':
            direction = (1, 0)
        elif direction_s == '>':
            direction = (0, 1)
        elif direction_s == '^':
            direction = (-1, 0)
        elif direction_s == '<':
            direction = (0, -1)

        return direction

    def move_forward(self, direction_s: str, grid: Grid):
        direction = self.get_direction(direction_s)
        new_pos = (
            self.cur_pos[0] + direction[0],
            self.cur_pos[1] + direction[1],
        )
        if grid.grid[new_pos] == '#':
            direction_s = self.turn_right(direction_s)
            grid.grid[self.cur_pos] = direction_s
            return grid, self.cur_pos, direction_s

        grid.grid[new_pos] = direction_s
        grid.grid[self.cur_pos] = '.'

        return grid, new_pos, direction_s

    def turn_right(self, direction_s):
        if direction_s == '^':
            return '>'
        elif direction_s == '>':
            return 'v'
        elif direction_s == 'v':
            return '<'
        elif direction_s == '<':
            return '^'


class Grid(NamedTuple):
    grid: dict[tuple[int, int], str]
    max_x: int
    max_y: int

    def print_grid(self):
        print('\n\n')
        for y in range(self.max_y):
            for x in range(self.max_x):
                print(self.grid[(y, x)], end='')
            print()


def get_grid_and_guard(inp) -> tuple[Grid, Guard]:
    grid_dict = {}
    for y, line in enumerate(inp.splitlines()):
        for x, sign in enumerate(line):
            grid_dict[(y, x)] = sign
            if sign == '^':
                guard = Guard((y, x), (y, x))

    return Grid(grid_dict, x, y), guard


def _check_loops(grid: Grid, guard: Guard) -> int:
    dir_s = '^'
    seen = set()
    while True:
        if (guard.cur_pos, dir_s) in seen:
            return 1
        seen.add((guard.cur_pos, dir_s))
        try:
            grid, new_guard_pos, dir_s = guard.move_forward(dir_s, grid)
        except KeyError:
            return 0
        if False:
            grid.print_grid()
        guard = guard._replace(cur_pos=new_guard_pos)


def _solve(inp: str) -> int:
    grid, guard = get_grid_and_guard(inp)
    unique_fields_visited = {guard.cur_pos}
    dir_s = '^'
    while True:
        unique_fields_visited.add(guard.cur_pos)
        try:
            grid, new_guard_pos, dir_s = guard.move_forward(dir_s, grid)
        except KeyError:
            break
        guard = guard._replace(cur_pos=new_guard_pos)

    result = 0
    for start_field in unique_fields_visited:
        guard = guard._replace(cur_pos=guard.start_pos)
        grid.grid[start_field] = '#'
        result += _check_loops(grid, guard)
        grid.grid[start_field] = '.'

    return result


_TESTS = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
_EXPECTED = 6


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
