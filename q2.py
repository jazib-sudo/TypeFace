import jellyfish
from fuzzywuzzy import fuzz
import os
f = open("input_file_path.txt","r")
lines = f.readlines()

inp = "input_string"
code1 = jellyfish.soundex(inp)
res = set()
for line in lines:
	words = line.split(" ")
	
	for word in words:
		code = jellyfish.soundex(word)
		if fuzz.ratio(code1,code)>=95:
			res.add(word)

print(f"words similar to {inp}")
print(res)

		