N , M = map(int, input().split())

N_list = [i+1 for i in range(N)]


for _ in range(M):
    i,j = map(int, input().split())
    tr = N_list[i-1]
    N_list[i-1] = N_list[j-1]
    N_list[j-1] = tr

for _ in range(N):
    print(N_list[_], end = " ")