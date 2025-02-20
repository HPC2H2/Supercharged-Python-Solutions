"""
Author: HPC2H2
Date: 2025-02-20
Description: Solution to exercise 1.1
"""
# Write a little program that asks for
# your name, age, and address, and thenprints
# all the information you just entered.
# However, instead of placing it ina function called main,
# place it in a function called test func.
# Then calltest func to run it.
# 编写一个程序,询问用户的姓名、年龄和地址,然后打印出刚刚输入的所有信息。
# 将程序代码放在一个名为test_func的函数中，然后调用函数来运行它。


def test_func():
    """
    测试函数，提示用户输入姓名、年龄和地址，并打印这些信息。

    函数功能：
    - 提示用户输入姓名、年龄和地址。
    - 输出用户输入的姓名、年龄和地址。

    使用示例：
    test_func()
    """
    name = input("Enter your name:")
    age = input("Enter your age:")
    address = input("Enter your address:")
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)

if __name__ == "__main__":
    test_func()
