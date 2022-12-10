def min_start(n):
	i = 1
	while i * (i + 1) < 2 * n:
		i += 1
	return (i)

def	count_ladder(n, maxx):
	count = 0
	if n <= 2:
		return 1
	for i in range(min_start(n), n + 1):
		if (i >= maxx): break
		count += count_ladder(n - i, i)
	return count

n = int(input())
print(count_ladder(n, n + 1))
