k = int(input())
values = [0] * k
for i in range(k):
	n,m = [int(x) for  x in input().split()]
	values[i] = (lambda n,m: 19 * m + (n + 239) * (n + 366) // 2)(n, m)
for i in values: print(i)