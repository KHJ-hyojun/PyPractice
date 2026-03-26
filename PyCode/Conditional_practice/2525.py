hour, minute = map(int, input().split())
cooktime = int(input())

minute += cooktime

while minute >= 60:
    minute -= 60
    hour += 1

if hour >= 24: hour -= 24
    
    

print(hour, minute)