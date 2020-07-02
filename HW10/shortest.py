def shortestDist(graph): 
    V = 11

    dist = graph

    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 
    
    line_1 = [0, min(dist[0][1], dist[0][2], dist[0][3])]

    if min(dist[0][1], dist[0][2], dist[0][3]) == dist[0][1]:
        line_1[0] = 1
    elif min(dist[0][1], dist[0][2], dist[0][3]) == dist[0][2]:
        line_1[0] = 2
    else:
        line_1[0] = 3

    
    line_2 = [0, min(dist[0][4], dist[0][5], dist[0][6])]

    if min(dist[0][4], dist[0][5], dist[0][6]) == dist[0][4]:
        line_2[0] = 4
    elif min(dist[0][4], dist[0][5], dist[0][6]) == dist[0][5]:
        line_2[0] = 5
    else:
        line_2[0] = 6

    line_3 = [0, min(dist[0][7], dist[0][8], dist[0][9])]

    if min(dist[0][7], dist[0][8], dist[0][9]) == dist[0][7]:
        line_3[0] = 7
    elif min(dist[0][7], dist[0][8], dist[0][9]) == dist[0][8]:
        line_3[0] = 8
    else:
        line_3[0] = 9

    line_4 = [10, dist[0][10]]
    
    print("{} {}".format(line_1[0], line_1[1]))
    print("{} {}".format(line_2[0], line_2[1]))
    print("{} {}".format(line_3[0], line_3[1]))
    print("{} {}".format(line_4[0], line_4[1]))



try:
    while(1):
        INF = 99999
        graph = [[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], 
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]]  
        graph[0][1] = int(input())
        graph[0][2] = int(input())
        graph[0][3] = int(input())
        graph[1][4] = int(input())
        graph[1][5] = int(input())
        graph[1][6] = int(input())
        graph[2][4] = int(input())
        graph[2][5] = int(input())
        graph[2][6] = int(input())
        graph[3][4] = int(input())
        graph[3][5] = int(input())
        graph[3][6] = int(input())
        graph[4][7] = int(input())
        graph[4][8] = int(input())
        graph[4][9] = int(input())
        graph[5][7] = int(input())
        graph[5][8] = int(input())
        graph[5][9] = int(input())
        graph[6][7] = int(input())
        graph[6][8] = int(input())
        graph[6][9] = int(input())
        graph[7][10] = int(input())
        graph[8][10] = int(input())
        graph[9][10] = int(input())
        shortestDist(graph)
except:
    exit(0)