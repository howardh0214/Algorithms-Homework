def crypt(x, y):
    while True:
        return (round(y ** (1 / x)))
        
        



if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests):
        m , n = list(map(int, input().split(' '))) 
        print(crypt(m, n))