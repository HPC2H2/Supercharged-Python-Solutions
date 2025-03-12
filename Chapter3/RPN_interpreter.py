"""
Author: HPC2H2
Date: 2025-03-12
Description: RPN interpreter
"""

def main():
    str_exp = input("Enter an RPN expression(only for intergers and +-*/): ")
    list_exp = str_exp.split()
    stack = []
    for item in list_exp:
        if item.isdigit():
            stack.append(int(item))
        elif item in "+-*/":
            try:
                b = stack.pop()
                a = stack.pop()
            except IndexError:
                raise IndexError("Too many operands, or too few operators")
            except ZeroDivisionError:
                pass

            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(a - b)
            elif item == '*':
                stack.append(a * b)
            elif item == '/':
                stack.append(a / b)
        else:
            raise ValueError("Invalid operator")
    
    if len(stack) > 1:
        raise IndexError("Too many operands, or too few operators")
    print("The result is", stack.pop())
    

if __name__ == "__main__":
    main()
