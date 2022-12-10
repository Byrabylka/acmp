def main():
	n,k = [int(x) for x in input().split()]
	shifr = input()
	codes = [shifr[i:i+k] for i in range(n - k + 1)]
	if len(codes) == len(set(codes)): return "NO"
	return "YES"

print(main())