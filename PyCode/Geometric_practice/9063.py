N = int(input())
if N == 1: print(0)
else:
    xx = [] 
    yy = []

    for i in range(N):
        x,y = map(int,input().split())
        xx.append(x)
        yy.append(y)

    print((max(xx)-min(xx))*(max(yy)-min(yy)))