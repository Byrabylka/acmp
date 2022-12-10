t1 = [int(x) for x in input().split(':')]
t2 = [int(x) for x in input().split(':')]
digits = [0] * 10
s_start = t1[0] * 3600 + t1[1] * 60 + t1[2]
s_end = t2[0] * 3600 + t2[1] * 60 + t2[2]
for i in range(s_start, s_end + 1):
	h = i // 3600
	digits[h // 10] += 1
	digits[h % 10] += 1
	m = (i - h * 3600) // 60
	digits[m // 10] += 1
	digits[m % 10] += 1
	s = i - h * 3600 - m * 60
	digits[s // 10] += 1
	digits[s % 10] += 1
for i in digits: print(i)