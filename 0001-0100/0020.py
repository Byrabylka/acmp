def sign(n):
	if n > 0: return 1
	if n == 0: return 0
	if n < 0: return -1

def main():
	n = int(input())
	lst = [int(x) for x in input().split()]
	if (n == 1): 
		print(1)
		return
	maxx = 1
	curr = 1
	sgn = sign(lst[1] - lst[0])
	if not sgn: sgn = 1
	for i in range(len(lst) - 1):
		if sign(lst[i + 1] - lst[i]) != sgn:
			maxx = max(maxx, curr)
			curr = 2
			if lst[i + 1] == lst[i]:
				curr = 1
			continue
		curr += 1
		sgn *= -1
	maxx = max(maxx, curr)
	print(maxx)

main()