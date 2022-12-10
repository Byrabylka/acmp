import itertools
import math
# def C_n_m(n, m):
# 	return (math.factorial(n) //(math.factorial(m) * math.factorial(n - m))
def check(lst):
	for i in range(len(lst)):
		if i == lst[i]: return 0
	return 1

variants = 0
n,m = [int(i) for i in input().split()]
nbs = [i for i in range(n - m)]
for i in itertools.permutations(nbs):
	variants += check(i)
print(variants * math.factorial(n) //(math.factorial(m) * math.factorial(n - m)))