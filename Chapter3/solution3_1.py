"""
Author: HPC2H2
Date: 2025-03-12
Description: Solution to exercise 3.1
"""

import functools
import random

def main():
    """
    计算随机数列表的方差相关数据。

    主函数完成以下功能:
    1. 使用固定种子生成100个1-100之间的随机整数列表
    2. 使用 reduce 函数计算列表平均值
    3. 计算每个元素与平均值的差的平方,返回结果列表

    Returns:
        None: 直接打印随机数列表和差值平方列表
    """
    # 生成一个包含100个随机数的列表
    random.seed(100)
    numbers = [random.randint(1, 100) for i in range(100)]
    # print(numbers)
    # 使用reduce列表处理函数来获取列表中数字的平均值
    avg = functools.reduce(lambda x, y: x + y, numbers) / len(numbers)
    # 计算每个元素与平均值的差的平方，返回结果列表
    result = [pow(x - avg, 2) for x in numbers]
    print(result)
    
if __name__ == "__main__":
    main()