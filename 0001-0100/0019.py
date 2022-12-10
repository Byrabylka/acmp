
class chess(object):
	def __new__(cls, q, r, n):
		return super(chess, cls).__new__(cls)

	def __init__(self, q, r, n):
		self.matr = [[0] * 8 for i in range(8)]
		self.q = q
		self.r = r
		self.n = n
	
	def obrabotka_q(self):
		x = 8 - int(self.q[1])
		y = ord(self.q[0]) - 65
		for i in range(8):
			if self.matr[x][i] == 0:
				self.matr[x][i] = 1
			if self.matr[i][y] == 0:
				self.matr[i][y] = 1	 
		for i in range(8):
			for j in range(8):
				if abs(i - x) == abs(j - y) and self.matr[i][j] == 0:
					self.matr[i][j] = 1
		self.matr[x][y] = 2
	
	def obrabotka_r(self):
		x = 8 - int(self.r[1])
		y = ord(self.r[0]) - 65
		for i in range(8):
			if self.matr[x][i] == 0:
				self.matr[x][i] = 1
			if self.matr[i][y] == 0:
				self.matr[i][y] = 1
		self.matr[x][y] = 2
	
	def obrabotka_n(self):
		x = 8 - int(self.n[1])
		y = ord(self.n[0]) - 65
		for i in range(8):
			for j in range(8):
				if abs((x - i) * (y - j)) == 2 and self.matr[i][j] == 0:
					self.matr[i][j] = 1
		self.matr[x][y] = 2

	def	count_ones(self):
		count = 0
		for  i in self.matr:
			for j in i:
				if j == 1: count += 1
		return count

	def __str__(self):
		chess.obrabotka_n(self)
		chess.obrabotka_q(self)
		chess.obrabotka_r(self)
		return(str(chess.count_ones(self)))


def main():
	q,r,n = input().split()
	obj = chess(q, r, n)
	print(obj)

main()