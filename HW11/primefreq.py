from collections import Counter

def primefreq(m): 
    ans = []
    output = []
    empty = 0
    c = Counter(m)
    for letter in c:
        ans.append([letter, c[letter]])

    for i in range(len(ans)):
        if isPrime(ans[i][1]) is True:
            output.append(ans[i][0])
            empty = 1

    output.sort()
    
    if empty == 0:
        return "Empty"



    return ''.join(output)



def isPrime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
    

if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests): 
        m = list(str(input()))
        print(primefreq(m))