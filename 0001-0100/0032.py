def get_int(lst):
	nb = 0
	for i in lst:
		nb = nb * 10 + int(i)
	return nb

def get_max(a):
	max_nb = a
	if a == 0: return a
	if a < 0: return get_min(-a) * -1
	lst = [int(i) for i in str(a)]
	lst.sort(key = lambda x: -x)
	return get_int(lst)

def get_min(a):
	min_nb = a
	if a == 0: return a
	if a < 0: return get_max(-a) * -1
	lst = [int(i) for i in str(a) if int(i) != 0]
	zero_count = str(a).count('0')
	lst.sort()
	for i in range(zero_count): lst.insert(1, 0)
	return get_int(lst)

def main():
	a = int(input())
	b = int(input())
	a = get_max(a)
	b = get_min(b)
	print(a - b)

main()