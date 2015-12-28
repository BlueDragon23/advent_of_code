import re

def inc(string):
	if string[-1] == 'z':
		return inc(string[:-1]) + 'a'
	else:
		return string[:-1] + chr(ord(string[-1]) + 1)

'''
Check whether a string contains a run of three consecutive characters
'''
def consec(string, count=1):
	if count == 3:
		return True
	if len(string) < 2:
		return False
	if ord(string[1]) - ord(string[0]) != 1:
		return consec(string[1:])
	else:
		return consec(string[1:], count + 1)

string = "cqjxxzaa"
pattern = r".*(.)\1.*(.)\2.*"
prog = re.compile(pattern)
while 'i' in string or 'o' in string or 'l' in string or not consec(string) or not prog.match(string):
	string = inc(string)
print string