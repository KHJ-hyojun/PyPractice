N = int(input())

arr = [[0]*100 for i in range(100)]

for i in range(N):
    x , y = map(int, input().split())

    for p in range(x,x+10):
        for q in range(y, y+10):
            arr[p][q] = 1

result = 0 

for row in range(100):
    result += arr[row].count(1)
print(result)
