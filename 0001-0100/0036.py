import math
def is_prime(n):
	if n <= 1: return 0
	if n <= 3: return 1
	for i in range(2, int(1 + math.sqrt(n)) + 1):
		if n % i == 0: return 0
	return 1

n = int(input())
count = 0
for i in range(n + 1, 2 * n):
	if is_prime(i): count += 1
print(count)