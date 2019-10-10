import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import random


def align(x, a, b):
	'''
	'''
	return sum(abs(a - x * b))

if len(sys.argv) < 3:
	print("usage: python covpare.py file1 file2")
	exit()

file1 = np.loadtxt(sys.argv[1])
file2 = np.loadtxt(sys.argv[2])

res = minimize(align, 1, args=(file1, file2))
print(res)

x_pos = np.arange(len(file1))

fig = plt.figure()

plt.subplot(4, 1, 1)
plt.bar(x_pos, file1, align='center', color='red',alpha=0.5)


plt.subplot(4, 1, 2)
plt.bar(x_pos, file2, align='center', color='blue', alpha=0.5)

plt.subplot(4, 1, 3)
plt.bar(x_pos, file1, align='center', color='red',alpha=0.5)
plt.bar(x_pos, file2, align='center', color='blue', alpha=0.5)

plt.subplot(4, 1, 4)
plt.bar(x_pos, file1, align='center', color='red',alpha=0.5)
plt.bar(x_pos, file2 * res.x, align='center', color='blue', alpha=0.5)

plt.show()
