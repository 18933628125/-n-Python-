"""
棋盘摆布
****Q****
**Q******
Q********
类似于这样

"""
import copy
import math

"""
Solution3:基于位运算的n皇后解法---相较于Solution1的conflict改进
有三个二进制位column,diagonal_cut,diagonal_add，分别代表同一列，左上右下，左下右上的位置是否可放置八皇后
如果bit位为1，则无法放置
逐行遍历：
column保持不变
diagonal_add向左移动一位
diagonal_cut向右移动一位

三者取或可以排除不可选的位置，直到找到合适的位置并且放置皇后

附：
x&(x-1)取到最低位的1
可以通过((1<<n)-1)&x来计算当前bit位情况

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

    # 分别记录当前对角线状态
    def put(row: int, column: int, diagonal_add: int, diagonal_cut: int):
        # 可以完成遍历棋盘摆放皇后
        if row == n:
            result.append(copy.deepcopy(board))
            return

        # 这个是可以放置的位置
        available = ((1 << n) - 1) & (~(column | diagonal_add | diagonal_cut))
        while available:
            # 用x&(-x+1)取最低位
            currentput = available & (~available + 1)
            column |= currentput
            diagonal_add |= currentput
            diagonal_cut |= currentput
            board[row][int(math.log2(currentput))] = queen_config
            # column不变，diagonal_add左移一位，diagonal_cut右移一位
            put(row + 1, column, diagonal_add << 1, diagonal_cut >> 1)
            # 复原
            column -= currentput
            diagonal_add ^= currentput
            diagonal_cut ^= currentput
            board[row][int(math.log2(currentput))] = space_config
            # available遍历下一个
            # 用x&(x-1)逐项遍历
            available &= (available - 1)

    """
    用bit位记录已经存放column的位置
    column = 0
    用bit位记录左上右下对角线已经存放皇后的位置
    diagonal_cut = 0
    用bit位记录左下右上对角线已经存放皇后的位置
    diagonal_add = 0
    """
    put(0, 0, 0, 0)
    return result


def Run(i: int):
    return n_Queen(i)
