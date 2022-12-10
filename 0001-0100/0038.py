def	get_values(n, numbers, curr_player):
	if curr_player == 1:
		if n == 1: return [numbers[0], 0]
		path1 = [sum(i) for i in zip([numbers[0], 0], get_values(n - 1, numbers[1:], 2))]
		path2 = [sum(i) for i in zip([numbers[-1], 0], get_values(n - 1, numbers[:-1], 2))]
		if path1[0] > path2[0]: return path1
		else: return path2
	else:
		if n == 1: return [0, numbers[0]]
		path1 = [sum(i) for i in zip([0, numbers[0]], get_values(n - 1, numbers[1:], 1))]
		path2 = [sum(i) for i in zip([0, numbers[-1]], get_values(n - 1, numbers[:-1], 1))]
		if path1[1] > path2[1]: return path1
		else: return path2

def main():
	n = int(input())
	numbers = [int(x) for x in input().split()]
	values = get_values(n, numbers, 1)
	if values[0] == values[1]: print(0)
	elif values[0] > values[1]: print(1)
	else: print(2)

main()