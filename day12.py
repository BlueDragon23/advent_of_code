import re
import json

pattern = r"-?\d+"
prog = re.compile(pattern)

file_ = open("input_day12")

'''
sum_ = 0
for line in file_:
	result = prog.findall(line)
	for x in result:
		sum_ += int(x)
print sum_
'''

parsed = json.load(file_)

for x in parsed:
	if "red" not in x:
		# Find all of the numbers in the structure