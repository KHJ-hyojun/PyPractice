N , M = map(int,input().split())
N_list = [0] * N

for _ in range(M):
    i,j,k = map(int,input().split())

    for p in range(i,j+1):
        N_list[p-1] = k
    
for i in range(N):
    print(N_list[i], end = ' ')