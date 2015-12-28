import re

file_ = open("input_day5")
pattern1 = r".*(..).*\1.*" # r".*[aeiou].*[aeiou].*[aeiou].*"
pattern2 = r".*(.).\1.*" # r".*(.)\1.*"
# pattern3 = r".*(ab|cd|pq|xy).*"
prog1 = re.compile(pattern1)
prog2 = re.compile(pattern2)
# prog3 = re.compile(pattern3)
count = 0
for line in file_:
	if prog1.match(line) and prog2.match(line): # and not prog3.match(line):
		count += 1
print count