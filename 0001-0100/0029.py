n = int(input())
y = [int(x) for x in input().split()]
paths = [0] * n
if n != 1:
	paths[1] = abs(y[0] - y[1])
for i in range(2, n):
	paths[i] = min(3 * abs(y[i] - y[i - 2]) + paths[i - 2], abs(y[i] - y[i - 1]) + paths[i - 1])
print(paths[-1])