class hare(object):

	def __new__(cls, k, n):
		return super(hare, cls).__new__(cls)

	def __init__(self, k, n):
		self.k, self.n = k, n
		self.lst = [0] * n

	def count(self, i):
		if i == 0:
			self.lst[i] = 1
		else:
			for j in range(max(i - self.k, 0), i):
				self.lst[i] += self.lst[j]
			if i < self.k:
				self.lst[i] += 1

	def	__str__(self):
		return (str)(self.lst[-1])



def main():
	k, n = list(map(int, input().split()))
	obj = hare(k, n)
	for i in range(n):
		obj.count(i)
	print(obj)

main()