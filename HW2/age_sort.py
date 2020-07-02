def Main():
    """
    def heapify(arr, n, i): 
        largest = i  
        l = 2 * i + 1    
        r = 2 * i + 2     
  
        if l < n and arr[i] < arr[l]: 
            largest = l 
    
        if r < n and arr[largest] < arr[r]: 
            largest = r 
    

        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] 
            heapify(arr, n, largest) 
  
    def heapSort(arr): 
        n = len(arr) 
     
        for i in range(n, -1, -1): 
            heapify(arr, n, i) 
    
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] 
            heapify(arr, i, 0) 
    """
    
    while True:
        try:
		        people = input()
        except EOFError:
		        break
    
        if people == str(0):
            break
    
        age = list(map(int, input().split(' ')))
        age.sort()

        for p in range(0, len(age)-1):
                print(age[p], end =" ")     

        print(age[len(age)-1])


if __name__ == '__main__':
    Main()