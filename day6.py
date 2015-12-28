import re

file_ = open("input_day6")
# Create the empty array
array = [[0 for x in range(1000)] for x in range(1000)]
pattern = r"(.*) (\d+),(\d+) through (\d+),(\d+)"
prog = re.compile(pattern)
for line in file_:
	result = prog.match(line)
	# Add one to account for inclusiveness
	startCoord = (int(result.group(2)), int(result.group(3)))
	endCoord = (int(result.group(4)) + 1, int(result.group(5)) + 1)
	if result.group(1) == "turn on":
		# turn all the lights on
		for y in range(startCoord[1], endCoord[1]):
			for x in range(startCoord[0], endCoord[0]):
				array[x][y] += 1
	elif result.group(1) == "turn off":
		# turn all the lights off
		for y in range(startCoord[1], endCoord[1]):
			for x in range(startCoord[0], endCoord[0]):
				array[x][y] = max(array[x][y]-1, 0)
	elif result.group(1) == "toggle":
		# toggle the lights
		for y in range(startCoord[1], endCoord[1]):
			for x in range(startCoord[0], endCoord[0]):
				array[x][y] += 2
sum = 0
for row in array:
	for light in row:
		sum += light
print sum