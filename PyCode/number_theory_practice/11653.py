N = int(input())
arr = []
for i in range(1, 1+N):
    if N % i == 0: arr.append(i)

for i in arr:
    if i == 1: continue
    while N % i == 0:
        print(i)
        N /= i