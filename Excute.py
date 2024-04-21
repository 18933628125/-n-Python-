import os
import sys
import time

import SaveExcuteTime
import ViewExcuteTime
from PrintBoard import PrintBoard
from getConfig import getConfig


# 导入模块处理
def importmodule():
    # 将Solution文件夹添加到模块搜索路径
    solution_folder = os.path.join(os.path.dirname(__file__), getConfig("Solutiondir"))
    sys.path.append(solution_folder)

    # 获取Solution的值
    solution_name = getConfig("Solutionname")

    # 导入Solution模块
    solution_module = __import__(solution_name)
    return solution_module


def ExcuteTime():
    importmodule()
    # 记录运行时的数量与时间
    runtime = []
    counts = []
    # 设置皇后数量
    number = int(getConfig("QueenNumber"))
    # 记录开始与结束时间
    starttime = 0
    endtime = 0
    # 记录排布结果
    result = []

    # 导入相关算法模块
    mymodule = importmodule()

    for i in range(1, number + 1):
        starttime = time.time()
        # NOTE:此处选择相关算法进行计算
        # 返回的是一个三维的result
        # 一个维度是总的解法数
        # 另两个维度是棋盘摆放的方法
        result = mymodule.Run(i)
        endtime = time.time()
        # 记录运行时间
        runtime.append(endtime - starttime)
        counts.append(i)
    # 打印棋盘的结果于txt文件中
    PrintBoard(number, result, endtime - starttime)
    # 将运行时间结果保存在excel表格中
    SaveExcuteTime.SaveExcuteTime(counts, runtime)
    # 查看可视化的执行时间结果
    ViewExcuteTime.View(counts, runtime)


