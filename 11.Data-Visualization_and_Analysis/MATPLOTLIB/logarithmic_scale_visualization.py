import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()

x=np.arange(-10*np.pi,10*np.pi, 0.5)
#ax.semilogy(x,np.sinc(x) * np.exp(-np.abs(x/10)))
ax.loglog(x,np.sinc(x) * np.exp(-np.abs(x/10)))

#ax.set_xscale('symlog',linthresh=2)
ax.grid()
plt.show()

"""# на графике видно, что от -30 до -20 все детали функции
и посторонний глядя на такой график,смотжет понять какие значения
принимает график функции

semilog--- эта функция просто для оси Y

semilogx --- эта функция уже для X оси

и эта функция также настраивается для plot, чтобы plot тоже мог принять алгорифмический масштаб
вот так: мы  эту функцию :
"""
#ax.semilog(x,np.sinc(x) * np.exp(-np.abs(x/10)))
                                   
                                   # перестраиваем на такую:
"""
ax.plot(x,np.sinc(x) * np.exp(-np.abs(x/10)))
ax.set_yscale('log') 
#('log') -----  указываем логарифмический масштаб
#"""