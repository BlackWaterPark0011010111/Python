import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
ax.plot(np.arange(1,5,0.25))

ax.xaxis.set_major_locator(MultipleLocator(base=4))
ax.grid()  
plt.show()     
    
"""MultipleLocator = он позволяет задавать шаг между рисочками на оси координат 
и для этого используется параметр base к которому приравнивается значение точнее сколько отрезов мы хотим видеть на оси
(MultipleLocator(base=1)) === значит цифры будут выставляться на 1-цу больше,то есть 1,2,3,......."""