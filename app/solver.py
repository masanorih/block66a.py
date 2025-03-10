from pprint import pformat

backtracks = 0


def find_next_cell(grid):
    """find_next_cell
    引数 grid から値が 0 の 座標を探してその座標(x, y) を返す
    前提条件として、grid には数字が未決定の場所には 0 が入っている
    この関数が grid の値を直接書き換えることはない
    Args:
        grid: List[List[int]]
            座標の値を示すリスト
    Returns:
        y: 数字
            発見した y 座標
        x: 数字
            発見した x 座標
    Raises:
        なし
    """
    for y in range(6):
        for x in range(6):
            if grid[y][x] == 0:
                # 0 を見つけた grid の座標を返す
                return y, x
    # すべてのマスに数字が入っている状態
    return -1, -1


def is_valid(grid, y, x, value, conditions):
    """is_valid
    入力値が数独の条件を満たしているかどうかを返す
    以下の3つの値が全て真なら真を返す
        is_row: y の同一横軸上に同一の数字が存在しないこと
        is_column: x の同一縦軸上に同一の数字が存在しないこと
        is_block: y, x の所属してるブロック状に同一の数字が存在しないこと
    Args:
        grid: List[List[int]]
            座標の値を示すリスト
        y: 数字
            対象の y 座標
        x: 数字
            対象の x 座標
        conditions: List[dict{}]
            問題固有の条件が記述されたリスト
        value: 数字
            1-9 までの数字
    Returns: boolean
        True: 値は設置可能
        False: 値は設置不可能
    Raises:
        なし
    """
    # 行に value と同じ数字がないことを確認
    is_row = value not in grid[y]
    if not is_row:
        # print(f"is_row is False. value={value}")
        return False
    # 列に value と同じ数字がないことを確認
    is_column = value not in [i[x] for i in grid]
    if not is_column:
        # print(f"is_column is False. value={value}")
        return False

    # ここで値を変更して、ダメなら is_valid で 0 に戻す
    grid[y][x] = value
    for c in conditions:
        ok = valid_condition(grid, c)
        if not ok:
            # print(f"valid_condition is False. value={value}")
            return False

    # print(pformat(grid))
    # print(f"is_valid ok. value={value}")
    return True


def get_value_of_point(grid, point):
    """get_value_of_point
    grid の一点の値を取得して返す
    Args:
        grid: List[List[int]]
            座標を示すリスト
        point: Dict
            y: y座標
            x: x座標
    Returns: 数字
        grid の y, x 地点に設定されている値
    Raises:
        なし
    """
    y = point["y"]
    x = point["x"]
    return grid[y][x]


def valid_condition(grid, condition):
    """valid_condition
    grid を条件(condition)毎にチェックする
    Args:
        grid: List[List[int]]
            座標の値を示すリスト
        conditions: List[dict{}]
            問題固有の条件が記述されたリスト
    Returns: boolean
        True:  条件が真
        False: 条件が真ではない
    Raises:
        なし
    """
    n = condition["n"]
    points = condition["points"]
    plen = len(points)
    if plen == 2:
        a = get_value_of_point(grid, points[0])
        b = get_value_of_point(grid, points[1])
        return blocks2(n, a, b)
    else:
        values = []
        for p in points:
            v = get_value_of_point(grid, p)
            values.append(v)
        return blocks4(n, values)


def blocks2(n, a, b: int):
    """blocks2
    grid 上の 2つのブロックの和差商積が n と成りうるかどうかを返す。
    いづれかの条件を満たすなら True が返る
    Args:
        n: 数字
            和差商積の結果として期待される数
        a: 数字
            ブロックの値その1
        b: 数字
            ブロックの値その2
    Returns: boolean
        True:  n となりうる
        False: n となりえない
    Raises:
        なし
    """

    # 値 0 は未処理なので True を返す
    if a == 0:
        return True
    if b == 0:
        return True

    # n が負の数の時は差のみ
    if n < 0:
        # 差
        if n == a - b:
            return True
        if n == b - a:
            return True
        return False

    # 和
    if n == a + b:
        return True
    # 差
    if n == a - b:
        return True
    if n == b - a:
        return True
    # 商
    if n == a / b:
        return True
    if n == b / a:
        return True
    # 積
    if n == a * b:
        return True
    # いづれも該当しないなら False
    return False


def blocks4(n, values):
    """blocks4
    grid 上の 3 or 4つのブロックの和積が n と成りうるかどうかを返す。
    いづれかの条件を満たすなら True が返る
    Args:
        n: 数字
            和積の結果として期待される数
        values: List[int]
            計算対象の数字のリスト
    Returns: boolean
        True:  n となりうる
        False: n となりえない
    Raises:
        なし
    """
    sums = 0
    multi = 1
    # for p in points:
    for v in values:
        # 値 0 は未処理なので True を返す
        if v == 0:
            return True
        sums += v
        multi *= v
    # 和
    if n == sums:
        return True
    # 積
    if n == multi:
        return True
    # いづれも該当しないなら False
    return False


def show_progress(grid):
    global backtracks
    # clear terminal output
    print("\033[H\033[J", end="")
    print(pformat(grid))
    print(f"backtracks={backtracks}")


def solve_block66a(grid, y, x, conditions, debug=False):
    """solve_block66a
    数独を解決する
    Args:
        grid: List[List[int]]
            座標の値を示すリスト
        y: 数字
            走査中の y 座標
        x: 数字
            走査中の x 座標
        conditions: List[dict{}]
            問題固有の条件が記述されたリスト
        debug: boolean
            debug 出力を行うかどうかの bool 値
    Returns: boolean
        True: 走査終了
        False: 走査継続
    Raises:
        なし
    """
    if debug:
        show_progress(grid)
    global backtracks
    y, x = find_next_cell(grid)
    # 終了判定(find_next_cell が -1 を返したら終了)
    if y == -1 or x == -1:
        return True

    # 入力
    for value in range(1, 7):
        if is_valid(grid, y, x, value, conditions):
            # grid[y][x] = value
            # 次へ
            if solve_block66a(grid, y, x, conditions, debug):
                return True
            backtracks += 1
            # 解決しなかったら、その座標の値を 0 にする
            # print("before backtrack")
            # print(f"y={y}, x={x}")
            # print(pformat(grid))
            grid[y][x] = 0
            # print("after backtrack")
            # print(pformat(grid))
        else:
            grid[y][x] = 0

    return False
