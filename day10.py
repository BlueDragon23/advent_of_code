import re

string = "3113322113"
pattern = r"((\d)\2*)" # Find repeated strings of digits
prog = re.compile(pattern)

for i in range(50):
	new_string = ""
	result = prog.findall(string)
	for item in result:
		new_string += str(len(item[0])) + str(item[0][0])
	string = new_string
print len(string)