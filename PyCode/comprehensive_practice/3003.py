answer = [1,1,2,2,2,8]
have = list(map(int, input().split()))
result = []
for i in range(6):
    result.append(answer[i] - have[i])
for i in range(6):
    print(result[i], end = " ")