import math 

test = int(input())
intersection = []

for _ in range(test):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    minus = abs(r1-r2)
    plus = r1+r2
    distance = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    
    if distance == 0 and r1 == r2: intersection.append(-1)
    elif plus == distance or minus == distance: intersection.append(1)
    elif minus < distance < plus : intersection.append(2)
    else: intersection.append(0)

for i in intersection:
    print(i)