receipt_sum = int(input())
enum = int(input())
real_sum = 0

for i in range(enum):
    a,b = map(int,input().split())
    real_sum += a*b

if real_sum == receipt_sum:
    print("Yes")
else:
    print("No")
