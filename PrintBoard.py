import os.path
from typing import List

from getConfig import getConfig


# 存储result结果到.txt文件中
def PrintBoard(number: int, result: List[List[str]], excutetime: int):
    filepath = os.path.join(getConfig("resultpath"), getConfig("Solutionname") + "Result.txt")
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write("皇后数量:" + str(number) + '\n')
        file.write("解法总数:" + str(len(result)) + '\n')
        file.write("运行用时:" + str(excutetime) + "秒" + '\n')
        # 逐行打印至result.txt文件中
        for section in result:
            for line in section:
                file.write("".join(line) + '\n')
            file.write("\n")
