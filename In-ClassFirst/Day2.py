__author__ = 'timaeudg'

import numpy as np
import matplotlib.pyplot as plt

# angles for the walks to use for the direction
angles = np.random.rand(1000)*2*np.pi

xstep_size = np.cos(angles)*1.0
ystep_size = np.sin(angles)*1.0

x = xstep_size.cumsum()
y = ystep_size.cumsum()

plt.plot(x,y)
plt.show()