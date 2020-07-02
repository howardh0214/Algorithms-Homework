def gcd(a, b): 
    if (a == 0): 
        return b 
    
    return gcd(b % a, a) 

"""
def check_prime(x,y):
    print(f"checking {x}, {y}")
    factors_x = []
    factors_y = []
    for i in range(2, int(x) + 1): 
        while x % i == 0: 
            factors_x.append(int(i)) 
            x = x / i
    for i in range(2, int(y) + 1): 
        while y % i == 0: 
            factors_y.append(int(i)) 
            y = y / i

    print(factors_x)
    print(factors_y)
    print(bool(set(factors_x).intersection(factors_y)))
    return(bool(set(factors_x).intersection(factors_y)))
"""

def Main():

    
    n = int(input())

    for _ in range(n):
        x = int(input())
        
        p = []
        sum = 1

        for i in range(2, x):
            if gcd(i, x) == 1:
                sum += 1

        print(sum)


if __name__ == '__main__':
    Main()