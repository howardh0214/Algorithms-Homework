def Main():
    
    n = int(input())
    
    for _ in range(n):
        
        x = int(input())
        a = 0
        b = 1
        c = 0
        
        if x == 1:
            print("1")
        else:
            for i in range(x-1):
                #print("iteration", i)
                #print("b:{}, a:{}".format(b, a))
                c = a + b
                a = b
                b = c
                #print("c:{}, b:{}, a:{}".format(c, b, a))

        a = 0
        b = 1
        
        if x != 1:
            print(c)
        




if __name__ == '__main__':
    Main()