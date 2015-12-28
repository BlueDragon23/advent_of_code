def single_santa():
	file_ = open("input_day3")
	visited = [(0,0)]
	current = (0, 0)
	for line in file_:
		for c in line:
			if c == '>':
				current = (current[0]+1, current[1])
			elif c == '<':
				current = (current[0]-1, current[1])
			elif c == '^':
				current = (current[0], current[1]+1)
			else:
				current = (current[0], current[1]-1)
			if current not in visited:
				visited.append(current)
	print len(visited)

def robo_santa():
	file_ = open("input_day3")
	visited = [(0,0)]
	current_n = (0, 0)
	current_r = (0, 0)
	robot = False
	for line in file_:
		for c in line:
			if robot:
				if c == '>':
					current_r = (current_r[0]+1, current_r[1])
				elif c == '<':
					current_r = (current_r[0]-1, current_r[1])
				elif c == '^':
					current_r = (current_r[0], current_r[1]+1)
				else:
					current_r = (current_r[0], current_r[1]-1)
				if current_r not in visited:
					visited.append(current_r)
			else:
				if c == '>':
					current_n = (current_n[0]+1, current_n[1])
				elif c == '<':
					current_n = (current_n[0]-1, current_n[1])
				elif c == '^':
					current_n = (current_n[0], current_n[1]+1)
				else:
					current_n = (current_n[0], current_n[1]-1)
				if current_n not in visited:
					visited.append(current_n)
			robot = not robot
	print len(visited)