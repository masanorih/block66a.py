from app.solver import blocks2, blocks4, is_valid, solve_block66a
from pprint import pformat
import pytest


def test_blocks2():
    r = blocks2(2, 1, 1)
    assert r == True, "1 + 1 = 2"
    r = blocks2(2, 1, 2)
    assert r == True, "1 * 2 = 2"
    r = blocks2(2, 3, 1)
    assert r == True, "3 - 1 = 2"
    r = blocks2(2, 6, 3)
    assert r == True, "6 / 3 = 2"
    r = blocks2(-2, 3, 1)
    assert r == True, "1 - 3 = -2"
    r = blocks2(-3, 2, 5)
    assert r == True, "2 - 5 = -2"


def test_blocks4():
    r = blocks4(3, [1, 1, 1])
    assert r == True, "1 + 1 + 1 = 3"
    r = blocks4(4, [1, 1, 1, 1])
    assert r == True, "1 + 1 + 1 + 1 = 4"
    r = blocks4(1, [1, 1, 1, 1])
    assert r == True, "1 * 1 * 1 * 1 = 1"
    r = blocks4(24, [2, 3, 4])
    assert r == True, "2 * 3 * 4 = 24"
    r = blocks4(9, [2, 3, 4])
    assert r == True, "2 + 3 + 4 = 9"
    r = blocks4(2, [5, 1, 2])
    assert r == False, "5 - 1 - 2 = 2 だけど差は認められていない"


def test_is_valid():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    # fmt:off
    conditions = [
        {"n":  3, "points": [ {"y":0, "x":0}, {"y":0, "x":1}]},
    ]
    # fmt:on
    r = is_valid(grid, 0, 0, 1, conditions)
    assert r == True, "y=0, x=0 に 1 は置ける"

    # 上に続いて、次のマスを埋める
    grid = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    r = is_valid(grid, 0, 1, 1, conditions)
    assert r == False, "y=0, x=1 に 1 は置けない"
    r = is_valid(grid, 0, 1, 2, conditions)
    assert r == True, "y=0, x=1 に 2 は置ける"

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    r = is_valid(grid, 5, 5, 1, conditions)
    assert r == True, "y=5, x=5 に 1 は置ける"
    r = is_valid(grid, 5, 5, 2, conditions)
    assert r == True, "y=5, x=5 に 2 も置ける"

    # fmt:off
    conditions = [
        {"n":  3, "points": [ {"y":5, "x":4}, {"y":5, "x":5}]},
    ]
    # fmt:on
    r = is_valid(grid, 5, 4, 1, conditions)
    assert r == True, "y=5, x=4 に 1 は置ける"
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0],
    ]
    # print(pformat(grid))
    r = is_valid(grid, 5, 5, 1, conditions)
    assert r == False, "y=5, x=5 に 1 は置けない"
    r = is_valid(grid, 5, 5, 2, conditions)
    assert r == True, "y=5, x=5 に 2 は置ける"


def test_solve_block66a():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    # fmt:off
    conditions = [
        { "n":  3, "points": [ {"y":5, "x":4}, {"y":5, "x":5} ] },
    ]
    # fmt:on
    r = solve_block66a(grid, 0, 0, conditions, debug=False)
    assert r == True, "solve_block66a() が回答を出せる"

    # v1 = grid[5][4]  # 4
    # v2 = grid[5][5]  # 3
    # assert v1 == 10, "v1 が 10"
    # assert v2 == 10, "v1 が 10"
    r = is_valid(grid, 5, 0, 3, conditions)
    assert r == False, "y=5, x=0 に 3 は置けない"
