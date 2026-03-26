T = int(input())
arr = [0,0,0,0]
cent = [25,10,5,1]
for i in range(T):
    mon = int(input())
    for j in cent:
        while mon > 0 and mon >= j:
            mon -= j
            arr[cent.index(j)] += 1
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    arr = [0,0,0,0]
    
    
