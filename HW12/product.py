def product(n):
    k = ""
    #if 1 <= n <= 9:
        #return n
    for i in range(9,1,-1):
        if n % i == 0:
            k = str(i) + k
            n /= i 
    if n == 1:
        return k
    else:
        return "-1"
    

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests): 
        print(product(int(input())))
        