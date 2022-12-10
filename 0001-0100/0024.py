def main():
	variants = 0
	n,m = [int(x) for x in input().split()]
	if n < m: return 0
	if m == 0: return 1
	if (m == 1): return n
	for k in range(1, n + 1):
		curr_len = (m - 1) * k +  1
		if (curr_len > n): break
		variants += n + 1 - curr_len
	return(variants)

print(main())