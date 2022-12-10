import math
class rectangle(object):

	def __new__(cls, x, y, coords):
	    return super(rectangle, cls).__new__(cls)
	
	def	distance(x, y, x1, y1):
		return math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

	def get_dio(x, y, coords):
		dios = []
		for i in range(4):
			dios.append(rectangle.distance(x, y, coords[2 * i], coords[2 * i + 1]))
		return dios

	def get_lens(x, y, coords):
		lens = []
		for i in range(4):
			lens.append(rectangle.distance(coords[2 * i], coords[2 * i + 1], coords[(2 * i + 2) % 8], coords[(2 * i + 3) % 8]))
		return lens

	def __init__(self, x, y, coords):
		self.x = x
		self.y = y
		self.coords = coords
		self.diagonals = rectangle.get_dio(x, y, coords)
		self.lens = rectangle.get_lens(x, y, coords)

	def angle_count(self):
		a = []
		for i in range(4):
			try:
				a.append(math.acos((self.diagonals[i] ** 2 + self.diagonals[(i + 1) % 4] ** 2 - self.lens[i] ** 2) / (2 * self.diagonals[i] * self.diagonals[(i + 1) % 4])))
			except: 
				a.append(3 * math.pi / 4)
		return sum(a)
	
	def check(self):
		return abs(rectangle.angle_count(self) - 2 * math.pi) < 0.1
	

def main():
	n = int(input())
	count = 0
	for i in range(n):
		x, y, *other = list(map(int, input().split()))
		res = rectangle(x, y, other)
		if rectangle.check(res): count += 1
	print(count)

main()