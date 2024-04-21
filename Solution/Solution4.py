"""
棋盘摆布
****Q****
**Q******
Q********
类似于这样

"""
import copy

"""
Solution4:基于迭代的n皇后解法---相较于Solution2的递归改进

使用递归的方法往往会使程序运行速度更慢
若改用迭代的方法运行程序，可能可以使程序运行更快些

idea:
通过一个数组position[]记录每次摆放时当前列的皇后的位置
position的下标表示所处行的位置

只要逐行遍历即可

"""

# queen的表示图标
# 空格的表示图标
queen_config = "Q"
space_config = "#"


def n_Queen(n: int):
    if n == 0:
        return []

    # 创建棋盘
    board = [[space_config] * n for _ in range(n)]
    # 储存摆放的结果
    result = []

    # 均使用set记录
    # 记录已经存放column的位置
    column = set()
    # 记录左上右下对角线已经存放皇后的位置
    diagonal_cut = set()
    # 记录左下右上对角线已经存放皇后的位置
    diagonal_add = set()

    # position记录每行皇后的列的摆放位置
    # 其下标表示当前行所在列的位置
    position = [0] * n

    # 当前行所在的位置
    row = 0
    while row >= 0:

        # 如果顺利到达第n行
        if row == n:
            # 将结果添加
            result.append(copy.deepcopy(board))
            # 往回走一行
            row -= 1
        else:
            # 逐列遍历
            if 0 <= position[row] < n:
                # 如果遇到无法摆放的情况
                if position[row] in column or row - position[row] in diagonal_cut or row + position[row] in diagonal_add:
                    position[row] += 1
                    continue
                else:
                    # 将当前行放置皇后并且遍历到下一行
                    column.add(position[row])
                    diagonal_cut.add(row - position[row])
                    diagonal_add.add(row + position[row])
                    board[row][position[row]] = queen_config
                    row += 1
                    continue
            else:
                # 如果发生了列的越界
                # 重置当前行
                position[row] = 0
                # 向上移动一行
                row -= 1

        # 最后如果没有发生行的越界
        if row >= 0:
            # 将当前行重置位置，并且去除相关的column,diagonal_cut,diagonal_add
            column.remove(position[row])
            diagonal_cut.remove(row - position[row])
            diagonal_add.remove(row + position[row])
            board[row][position[row]] = space_config
            # 将上一行的列+1进行遍历
            position[row] += 1

    return result


# 跑动整个算法
def Run(i: int):
    return n_Queen(i)
