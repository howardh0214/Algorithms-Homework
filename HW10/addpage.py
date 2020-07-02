def page(l):
    sum = 0
    start1 = 0
    start2 = 1
    page = 0
    while (sum <= l):
        sum = start1 + start2
        page += 1
        start1 = sum
        start2 += 1

    print("{} {}".format(sum-l, page))

    #print("sum "+ str(sum))
    #print("page "+ str(page))





if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests): 
        l = int(input())
        page(l)