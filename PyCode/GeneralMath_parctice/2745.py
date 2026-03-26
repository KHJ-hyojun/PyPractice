num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N,B = input().split()

answer = 0

for i, num in enumerate(N[::-1]):
    answer += int(B) ** i *num_list.index(num)

print(answer)

