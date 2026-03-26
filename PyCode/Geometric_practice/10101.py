a = int(input())
b = int(input())
c = int(input())

angle = a + b + c

if a == b == c == 60:
    print("Equilateral")
elif angle == 180 and (a==b or b==c or a==c):
    print("Isosceles")
elif angle == 180:
    print("Scalene")
else:
    print("Error")