import os.path
from typing import List

import openpyxl

from getConfig import getConfig


# X代表运行次数
# Y代表运行时间

def SaveExcuteTime(X: List[int], Y: List[float]):
    # 创建一个新的Excel工作簿
    workbook = openpyxl.Workbook()

    # 获取第一个工作表
    sheet = workbook.active

    # 写入标题
    sheet['A1'] = '次数'
    sheet['B1'] = '运行时间'

    # 存储次数和运行时间的数据
    # 将数据写入Excel表格中
    for i in range(len(X)):
        sheet.append([X[i], Y[i]])

    # 保存Excel文件
    savepath = os.path.join(getConfig("ExcuteTimepath"), getConfig("Solutionname") + "ExcuteTime.xlsx")
    workbook.save(savepath)
