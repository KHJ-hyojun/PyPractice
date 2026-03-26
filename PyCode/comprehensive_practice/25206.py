grade_dic = {"A+" : 4.5, "A0": 4.0, "B+" : 3.5, "B0" : 3.0 , "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0.0, "P" : 0.0}
all_sum = 0
hak_sum = 0
for i in range(20):
    a, b, c = input().split()
    if c == "P": continue
    b = float(b)
    all_sum += b * grade_dic[c]
    hak_sum += b
print(all_sum / hak_sum)


