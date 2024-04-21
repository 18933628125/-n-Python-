"""
棋盘摆布
****Q****
**Q******
Q********
类似于这样

"""
import copy

"""
Solution2:基于回溯的n皇后解法---相较于Solution1的conflict改进
conflict产生条件：
1、处在同一列
2、处在左上右下的斜对角线上:row-column为定值
3、处在左下右上的斜对角线上:row+column为定值

所以可以考虑采用set来存放不可放置皇后位置

时间复杂度O(n^n)
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

    def put(row: int):
        # 可以完成遍历棋盘摆放皇后
        if row == n:
            result.append(copy.deepcopy(board))
            return
        # 逐列遍历
        for i in range(n):
            # 如果发生冲突则跳过
            if i in column or row - i in diagonal_cut or row + i in diagonal_add:
                continue
            # 否则则摆放皇后并且记录
            else:
                column.add(i)
                diagonal_cut.add(row - i)
                diagonal_add.add(row + i)
                board[row][i] = queen_config
                # 继续下一个摆放
                put(row + 1)
                column.remove(i)
                diagonal_cut.remove(row - i)
                diagonal_add.remove(row + i)
                board[row][i] = space_config

    put(0)
    return result


# 跑动整个算法
def Run(i: int):
    return n_Queen(i)
