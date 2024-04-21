import copy

"""
Shared_Data_Pattern:
数据之间完全共享，没有隐私,非常危险，容易被误改


"""

# queen的表示图标
# 空格的表示图标
queen_config = "Q"
space_config = "#"
# 储存摆放的结果
result = []
# 棋盘
board = []

# 均使用set记录
# 记录已经存放column的位置
column = set()
# 记录左上右下对角线已经存放皇后的位置
diagonal_cut = set()
# 记录左下右上对角线已经存放皇后的位置
diagonal_add = set()

# 设定大小
size = 0


def put(row: int):
    # 可以完成遍历棋盘摆放皇后
    if row == size:
        result.append(copy.deepcopy(board))
        return
    # 逐列遍历
    for i in range(size):
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


def n_Queen():
    # 将global定义为全局变量
    global board, result
    if size == 0:
        return result
    # 初始化棋盘
    board = [[space_config] * size for _ in range(size)]
    put(0)
    return result


# 跑动整个算法
def Run(i: int):
    # 将size定义为全局变量
    global size
    # 设置大小
    size = i
    return n_Queen()
