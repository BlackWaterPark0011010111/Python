import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
x=np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))

ax.minorticks_on()
ax.grid(which='major', lw=2)
ax.grid(which='minor' )
ax.xaxis.set_minor_locator(NullLocator())

plt.show()