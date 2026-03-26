max = 0
attempt = 0
index = 0
while 1:
    try:
        a = int(input())
        if max <= a: 
            max = a
            index = attempt + 1
        attempt += 1
    except:
        break
print(max)
print(index)


