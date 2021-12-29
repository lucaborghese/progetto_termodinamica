#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--partnum", help='Particle number', type=int, default=100)
parser.add_argument("--iterations", help='Number of iterations', type=int, default=200)
parser.add_argument("--totalenergy", help='Total Energy of the sample', type=int, default=1)

hist_bins = np.linspace(0, 40, 100)
args = parser.parse_args()

# np.random.seed(5)

rg = np.random.default_rng()

x = np.full((1,args.partnum), 5, dtype=int)[0]

curitnum = 0
while curitnum < args.iterations:

	i = rg.integers(0,args.partnum,1)
	j = rg.integers(0,args.partnum,1)

	if x[i] != 0:
		x[i] = x[i] - 1
		x[j] = x[j] + 1

	curitnum = curitnum + 1

fig, ax = plt.subplots()

ax.hist(x)

ax.set(xlim=(0, 20), xticks=np.arange(1, 20),
       ylim=(0, 30), yticks=np.linspace(0, 30, 9))

plt.show()
# print(x)