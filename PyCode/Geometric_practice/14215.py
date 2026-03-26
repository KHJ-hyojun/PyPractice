xx = list(map(int,input().split()))

kk = max(xx) 

if kk >= sum(xx) - kk:
    print(2*(sum(xx) - kk) - 1)
else:
    print(sum(xx))