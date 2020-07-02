def smoke(n,k):
    ans = n + n // k
    n = n // k + n % k
    while n >= k:
        n -= k
        n += 1
        ans += 1
    return ans

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests): 
        n, k = map(int, input().split())
        print(smoke(n,k))