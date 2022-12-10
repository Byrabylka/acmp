x1,y1,x2,y2 = [int(x) for x in input().split()]
a,b = [int(x) for x in input().split()]
if x1 == x2: print(x1 + x1 - a, b)
else: print(a, y1 + y1 - b)