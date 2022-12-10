import math

def norm(x, y):
	return math.sqrt(x ** 2 + y ** 2)

def q_37(n, q):
	ret = "Yes"
	for i in range(n):
		x1, y1, x2, y2 = [int(x) for x in input().split()]
		if norm(x2, y2) == 0: continue
		if 1000 * norm(x2, y2) > norm(x1, y1) * q:
			ret = "No"
	return ret

def main():
	n, q = [float(x) for x in input().split()]
	q = int(1000 * q)
	print(q_37(int(n), q))

main()