import numpy as np
import matplotlib.pyplot as plt

#y=np.arange(0,5,1)
#x=np.array([a*a for a in y])
#y2=[0,2,3,4,5,7]
#x2=[i+1 for i in y2]
#lines=plt.plot(x,y,x2,y2)
#
#plt.minorticks_on()
#plt.grid( which='major', color= '#444' , linewidth = 1 )
#plt.grid( which='minor', color= '#aaa' , ls = ':')
#plt.show()
##which -- указывает какую сетку будем подключать major\minor?
##linewidth---- какая толщина ветки



fig =plt.figure(figsize=(7,4))#создаем окно
ax=fig.add_subplot()# в ax добавляем координатную ось
plt.figtext(0.05,0.6,'Текст в области окна',fontsize=24,color='red')#размещаем текст в области окна и координаты нужно указывать в пределвх 1,потому что 1- это вся ширина
fig.suptitle('Заголовок')#subtitle---исключительно для заголовка метод
ax.set_xlabel('Ox')#подпись для оси X через set_label
ax.set_ylabel('Yx')#подпись для оси Y через set_label
ax.text(0.5,0.1,'Произвольный текст в координатных осях')
ax.annotate('Аннотация', xy=(0.2, 0.4), xytext=(0.6, 0.7), 
            arrowprops={'facecolor': 'gray', 'shrink': 0.1})
plt.show()

#в ax.text----- размещаем текст в области системы координат. то есть те координаты которые мы записали(0.05 и 0.1)-это координаты 
#которые прокладываются по отношению уже имеющихся координат осей
#annotate--- создает аннотацию----->подробней
#Аннотация -- это просто какая нибудь подпись для элемента графика