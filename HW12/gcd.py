import math 

if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests): 
        m = list(map(int, input().split(' ')))
        print(math.gcd(m[0],m[1]))