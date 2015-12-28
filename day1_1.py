def part1():
	file_ = open("input_day1_1")
	floor = 0
	for line in file_:
		for c in line:
			if c == '(':
				floor += 1
			else:
				floor -= 1
	print floor

def part2():
	file_ = open("input_day1_1")
	floor = 0
	position = 1
	for line in file_:
		for c in line:
			if c == '(':
				floor += 1
			else:
				floor -= 1
			if floor == -1:
				print position
				return
			position += 1
	print floor