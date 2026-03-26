ss = [input() for i in range(5)]
result = ""

for i in range(15):
    for j in range(5):
        try:
            result += ss[j][i]
        except:
            pass
print(result)
            