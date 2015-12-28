import re
import pdb

file_ = open("input_day7")
pattern1 = r"(?P<in1>.+) (?P<op>.+) (?P<in2>.+) -> (?P<out>.+)"
pattern2 = r"NOT (?P<in1>.+) -> (?P<out>.+)"
pattern3 = r"(?P<in1>\d+) -> (?P<out>.+)"
prog1 = re.compile(pattern1)
prog2 = re.compile(pattern2)
prog3 = re.compile(pattern3)

# Use a dictionary to track wires
wires = {}
executed = []
filesize = 0
lines = list(file_)
for line in lines:
	filesize += 1
print filesize

while len(executed) != filesize and "a" not in wires:
	for index, line in enumerate(lines):
		if index in executed:
			continue
		result = prog1.match(line)
		if result:
			# Switch on operator
			op = result.group('op')
			if result.group("in1") not in wires:
				continue
			if op == "AND":
				if result.group("in2") not in wires:
					continue
				wires[result.group("out")] = wires[result.group("in1")] & wires[result.group("in2")]
			elif op == "OR":
				if result.group("in2") not in wires:
					continue
				wires[result.group("out")] = wires[result.group("in1")] | wires[result.group("in2")]
			elif op == "RSHIFT":
				wires[result.group("out")] = wires[result.group("in1")] >> int(result.group("in2"))
			elif op == "LSHIFT":
				wires[result.group("out")] = wires[result.group("in1")] << int(result.group("in2"))
			executed.append(index)
			print line
			print wires
			continue
		result = prog2.match(line)
		if result:
			# Invert input
			if result.group("in1") in wires:
				wires[result.group('out')] = ~wires[result.group('in1')]
				executed.append(index)
				print line
				print wires
			continue
		result = prog3.match(line)
		if result:
			# Output = input
			wires[result.group('out')] = int(result.group('in1'))
			executed.append(index)
			print line
			print wires
			continue
print wires["a"]