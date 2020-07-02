def Main():
    n_tests = int(input())
    for _ in range(n_tests):
        scores = list(map(int, input().split(' ')))
        scores = sorted(scores)
        k = int(input())
        print(scores[k-1])

        

if __name__ == '__main__':
    Main()