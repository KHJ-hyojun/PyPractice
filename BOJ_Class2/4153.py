while True:
        
    xx = list(map(int,input().split()))
    if xx == [ 0,0,0 ] : break
    com = 0
    for i in xx:
        if i != max(xx):
            com += i**2

    if max(xx)**2 == com:
        print("right")
    else:
        print("wrong")