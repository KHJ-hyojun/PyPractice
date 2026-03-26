num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())

answer  ="" 

while N:
    answer += num_list[N%B]
    N //= B

print(answer[::-1])
