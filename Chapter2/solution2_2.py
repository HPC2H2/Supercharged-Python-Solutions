"""
Author: HPC2H2
Date: 2025-02-20
Description: Solution to exercise 2.2
"""
# Write a function that efficiently strips the first two characters
# of a string andthe last two characters of a string. Returning an
# empty string should be anacceptable return value. Test this function
# with a series of different inputs.
# 编写一个函数，该函数可删除字符串的前两个字符和后两个字符。
# 空字符串应该是一个可接受的返回值。使用一组不同的输人来测试此功能。


def del_first_and_last_two_chars(s):
    """
    删除字符串首尾的两个字符。

    参数:
        s (str): 输入的字符串。

    返回:
        str: 删除首尾两个字符后的新字符串。
    """
    return s[2:-2]

if __name__ == "__main__":
    print(del_first_and_last_two_chars("Hello, World!")) # llo, Wor
    print(del_first_and_last_two_chars("Python")) # th
    print(del_first_and_last_two_chars("")) #
