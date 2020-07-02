import math

def Main():
    n = int(input())
    p = n

    factors = []

    for i in range(2, int(n) // 2): 
        while n % i == 0: 
            factors.append(int(i)) 
            n = n / i 

    #print(factors)
    
    factors_p = []
    
    for item in factors:
        #print(item, "is processing")
        if factors.count(item) != 1:
            factors_p.append([item, factors.count(item)])
        else:
            factors_p.append([item, factors.count(item)])
    
    res = []
    [res.append(x) for x in factors_p if x not in res] 

    #print(factors_p)
    #print(res)
    #print(len(res))
    print(p,"=",sep="", end ="")

    for i in range(0, len(res)):
        print(res[i][0], sep="", end ="")
        if res[i][1] != 1:
            print("^", res[i][1], sep="", end ="")
        if i != len(res)-1:
            print("*", end ="")



if __name__ == '__main__':
    Main()