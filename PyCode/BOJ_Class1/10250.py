T= int(input())


while T>0:
    T -= 1
    H, W, N = map(int, input().split())
    floor = N % H
    way = 1 + (N//H)

    if floor == 0:
        floor = H
        way -= 1
    
    

print(floor * 100 + way)
            


