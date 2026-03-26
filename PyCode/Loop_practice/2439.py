t = int(input())
rr = t

for i in range(t):
    print(" " * (rr-1) + "*" * (i+1))
    rr = rr-1