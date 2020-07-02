def perfect(m): 
    ans = []
    factor = []
    for i in range(len(m)):
        factor.append([0])
        for j in range(2, int(m[i]**0.5+1)):
            if (m[i]/j) % 1 == 0.0:
                if j != int(m[i]/j):
                    factor[i].append(j)
                    factor[i].append(int(m[i]/j))
                else:
                    factor[i].append(j)
            
        factor[i].append(1)
    
    for i in range(len(m)):
        if sum(factor[i]) == m[i]:
            ans.append(m[i])
    
    return ans




try:
    while(1):
        n = input()
        m = list(map(int, input().split(' '))) 
        ans = perfect(m)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
except:
    exit(0)