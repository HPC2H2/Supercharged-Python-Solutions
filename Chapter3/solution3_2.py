"""
Author: HPC2H2
Date: 2025-03-12
Description: Solution to exercise 3.2
"""

def main():
    str_numbers = input("Enter a list of numbers (separate with spaces): ")
    try:
        list_numbers = list(map(float, str_numbers.split()))
    except ValueError:
        print("Invalid input")
    # 找中位数
    list_numbers.sort()
    mid = int(len(list_numbers) / 2)
    median = list_numbers[mid] if len(list_numbers) % 2 == 1 else \
        (list_numbers[mid - 1] + list_numbers[mid]) / 2
    print("The median is: ", median)

if __name__ == "__main__":
    main()