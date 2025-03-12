"""
Author: HPC2H2
Date: 2025-03-12
Description: RPN interpreter
"""

def main():
    str_exp = input("Enter an RPN expression: ")
    list_exp = str_exp.split()
    stack = []
    for e in list_exp:
        if e.isdigit():
            stack.append(int(e))
        else:
            try:
                b = stack.pop()
                a = stack.pop()
                if e == "+":
                    stack.append(a + b)
                elif e == "-":
                    stack.append(a - b)
                elif e == "*":
                    stack.append(a * b)
                elif e == "/":
                    stack.append(a / b)
                else:
                    print("Invalid operator")
            except IndexError:
                print("Invalid expression")
            finally:
                if len(stack) > 1:
                    print("多余的的数字操作数")
                print("The result is", stack.pop())
    

if __name__ == "__main__":
    main()
