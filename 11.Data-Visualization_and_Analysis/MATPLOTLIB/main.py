import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#sns.set_theme()
#
#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]
#
#fig, ax = plt.subplots()
#
#ax.scatter(input_values, squares, s=50, c='red', label='points')
#ax.plot(input_values, squares, linewidth=3, label='line')
#
#ax.set_title('Square Numbers', fontsize=30)
#ax.set_xlabel('Value', fontsize=15)
#ax.set_ylabel('Square of Value', fontsize=15)
#ax.tick_params(axis='both', labelsize=12)
#ax.grid(True) # или так можно ax.grid() просто добавляет сетку
#ax.legend()
#plt.show()
"""====================================================================================================================="""
#plt.subplot(2,3,1)
#plt.plot(np.random.random(10))
#plt.subplot(2,3,2)
#plt.plot(np.random.random(10))
#plt.subplot(233)#тоже самое что и с запятыми
#plt.plot(np.random.random(10))
#ax3=plt.subplot(212)
#plt.plot(np.random.random(10))
#plt.grid()
#plt.show()
#plt.figure(figsize=(15, 5))  # Широкая фигура для 3х графиков






# fig=plt.figure(figsize=(7,4))
# #fig= это еще одна фигура, то есть окно
# #если мы пишем еще одну фигуру(окно)  в коде,то будет открываться 2 одновременно
# #plt.figure(figsize=(7,4)) ==а с помощь figure а потом figsize сразу устанавливаем (задаем ) размер окну
# ax1=fig.add_subplot(3,1,3)
# #plt.plot(np.arange(0,5,0.2))











f,ax=plt.subplots(2,2)#по 2 графика в двух строках
f.set_size_inches(10,10)
#f.set_size_inches(10,10) ==f(фигура)==это само окно которое всплывает при запуске программы
f.set_facecolor('#000080')
#set_facecolor('#00FFFF') == тут мы задаем цвет самого всплывающего окна,то есть фон на котором будут графики
ax[0,0].plot(np.arange(0,5,0.2))
#(0,5, 0.2) с расстоянием от 0 и до 5 и с шагом 0.2 
#[0,0]=первая координатная ось
ax[0,0].grid()
#ax[0,0].grid() ==отображение сетки для первого графика через grid()
ax[0,1].plot(np.arange(5,0,-0.2))
#ax[0,1] ==2й график
# plot(np.arange(5,0,-0.2))  == тут мы убывающий строим то есть мы на графике показываем с 5 и в низ к нулю и также убывающий гаш с минусом(-0ю2)
ax[0,1].grid() #сетка для 2-го
plt.show()












#plt.subplot(1, 3, 1)  # 1-й график
#plt.plot([1, 2, 3], [1, 2, 1])
#plt.title("Колонка 1")
#
#plt.subplot(1, 3, 2)  # 2-й график
#plt.plot([1, 2, 3], [2, 1, 2])#пересечение x y,x y,x y
#plt.title("Колонка 2")
#
#plt.subplot(1, 3, 3)  # 3-й график
#plt.plot(np.random.random(10))# рандомный рисунок
#plt.title("Колонка 3")
#
#plt.show()


