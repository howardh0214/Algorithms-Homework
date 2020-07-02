def brick(n, original):
    average = sum(original) / len(original)
    moves = 0
    for i in range(len(original)):
        moves += abs(original[i]-average)
    moves /= 2
    return int(moves)





if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests): 
        n = int(input())
        original = list(map(int, input().split(' ')))
        print(brick(n, original))