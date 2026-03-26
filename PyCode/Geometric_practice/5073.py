while True:
    xx = list(map(int,input().split()))
    kk = max(xx)
    xx.remove(kk)
    xx.append(kk)
    if xx[0] == xx[1] == xx[2] == 0 : break
    else:
        if xx[2] < xx[0] + xx[1]:
            if xx[0] == xx[1] == xx[2] :
                print("Equilateral")
            elif xx[0] == xx[1] or xx[1] == xx[2] or xx[0] == xx[2]:
                print("Isosceles")
            else:
                print("Scalene")
        else:
            print("Invalid")