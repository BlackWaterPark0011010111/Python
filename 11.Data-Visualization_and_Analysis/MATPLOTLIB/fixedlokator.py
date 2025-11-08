import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
x=np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))

ax.grid()
ax.xaxis.set_major_locator(FixedLocator([-2,-1,0,1,2,3]))

plt.show()

"""FixedLocator-просто выводит список тех значений которые мы сами хотим видеть"""