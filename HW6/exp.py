def exp(total):
    if total == 0:
        return 1

    temp = exp(total//2)

    if total % 2 == 0:
        return temp * temp
    else:
        return 2 * temp * temp






if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests):
        m , n = list(map(int, input().split(' '))) 
        print(exp(m) + exp(n))