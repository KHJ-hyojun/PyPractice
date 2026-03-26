N, M = map(int,input().split())

arr1 = [[0] * M for i in range(N)]
arr2 = [[0] * M for i in range(N)]


for i in range(N):
    ss = list(map(int, input().split()))
    for j in range(M):
        arr1[i][j] = ss[j]
        
for i in range(N):
    ss = list(map(int, input().split()))
    for j in range(M):
        arr2[i][j] = ss[j]

final = [[arr1[i][j] + arr2[i][j] for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        print(final[i][j], end=" ")
    print()