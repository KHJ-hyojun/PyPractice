asc = [1,2,3,4,5,6,7,8]
de = [8,7,6,5,4,3,2,1]

xx = list(map(int,input().split()))

if xx == asc:
    print("ascending")
elif xx == de:
    print("descending")
else:
    print("mixed")
