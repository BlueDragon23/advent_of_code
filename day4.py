import hashlib
m = hashlib.md5()
prefix = "ckczppom"
m.update(prefix)
current = 1
testHash = m.copy()
testHash.update(str(current))
while not testHash.digest().startswith("00000"):
	print testHash.digest()
	testHash = m.copy()
	current += 1
	testHash.update(str(current))
print prefix + current