def bin_packing(things, n_things):
    bin_count = 0
    bin = [float(1) for i in things]
    for i in range(n_things):
        min_space_left = float(1)
        best_bin_index = 0
        for j in range(bin_count):
            if (bin[j] >= things[i] and bin[j] < min_space_left):
                best_bin_index = j
                min_space_left = bin[j] - things[i]
            
        if min_space_left == float(1) and things[i] != 0:
            bin[bin_count] = float(1) - things[i]
            bin_count += 1
        else:
            bin[best_bin_index] -= things[i]
    return bin_count
                
       
        
if __name__ == '__main__':
    n_things = int(input())
    things = list(map(float,input().split(' ')))
    print(bin_packing(things, n_things))