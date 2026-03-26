T = int(input())
for i in range(T):
    final =""
    a,b = input().split()
    for j in range(len(b)):
        final += b[j] * int(a)
    print(final)
