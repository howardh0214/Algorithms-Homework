import math

def Brute_Force(Array):
    size = len(Array)
    minimum_distance = Euclidean_Distance(Array[0],Array[1])
    if len(Array) == 2:
        return minimum_distance
    for i in range(0,size):
        for j in range(i+1,size):
            distance = Euclidean_Distance(Array[i],Array[j])
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance

def Initial_sort(a):
    Px = sorted(a, key=lambda x: x[0])  
    Py = sorted(a, key=lambda x: x[1])  
    return Px, Py

def og(Px):
    midpoint_x = len(Px) // 2
    Qx = Px[:midpoint_x]
    Qx_og = Qx[:]
    return Qx_og

def Closest_Pair(Px, Py):
    midpoint_x = len(Px) // 2
    Qx = Px[:midpoint_x]
    if len(Px) <= 3:
        return Brute_Force(Px)
    else:
        Rx = Px[midpoint_x:]
        median_x = Px[midpoint_x]
        Qy,Ry = [], []
        for point in Py:
            if point[0] < int(median_x[0]):
                Qy.append(point)
            else:
                Ry.append(point)

        min_distance_Left = Closest_Pair(Qx,Qy)
        min_distance_Right = Closest_Pair(Rx,Ry)
        min_distance = min(min_distance_Left,min_distance_Right)
        return min_distance
            
def Closest_Split_Pair(min_distance, Qx, Py):
    x_bar = Qx[-1][0]
    Sy = []
    for y in Py:
        if (x_bar - min_distance) < y[0] < (x_bar + min_distance):
            Sy.append(y)
    

    for i in range(len(Sy) - 1):
        for j in range(i+1, min(i + 7, len(Sy))):
            P = Sy[i]
            Q = Sy[j]
            dist = Euclidean_Distance(P,Q)
            if dist < min_distance:
                min_distance = dist
    return min_distance   

def Euclidean_Distance(P,Q):
    return math.sqrt((P[0]-Q[0])**2 + (P[1]-Q[1])**2)

if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests):
        n_points = int(input())
        points = []
        array = [0,0]
        for _ in range(n_points):
            points.append(list(map(int,input().split(' '))))
        Px, Py = Initial_sort(points)
        array = og(Px)
        dist = Closest_Pair(Px, Py)
        print("{:.3f}".format(Closest_Split_Pair(dist, array, Py)))
         