S = input()
arr = [-1 for i in range(26)]
for i in range(len(S)):
    if arr[ord(S[i]) - 97] == -1:
        arr[ord(S[i]) - 97] = i
for i in range(26):
    print(arr[i], end = " ")