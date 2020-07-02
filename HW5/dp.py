import sympy
import math
import sys

def dp(n_tests, equation):
    
    for _ in range(n_tests):
        x = sympy.symbols('x')
        equation_split = equation.split("=")
        equation_left = [char for char in equation_split[0]]
        equation_right = [char for char in equation_split[1]]

        left = []
        right = []

        for i in range(len(equation_left)):
            if equation_left[i] == "x" and i != 0 and equation_left[i-1] != "+" and equation_left[i-1] != "-":
                #print("x detected at", i)
                left.append("*")
            left.append(equation_left[i])
            
        
        right.append("-")
        right.append("(")
        for j in range(len(equation_right)):
            if equation_right[j] == "x" and j != 0 and equation_right[j-1] != "+" and equation_right[j-1] != "-":
                #print("x detected at", j)
                right.append("*")
            right.append(equation_right[j])
        right.append(")")
        
        left.append(right)
        left = [item for sublist in left for item in sublist]

        empty = ""
        left = empty.join(left)

        left = eval(left)

        if left == 0:
            print("IDENTITY")
        else:
            try:
                print(int(math.floor(sympy.solve(left,x)[0])))
            except IndexError:
                print("IMPOSSIBLE")


if __name__ == '__main__':
    n_tests = int(input())
    equation = sys.stdin.readline()
    dp(n_tests, equation)
