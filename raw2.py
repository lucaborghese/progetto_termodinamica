#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


parser = argparse.ArgumentParser()
parser.add_argument("--partnum", help='Particle number', type=int, default=100)
parser.add_argument("--iterations", help='Number of iterations', type=int, default=200)
parser.add_argument("--totalenergy", help='Total Energy of the sample', type=int, default=1)

args = parser.parse_args()


def prepare_animation(bar_container, x, hist_bins, rg, ax):
	
	def animate(frame_number):
        
		curitnum = 0
		while curitnum < args.iterations:

			i = rg.integers(0,args.partnum,1)
			j = rg.integers(0,args.partnum,1)

			if x[i] != 0:
				x[i] = x[i] - 1
				x[j] = x[j] + 1

			curitnum = curitnum + 1

		n, _ = np.histogram(x, hist_bins)
		for count, rect in zip(n, bar_container.patches):
			rect.set_height(count)
		ax.set_ylim(top=(int(max(n) / 100) + 1) * 100)
		return bar_container.patches
	return animate

# np.random.seed(5)

x = np.full((1,args.partnum), 5, dtype=int)[0]
hist_bins = np.linspace(0, 39, 40)
rg = np.random.default_rng()

fig, ax = plt.subplots()
_, _, bar_container = ax.hist(x, hist_bins, lw=1,
                              ec="yellow", fc="green", alpha=1)
ax.set_ylim(top=args.partnum)  # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(fig, prepare_animation(bar_container, x, hist_bins, rg, ax), 50,
                              repeat=False, blit=False, interval=1000)
plt.show()