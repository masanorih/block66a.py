from app.solver import solve_block66a
from datetime import datetime
from pprint import pformat

# 発生した backtrack の回数を保存する
# backtracks = 0
# grid の初期状態
input_grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# XXX ここに問題特有の条件を書いていけばよい XXX
# fmt:off
input_conditions = [
    { "n":  5, "points": [ {"y":0, "x":0}, {"y":1, "x":0} ] },
    { "n":  3, "points": [ {"y":0, "x":1}, {"y":1, "x":1} ] },
    { "n":  2, "points": [ {"y":0, "x":4}, {"y":0, "x":5} ] },
    { "n": 25, "points": [ {"y":1, "x":4}, {"y":1, "x":5}, {"y":2, "x":5} ] },
    { "n":  2, "points": [ {"y":2, "x":0}, {"y":2, "x":1} ] },
    { "n": -5, "points": [ {"y":2, "x":2}, {"y":3, "x":2} ] },
    { "n": -2, "points": [ {"y":2, "x":3}, {"y":2, "x":4} ] },
    { "n": 18, "points": [ {"y":3, "x":0}, {"y":3, "x":1} ] },
    { "n": -3, "points": [ {"y":3, "x":3}, {"y":3, "x":4} ] },
    { "n":  9, "points": [ {"y":3, "x":5}, {"y":4, "x":4}, {"y":4, "x":5} ] },
    { "n": -2, "points": [ {"y":4, "x":0}, {"y":5, "x":0} ] },
    { "n": -4, "points": [ {"y":4, "x":1}, {"y":5, "x":1} ] },
    { "n": -2, "points": [ {"y":5, "x":4}, {"y":5, "x":5} ] },
]
# fmt:on

start = datetime.now()
solve_block66a(grid=input_grid, y=0, x=0, conditions=input_conditions, debug=True)
end = datetime.now()
diff = end - start
print(f"time={diff}")
