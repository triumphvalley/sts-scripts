import numpy as np
import matplotlib.pyplot as plt

y = np.arange(2004, 2020)
a = np.array([5.4, 5.2, 5.0, 5.0, 5.4, 5.8, 6.4, 6.6, 6.7, 6.6, 6.9, 6.8, 7.1, 7.2, 7.5, 8.1])
u = np.array([0, 4, 4, 4, 1, 4, 2, 4, 3, 11, 6, 44, 4, 1, 4, 2])
t = np.array([0, 4, 233, 5, 4, 197, 5, 231, 285, 278, 39, 62, 33, 1, 239, 166])
u_a = (u / a) * a.mean()

ax = plt.subplot(111)
ax.bar(y-0.1, u, width=0.2, color='b')
ax.bar(y+0.1, u_a, width=0.2, color='r')

plt.show()