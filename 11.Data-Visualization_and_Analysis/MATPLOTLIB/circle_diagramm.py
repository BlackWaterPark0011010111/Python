import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(6,4))
ax=fig.add_subplot()

vals=[10,40,23,20,7] # всего 100=100%
labels=['Toyota','BMW','Lexus','Audi','Mercedes']
# vals и labels===
# vals= просто набор меток,множество чисел,долей,то есть каждое числоэто доля каждого наименования в переменной labels  и labels - наборзначений для этих меток
ax.pie(vals,labels=labels)


# а можно и так
#exp=(0.1,0.2,0,0,0)
#ax.pie(vals,labels=labels,autopct='%.2f',explode=exp,shadow=True)
# здесь мы говорим,что передаем все параметры переменной vals, все метки в labels, в каком формате будут отображаться значение долей,с точностью до сотых с помощью autopct, explode-- говорит какие доли будут выдвинуты из круговой диаграммы и указываем на какую величину они будут выдвинуты с помощью переменной wxp, и с shadow=True --- показываем тень с которой они будут отображатся
# и отображаем их в качестве круговой диаграммы с функцией pie

ax.grid()
plt.show()
