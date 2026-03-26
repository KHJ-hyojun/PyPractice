N, K = map(int, input().split())
arr = []
for i in range(N):
    if N % (i+ 1) == 0:
        arr.append(i+1)
if K > len(arr):
    print(0)
else:
    print(arr[K - 1])