curr_zero_count = 0
max_zero_count = 0
sequance = input()
for i in sequance:
	if i == "0": curr_zero_count += 1
	else:
		max_zero_count = max(max_zero_count, curr_zero_count)
		curr_zero_count = 0
max_zero_count = max(max_zero_count, curr_zero_count)
print(max_zero_count)