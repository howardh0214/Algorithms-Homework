def oddsum(m,n):
    sum = 0
    for i in range(m,n+1):
        if i % 2 == 1:
            sum += i

    return sum



if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests): 
        m = int(input())
        n = int(input())
        print("Case {}: {}".format(i+1, oddsum(m,n)))