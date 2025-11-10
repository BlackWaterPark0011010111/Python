import numpy as np
import matplotlib.pyplot as plt


#создаем фигуру и координатные оси
fig=plt.figure(figsize=(4,4))
ax=fig.add_subplot()



x=np.arange(0,10)#формируем координату X от 0 и до 9,
ax.step(x,x, '-go')#отображаем этот график как по X так и по Y (от 0 и до 9)
#-go----тип линии,так же мы можем указать как 3-ю переменную :тип линии,цвет и маркер
#ax.step(x,x,where='post')#здесь мы указываем post-как инверсную картину,так же можно прописать 'mid' а по умолчанию используется метод 'pre'


#чтобы передать параметры для двоих графиков:
#ax.step(x,x,where='post',  np.cos(x), '--x', where='mid')
#первый график            второй график

ax.grid()
plt.show()


#стековый график
#Yi(x) = y1(x) + y2(x) + ... + yi(x)


fig=plt.figure(figsize=(4,4))
ax=fig.add_subplot()
x=np.arange(0,10)
y1=np.array([-y**2 for y in x]) + 8
y2=np.array([-y**2 for y in x]) + 8
y3=np.array([-y**2 for y in x]) + 8

ax.stackplot(x,y1,y2,y3)

ax.grid()
plt.show()
