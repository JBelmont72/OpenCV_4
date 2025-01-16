'''
https://www.geeksforgeeks.org/matplotlib-tutorial/?ref=shm
'''
# importing libraries 
import math
import matplotlib.pyplot as plt 
import numpy as np 
x=np.array([0,0.5*math.pi,math.pi,1.5*math.pi,2*math.pi])
# x = np.linspace(0.1, 2 * np.pi, 41) 
y = np.exp(np.sin(x)) 
print(x)
plt.stem(x, y) 
plt.show()

import matplotlib.pyplot as plt 
# data to display on plots 
x = [1, 2, 3, 4, 5, 6, 7, 4,7] 
# This will plot a simple histogram
plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])
# Title to the plot
plt.title("Histogram")
# Adding the legends
plt.legend(["bar"])
plt.show()
