import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
#ax.plot(np.arange(0,5,0.25))
line1, =ax.plot(np.arange(0,5,0.25),'--o',label='line1')#в самом начале где объявляется переменная,обязательно после нее нужна запятая,пиздец как обязательно,ато не будет видно это ебучее окно с подсказкой по названиям осей
#ax.plot(np.arange(0,10,0.5))
line2, =ax.plot(
    np.arange(0,10,0.5),
    ':s',label='line2')
#в самом начале где объявляется переменная,обязательно после нее нужна запятая,пиздец как обязательно,ато не будет видно это ебучее окно с подсказкой по названиям осей
#ax.legend((line1,line2),['Линия2','Линия'],loc='upper right')
ax.legend((line2,line1),[r'$f(x) =a \cdot b+c$',r'$f(x)=k \cdot x+b$'],facecolor='r',framealpha=0.5)
plt.show()