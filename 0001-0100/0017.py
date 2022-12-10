def check(n, numbers, i):
	if n % i != 0:
		return 0
	start = numbers[:i] * (n // i)
	return start == numbers	

def main():
	n = int(input())
	numbers = list(map(int, input().split()))[:-1]
	for i in range(1, n + 1):
		if check(n - 1, numbers, i):
			print(i)
			return
	print(n - 1)

main()