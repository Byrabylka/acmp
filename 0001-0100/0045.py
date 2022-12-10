def digit_compositions(n):
	if n == 1: return [1]
	if n == 0: return [10]
	lst = []
	while n > 1:
		for i in range(9, 0, -1):
			if n % i == 0:
				lst.append(i)
				n = n // i
				break
		if i == 1 and n != 1: return [] 
	return lst

def main():
	n = int(input())
	lst = sorted(digit_compositions(n))
	res = 0
	for i in lst:
		res = res * 10 + i
	if res == 0: res = -1
	print(res)

main()