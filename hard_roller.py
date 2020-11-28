import numpy as np
import matplotlib.pyplot as plt
from pylab import*
import math
from matplotlib.ticker import LogLocator
import pandas as pd

x_arr = []
y = np.array([1, 8, 7, 11, 8, 8, 3, 3, 14, 10, 2, 19, 20, 14, 9, 8, 13, 7, 10, 13, 4, 18, 10, 5, 5, 18, 6, 10, 9, 2, 15, 1, 18, 6, 2, 17, 1])
print(np.mean(y))

count = 1
for n in y:
    x_arr.append(count)
    count += 1

x = np.array(x_arr)
m, b = np.polyfit(x,y,1)

plt.scatter(x,y)
plt.plot(x, m*x + b, color='green')

plt.xlabel('Roll Count')
plt.ylabel('Roll Valuet')
plt.yticks(np.arange(0,21,1))

plt.show()
