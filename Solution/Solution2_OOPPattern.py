"""

采用面向对象的设计模式:
Board 类：创建一个 Board 类来表示国际象棋棋盘，该类包括方法来放置和移除皇后，以及检查皇后之间的冲突。

Queen 类：创建一个 Queen 类来表示皇后对象。这个类应该包括皇后的位置信息

Solution 类：创建一个 Solution 类来实现八皇后问题的解决算法。这个类应该包括递归函数或迭代函数，用于尝试放置皇后，并检查是否有冲突

FormatResult 脚本:格式化棋盘输出

Main 脚本：创建一个 Main 脚本，用于初始化棋盘、调用求解器并展示解决方案。


"""
import copy
from typing import List


class Queen:
    def __init__(self, i: int, j: int):
        self.row = i
        self.column = j


# 在board class中存放棋盘以及摆放皇后之后的位置,并且可用判断是否存在conflict
class Board:
    def __init__(self, n: int):
        # 初始化棋盘大小
        self.board_size = n
        # 初始化棋盘，存放Queen
        self.board = []
        # 均使用set记录
        # 记录已经存放column的位置
        self.column = set()
        # 记录左上右下对角线已经存放皇后的位置
        self.diagonal_cut = set()
        # 记录左下右上对角线已经存放皇后的位置
        self.diagonal_add = set()

    # 检测是否发生冲突
    def conflict(self, currentqueen: Queen) -> bool:
        # 如果与之前摆放的皇后有发生冲突
        if currentqueen.column in self.column or currentqueen.row - currentqueen.column in self.diagonal_cut or currentqueen.column + currentqueen.row in self.diagonal_add:
            return True
        else:
            return False


class Solution:
    # queen的表示图标
    # 空格的表示图标

    def n_Queen(self, myboard: Board) -> List[Board]:
        # 如果当前棋盘大小为0,则直接返回
        if myboard.board_size == 0:
            return []

        # 储存摆放的结果
        result = []

        # 递归式摆放
        def put(row: int):
            # 可以完成遍历棋盘摆放皇后
            if row == myboard.board_size:
                result.append(copy.deepcopy(myboard))
                return

            # 逐列遍历
            for column in range(myboard.board_size):
                # 创建一个临时的皇后变量
                tempqueen = Queen(row, column)
                # 如果发生冲突则跳过
                if myboard.conflict(tempqueen):
                    continue
                # 否则则摆放皇后并且记录
                else:
                    myboard.column.add(column)
                    myboard.diagonal_cut.add(row - column)
                    myboard.diagonal_add.add(row + column)
                    myboard.board.append(tempqueen)
                    # 继续下一列摆放
                    put(row + 1)
                    # 还原
                    myboard.column.remove(column)
                    myboard.diagonal_cut.remove(row - column)
                    myboard.diagonal_add.remove(row + column)
                    myboard.board.pop()

        put(0)
        return result


# 将结果格式化为棋盘字符串输出
def FormatResult(result: List[Board], size: int) -> List[List[List[str]]]:
    # queen的表示图标
    # 空格的表示图标
    queen_config = "Q"
    space_config = "#"
    newFormattedREsult = []
    # 格式化相关解法
    for every in result:
        current = [[space_config] * size for _ in range(size)]
        for queen in every.board:
            current[queen.row][queen.column] = queen_config
        newFormattedREsult.append(current)
    return newFormattedREsult


def Main(i: int):

    # 创建棋盘
    board = Board(i)
    # 解法调用
    mysolution = Solution()
    result = mysolution.n_Queen(board)
    # 返回格式化的结果
    return FormatResult(result, i)


# 跑动整个算法
def Run(i: int):
    return Main(i)
