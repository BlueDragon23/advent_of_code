file_ = open("input_day8")
code_chars = 0
actual_chars = 0

for line in file_:
	line = line.strip()
	print line + " -> " + eval(line)
	code_chars += len(line)
	# actual_chars += len(eval(line)) # I know you should never do this
	
print "Code length = " + str(code_chars)
print "Evaluated length = " + str(actual_chars)
print "Difference = " + str(code_chars - actual_chars)