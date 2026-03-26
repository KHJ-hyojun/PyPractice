All_st = {i+1 for i in range(30)}
Now_st = []

for i in range(28):
    a = int(input())
    Now_st.append(a)
Not_st = sorted(All_st - set(Now_st))
print(Not_st[0])
print(Not_st[1])
