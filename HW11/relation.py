def relation(m):
    if m[0] < m[1]:
        return "<"
    elif m[0] > m[1]:
        return ">"
    else:
        return "="


if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests): 
        m = list(map(int, input().split(' ')))
        print(relation(m))