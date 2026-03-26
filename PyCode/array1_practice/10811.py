N, M = map(int, input().split())

arr = [i+1 for i in range(N)]

for r in range(M):
    i,j = map(int, input().split())
    basket = arr[i-1:j]
    basket.reverse()
    arr[i-1:j] = basket

for i in range(N):
    print(arr[i],end=" ")