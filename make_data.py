import sys
import random

if len(sys.argv) < 2:
	print("usage: python make_data.py NUM_DATA [OFFSET]")
	exit()

if not sys.argv[2]:
	sys.argv[2] = 1
for _ in range(int(sys.argv[1])):
	print(random.random() + int(sys.argv[2]))



