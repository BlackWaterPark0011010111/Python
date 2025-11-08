import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
ax.plot(np.arange(1,5,0.25))

#lc=NullLocator()
#ax.xaxis.set_major_locator(lc)  или еще вот так чтобы не создавать обьект класса "lc"
ax.xaxis.set_major_locator(NullLocator())
ax.grid()
plt.show()

"""граничные значения благодаря которым можно задавать для оси X и Y

Управление положением меток на координатах оси x и y
для этого в пакете matplotlib есть две функции:
set_major_locator()
                    И
set_minor_locator()
В качестве аргумента в этих функциях выступает класс matplotlib.ticker.Locator

from matplotlib.ticker import NullLocator
...................
.................
...............

lc=NullLocator()
ax.grid()
ax.xaxis.set_major_locator(lc)
                                ИЛИ чтобы не создавать обьект класса
ax.xaxis.set_major_locator(NullLocator())                               
xaxis= объект оси X.
set_major_locator(lc)=мы вызываем эту функцию для объекта xaxis  и в качестве аргумента выступает экземпляр класса NullLocator -lc
NullLocator- используется для сокрытия меток по выбранной оси(X xaxis или Y yaxis) то есть будут горизонтальные линии
Если ввести 

ax.yaxis.set_major_locator(lc)
                                ИЛИ чтобы не создавать обьект класса
ax.yaxis.set_major_locator(NullLocator())                               


то на графике будут вертикальные линии"""