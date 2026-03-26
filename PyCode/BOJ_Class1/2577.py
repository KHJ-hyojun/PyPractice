a = int(input())
b = int(input())
c = int(input())

arr = [0,0,0,0,0,0,0,0,0,0]
x = str(a*b*c)

for i in range(len(x)):
    arr[int(x[i])] += 1

for j in arr:
    print(j)
