"""
Author: HPC2H2
Date: 2025-02-20
Description: Solution to exercise 2.1
"""
# Write a program that prompts for a string and
#  counts the number of vowelsand consonants, then outputs the result.
# (Hint: use the in and not in operatorsto reduce the amount
#  of code you might otherwise have to write.)
# 编写一个程序，提示输入字符串并计算元音和辅音的数量，然后输出结果。
# (提示:使用in和 not in 运算符可以减少代码量。)


if __name__ == "__main__":
    while True:
        curstr = input("Enter a string:")
        if not curstr:
            break
        vowel_count = 0
        for ch in "aeiouAEIOU":
            vowel_count = vowel_count + curstr.count(ch)
        consonantcount = len(curstr) - vowel_count
        print("Vowels:", vowel_count)
        print("Consonants:", consonantcount)
