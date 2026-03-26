T = int(input())

while T > 0:
    T -= 1
    xx = input()
    result = 0
    cnt = 0
    for i in range(len(xx)):
        if xx[i] == "O":
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)