M = int(input())
N = int(input())
arr = []
for i in range(M,N+1):
    cnt = []
    for j in range(1,1+i):
        if i % j == 0 : cnt.append(j)
    if len(cnt) == 2: arr.append(i)
    
if len(arr) == 0 :
        print(-1)
else:
    print(sum(arr))
    print(min(arr))