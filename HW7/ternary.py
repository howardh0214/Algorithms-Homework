def ternary(n):
    convertString = "0123456789ABCDE"
    if n < 3:
        return convertString[n]
    else:
        return ternary(n//3) + convertString[n%3]





if __name__ == '__main__':
    while True:
        x = int(input())
        if x >= 0:
            print(ternary(x))
        else:
            break