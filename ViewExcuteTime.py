# 将八皇后的运行时间可视化
import os
from typing import List

import matplotlib.pyplot as plt

from getConfig import getConfig


def View(X: List[int], Y: List[float]):
    # 创建折线图
    plt.plot(X, Y)
    # 添加标题和标签
    plt.title(getConfig("Solutionname") + '  n_Queens')
    plt.xlabel('number')
    plt.ylabel('Excute Time')
    # 保存图片
    save_pic_path = os.path.join(getConfig("ExcuteTimepath"), getConfig("Solutionname") + "TimeChart.png")
    plt.savefig(save_pic_path)
    # 展示
    plt.show()
