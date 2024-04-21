"""
棋盘摆布
****Q****
**Q******
Q********
类似于这样

"""
import copy
from typing import List

"""
Solution1:基于递归的n皇后摆布（暴力枚举法）
1、逐行遍历棋盘，在每个格子都尝试摆放皇后
def put(row: int):

2、摆放之后遍历整个棋盘，判断是否有摆放冲突，如果没有则继续下一行的遍历，有则停止
def conflict(board: List[List[str]], row: int, column: int):

3、遍历该列的每一格，直到所有都遍历完才结束

时间复杂度O(n^2*n^n)，及其大，不适合实际运用

"""

# queen的表示图标
# 空格的表示图标
queen_config = "Q"
space_config = "#"


# 判断摆布的位置是否会与其他皇后发生冲突
def conflict(board: List[List[str]], row: int, column: int):
    # 发生冲突的条件:row+column相同位置摆放有皇后,fabs(row-column)相同位置摆放有皇后
    # 或者相同row的地方摆放有皇后，相同column的地方摆放有皇后
    n = len(board)
    # 整个棋盘遍历
    for i in range(n):
        for j in range(n):
            if i == row or j == column or i + j == row + column or i - j == row - column:
                # 真的摆放有皇后
                if board[i][j] == queen_config:
                    return True
    # 没有摆放皇后
    return False


def n_Queen(n: int):
    if n == 0:
        return []

    # 创建棋盘
    board = [[space_config] * n for _ in range(n)]
    # 储存摆放的结果
    result = []

    def put(row: int):
        # 可以完成遍历棋盘摆放皇后
        if row == n:
            result.append(copy.deepcopy(board))
            return

        for i in range(n):
            # 如果不发生冲突则摆放
            if not conflict(board, row, i):
                board[row][i] = queen_config
                # 继续下一个摆放
                put(row + 1)
                board[row][i] = space_config

    put(0)
    return result


# 跑动整个算法
def Run(i: int):
    return n_Queen(i)
