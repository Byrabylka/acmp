a, b = input().split()

bulls = 0
for i, j in zip(a, b):
	if i == j:
		bulls += 1
cows = len(set(a).intersection(set(b))) - bulls
print(bulls, cows)