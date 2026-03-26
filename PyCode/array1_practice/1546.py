N = int(input())
arr = list(map(int,input().split()))
M = max(arr)
average = 0
for i in range(N):
    arr[i] /= M
    arr[i] *= 100
    average += arr[i]
average /= N
print(average)