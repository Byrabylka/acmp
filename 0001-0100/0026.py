import math
x1,y1,r1 = [int(x) for x in input().split()]
x2,y2,r2 = [int(x) for x in input().split()]
distance = math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)
if distance <= r1 + r2 and distance >= abs(r1 - r2): print('YES')
else: print("NO")