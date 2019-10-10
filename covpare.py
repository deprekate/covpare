import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib.patches import Rectangle
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
print("Scaling Factor:", res.x)

x_pos = np.arange(len(file1))

fig = plt.figure(figsize=(12,5))

plt.subplot(4, 1, 1)
plt.bar(x_pos, file1, align='center', color='red',alpha=0.5, width=1)
plt.ylabel(os.path.basename(sys.argv[1]))
plt.title('Coverage Map')

plt.subplot(4, 1, 2)
plt.bar(x_pos, file2, align='center', color='blue', alpha=0.5, width=1)
plt.ylabel(os.path.basename(sys.argv[2]))

plt.subplot(4, 1, 3)
plt.bar(x_pos, file1, align='center', color='red',alpha=0.5, width=1)
plt.bar(x_pos, file2, align='center', color='blue', alpha=0.5, width=1)
plt.ylabel('overlayed')

plt.subplot(4, 1, 4)
plt.bar(x_pos, file1, align='center', color='red',alpha=0.5, width=1)
plt.bar(x_pos, file2 * res.x, align='center', color='blue', alpha=0.5, width=1)
plt.xlabel('Position on Genome')
plt.ylabel('scaled')

#fig.add_patch(rect)
d = (file1 - res.x * file2)
mn = np.mean(d)
sd = np.std(d)
ind = np.where((d > mn+(2*sd)) | (d < mn-(2*sd)))
for loc in ind[0]:
	#fig.patches.extend([Rectangle((loc*10,100),40,30,linewidth=1,edgecolor='r',facecolor='none')])
	plt.gca().add_patch(
			Rectangle(
				(loc-1.1, 0), #x,y
				2, 
				20, 
				linewidth=1,
				edgecolor='r',
				facecolor='none',
				zorder=9
			)
		)



plt.show()
