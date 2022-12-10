def	count_ones(matr):
	count = 0
	for  i in matr:
		for j in i:
			if j == 1: count += 1
	return count

n,m = [int(x) for x in input().split()]
matr = [[1] * m for x in range(n)]
count_rect = int(input())
for k in range(count_rect):
	x1,y1,x2,y2 = [int(x) for x in input().split()]
	for i in range(x1, x2):
		matr[i][y1:y2] = [0] * (y2 - y1)
print(count_ones(matr))
