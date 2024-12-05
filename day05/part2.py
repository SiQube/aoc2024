from __future__ import annotations

import math
import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    rules, updates = inp.split('\n\n')
    rulebook: dict[str, list[str]] = {}
    for rule in rules.splitlines():
        key, value = rule.split('|')
        if key in rulebook:
            rulebook[key].append(value)
        else:
            rulebook[key] = [value]

    incorrect_ordering = []
    for pages_s in updates.splitlines():
        correct = True
        pages = pages_s.split(',')
        for page_id, page in enumerate(pages):
            if page in rulebook:
                for rule in rulebook[page]:
                    if rule in pages[:page_id]:
                        correct = False
                        break

        if not correct:
            incorrect_ordering.append(pages)

    result = 0
    for pages in incorrect_ordering:
        for rule, update in rulebook.items():
            for page_id, page in enumerate(pages):
                if page in rulebook:
                    for rule in rulebook[page]:
                        if rule in pages[:page_id]:
                            broken_page_id = pages.index(page)
                            broken_rule_id = pages.index(rule)
                            pages[broken_rule_id] = page
                            pages[broken_page_id] = rule

        result += int(pages[math.ceil(len(pages)//2)])
    return result


_TESTS = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
_EXPECTED = 123


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
