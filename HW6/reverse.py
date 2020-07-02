
n_reverse = 0


def reverse(num):
    reverse = 0
  
    while(num > 0): 
        a = num % 10
        reverse = reverse * 10 + a 
        num = num // 10
      
    return reverse

def sum_reverse(number):
    global n_reverse
    a = reverse(number)
    if number == a and n_reverse != 0:
        return number
    else:
        n_reverse += 1
        return sum_reverse(number + a)







if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests):
        num = int(input())
        n_reverse = 0
        x = sum_reverse(num)
        print(n_reverse, end = " ")
        print(x)