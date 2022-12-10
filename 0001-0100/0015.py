matr = []
count = 0
n = int(input())
for i in range(n):
	matr.append(list(map(int, input().split())))
for i in range(n):
	for j in range(i + 1, n):
		count += matr[i][j]
print(count)