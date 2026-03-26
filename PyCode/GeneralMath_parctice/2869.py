"""
up, down, length = map(int, input().split())
day_cnt = 0
how = 0

while how < length:
    if how + up > length and how + up - down < length:
        break
    else:
        how += up - down
        day_cnt += 1

print(day_cnt)

"""
up, down, length = map(int,input().split())

day_cnt = (length - down) / (up - down)

if day_cnt == int(day_cnt):
    print(int(day_cnt))
else:
    print(int(day_cnt) + 1)
