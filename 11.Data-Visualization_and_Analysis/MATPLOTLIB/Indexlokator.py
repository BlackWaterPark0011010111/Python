import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import IndexLocator

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
x=np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))

ax.grid()
ax.xaxis.set_major_locator(IndexLocator(base=0.5,offset=0))

plt.show()
"""то есть мы на графике хотим видеть синусоиду в интервале от pi/2
строка 7 до pi с шагом 0.1.   
для локатора Indexlocator с параметро шага =0.5 и смещение 0
то есть мы продвигаемся от наименьшего значения ,от значения pi/2 и с шагом 0.5 
на графике будет видно что он начинается с -1.57, то есть половина pi. и шаг 0.5 по оси X.
-1.57-1.07-0.57-0.7........."""