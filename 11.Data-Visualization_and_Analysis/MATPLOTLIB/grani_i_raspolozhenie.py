import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
ax.plot(np.arange(1,5,0.25))# сама блядь рысочка ебаная на оси 

#функции с помощью которых можно задавать граничные значения
#Задаем минимальные и максимальные значения на осях координат
#ax.set(xlim=(xmin,xmax),ylim=(ymix,ymax))

ax.set(xlim=(-5,30), ylim=(-1,6))
                                #или вот так
#ax.set_xlim(-5,30)
#ax.set_ylim(-1,6)
                                #или вот так можно записать значения:
#ax.set_xlim(xmin=-5,xmax=30)
#ax.set_ylim(ymin=-1,ymax=6)



ax.grid()
plt.show()