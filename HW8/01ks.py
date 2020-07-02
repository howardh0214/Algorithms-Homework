def ks(W , wt , val , n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
    
    

    




if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests): 
        W = int(input())
        wt = list(map(int, input().split(' ')))
        val = list(map(int, input().split(' ')))
        n = 5
        print(ks(W, wt, val, n))
