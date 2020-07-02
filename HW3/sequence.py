def Main():

    n = int(input())

    for _ in range(n):

            m = int(input())

            output = 0

            numbers = list(map(int, input().split(' ')))

            for i in range(len(numbers)):
                for j in range(len(numbers)):
                    if j == i:
                        continue
                    for m in range(len(numbers)):
                        if m == i or m == j :
                            continue
                        if numbers[m] == numbers[i] + numbers[j]:
                            output = 1

            if output == 1:
                print("false")
            else:
                print("true")


if __name__ == '__main__':
    Main()