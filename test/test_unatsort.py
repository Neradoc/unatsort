from unatsort import natsorted
import random

letters = "aqzswxcderfvbgtyhnjukilopm"
data = []

for x in range(10):
	p = "F"
# 	for x in range(random.randint(1,5)):
# 		p += random.choice(letters)
	for x in range(random.randint(1,5)):
		p += str(random.randint(0,9))
	data.append(p)

print(data)
print(sorted(data))
print(natsorted(data))
