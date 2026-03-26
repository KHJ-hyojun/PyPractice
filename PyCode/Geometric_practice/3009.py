x_list = []
y_list = []

for i in range(3):
    x,y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

resultx = 0
resulty = 0
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        resultx = x_list[i]
    if y_list.count(y_list[i]) == 1:
        resulty = y_list[i]

print(resultx,resulty)
    

