"""

采用Pipe And Filter设计模式：

Data_Source类存放棋盘

Filter类用于摆放皇后以及判断皇后之间是否会发生冲突
process()函数用于处理皇后摆放位置,并且将得到的结果以编码形式返回
conflict()函数用于判断皇后之间是否发生冲突
putQueen()函数用于摆放皇后

StoreResult类用于保存成功摆放的编码结果为棋盘结果，并且最后读取结果
Store()函数将编码的结果转化为棋盘结果存储
getResult()返回棋盘结果

Solve类用于驱动管道数据流与过滤器运行，并且实现数据流之间的交互
数据源->数据过滤器->数据存储->读取结果


"""
import copy
from typing import List

# queen的表示图标
# 空格的表示图标
queen_config = "Q"
space_config = "#"


class Data_Source:
    def __init__(self, size: int):
        # 初始化创建棋盘
        self.board = [[space_config] * size for _ in range(size)]

    # 获得棋盘对象（封装性）
    def get_board(self):
        return self.board


class Filter:
    def __init__(self):
        # 均使用set记录
        # 记录已经存放column的位置
        self.__column = set()
        # 记录左上右下对角线已经存放皇后的位置
        self.__diagonal_cut = set()
        # 记录左下右上对角线已经存放皇后的位置
        self.__diagonal_add = set()
        # 存放得到结果的编码
        self.process_result = []

    # 判断是否发生冲突
    def __conflict(self, currentRow: int, currentColumn: int) -> bool:
        if currentColumn in self.__column or currentRow - currentColumn in self.__diagonal_cut or currentRow + currentColumn in self.__diagonal_add:
            return True
        return False

    def __putQueen(self, currentRow: int, size: int, board: List[List[int]]):
        # 可以完成遍历棋盘摆放皇后
        if currentRow == size:
            # 添加进入process_result中
            self.process_result.append(copy.deepcopy(board))
            return
        # 逐列遍历
        for currentColumn in range(size):
            # 如果发生冲突则跳过
            if self.__conflict(currentRow, currentColumn):
                continue
            # 否则则摆放皇后并且记录
            else:
                self.__column.add(currentColumn)
                self.__diagonal_cut.add(currentRow - currentColumn)
                self.__diagonal_add.add(currentRow + currentColumn)
                board.append([currentRow, currentColumn])
                # 继续下一个摆放
                self.__putQueen(currentRow + 1, size, board)
                self.__column.remove(currentColumn)
                self.__diagonal_cut.remove(currentRow - currentColumn)
                self.__diagonal_add.remove(currentRow + currentColumn)
                board.pop()

    def process(self, data: Data_Source):
        # 获得棋盘大小
        n = len(data.get_board())
        # 如果为空棋盘，则直接返回空结果
        if n == 0:
            return []
        self.__putQueen(0, n, [])
        return self.process_result


class StoreResult:
    def __init__(self):
        self.result = []

    # 将编码的结果转化为字符化棋盘摆放
    def Store(self, data: List[List[int]]):
        # 如果结果为空，则直接返回
        if not data:
            return self.result
        for every in data:
            # 从数据源上初始化创建棋盘
            myboard = Data_Source(len(data[0]))
            for queen in every:
                row = queen[0]
                column = queen[1]
                myboard.get_board()[row][column] = queen_config
            self.result.append(myboard.get_board())

    # 返回整个棋盘的结果
    def getResult(self):
        return self.result


class Solve:
    def Pipe_And_Filter_Driver(self, size: int):
        # 创建棋盘
        data = Data_Source(size)
        # 创建过滤器
        filter = Filter()
        # 创建存储器
        store = StoreResult()
        # 获取filter处理后的结果
        result = filter.process(data)
        # 将结果存储在store中
        store.Store(result)
        # 返回该结果
        return store.getResult()


# 跑动整个算法
def Run(i: int):
    # 创建驱动器
    solve = Solve()
    return solve.Pipe_And_Filter_Driver(i)
