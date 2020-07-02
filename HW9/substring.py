try:
    while(1>0):
        a = input().split()
        s,t,k=a[0],a[1],0
        for i in range(len(t)):
            if k == len(s):
                break
            if s[k] == t[i]:
                k += 1
        if k != len(s):
            print("No")
        else:
            print("Yes")
except:
    exit(0)