import sys

def Main():
    n_tests = int(input())

    for _ in range(n_tests):
        array_size = int(input())
        array = list(map(int, input().split(' ')))

        subarray_sum = -sys.maxsize - 1
        max_sum = -sys.maxsize - 1 

        for i in range(len(array)):
            subarray_sum = max(array[i], subarray_sum + array[i])
            max_sum = max(max_sum, subarray_sum)

        print(max_sum)

if __name__ == '__main__':
    Main()
