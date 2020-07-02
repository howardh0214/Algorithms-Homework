def Main():
    n = input()
    for _ in range(int(n)):
        ab = list(map(int, input().split(' ')))
        a = ab[0]
        b = ab[1]

        #print(a, b)

        sum = 0

        for i in range(a, b+1):
            if i % 2 != 0:
                #print(i, "is a odd number")
                for p in range (3, i//2):
                    if (i % p) == 0:
                        sum += i
                        #print("\n", i, "is not a prime number")
                        #print(sum, ", after addition\n")
                        break
                    else:
                        sum = sum
                        #print(sum, ", no addition\n")
                        #print("\n", i, "is a prime number")
            #else:
                #print(i, "is not a odd number")
                    

        print(sum)


if __name__ == '__main__':
    Main()