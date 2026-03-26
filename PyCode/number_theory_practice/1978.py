N = int(input())
arr = list(map(int, input().split()))
result = 0
for i in arr:
    if i == 1: continue
    cnt = []
    for j in range(1,i+1):
        if i % j == 0 : cnt.append(j) 
    if len(cnt) == 2: result += 1
print(result)
