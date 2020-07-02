import math

def count(l, k):
    length = []
    for i in range(1, l+1):
        length.append(i)
    for i in range(l-1, 0, -1):
        length.append(i)

    square = []
    for i in range(len(length)):
        #even
        if length[i] % 2 == 0: 
            square.append(create_even(length[i]))
        #odd
        else:
            square.append(create_odd(length[i]))
    
    newlist = [item for items in square for item in items]
    
    return newlist[k-1]


def create_odd(n):
    output = []
    if n == 1:
        output = [1]
    else:
        for i in range(1, math.ceil(n/2)):
            output.append(i)
        for i in range(math.ceil(n/2), 0, -1):
            output.append(i)
    return output
        
    
def create_even(n):
    output = []
    if n == 2:
        output = [1, 1]
    else:
        for i in range(1, int(n/2)+1):
            output.append(i)
        for i in range(int(n/2), 0, -1):
            output.append(i)
    return output
        
    




if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests): 
        l, k = map(int, input().split(' '))
        print(count(l, k))