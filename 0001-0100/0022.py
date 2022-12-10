count = 0
n = int(input())
while n > 0:
	count += n % 2
	n = n // 2
print(count)