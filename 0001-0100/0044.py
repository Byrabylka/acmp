def count_arrows(seq):
	count = 0
	if len(seq) < 5: return 0
	for i in range(len(seq) - 4):
		curr_five = seq[i:i+5]
		if curr_five == "<--<<" or curr_five == ">>-->": count += 1
	return count

def main():
	sequance = input()
	print(count_arrows(sequance))

main()