import matplotlib.pyplot as plt
import numpy as np

fig,ax= plt.subplots()
x=np.array([-3,-2,-1,0,1,1,2,3])#задаем параболу
y=np.array([9,4,1,0,1,1,4,9])#задаем параболу
ax.plot(x,y)                #RGB        #отключаем линии,рисуем точки
ax.plot(x,np.sin(x),color=(1.0,0.2,0.3),linestyle='None', marker='.')#точечная
ax.plot(x, x + 5,color='blue', linestyle='--')#линейная
ax.plot(x, x + 3,color='g',linestyle=':')#линейная
ax.plot(x, np.cos(x), color='0.72', linestyle='-.')#серая штрих-пунктирная
ax.plot(x,x,color="#C1050E",linestyle='--')
plt.show()


#
#fig,ax=plt.subplots()
#x=np.array([-9,-5,-2,-1,0,1,5,9])
#y=np.array([9,5,2,1,0,1,5,9])
#ax.plot(x,y, marker='o')
#ax.plot(0.5 * x, y, marker='>')
#ax.plot(2 * x, y, marker='*')
#plt.grid()
#plt.show()


#x = np.linspace(-3, 3, 100)
#f = x**3 
#f_minus_x = (-x)**3  
#
#plt.subplot(1, 2, 2)
#plt.plot(x, f, linewidth=2)
#plt.plot(x, f_minus_x, '--', linewidth=2)
#plt.legend()
#plt.grid(True)
#
#plt.tight_layout()
#plt.show()

#x = np.linspace(-2, 2, 100)
#f = 2**x  # f(x) = 2ˣ
#f_minus_x = 2**(-x)  # f(-x) = 2⁻ˣ
#
#plt.figure(figsize=(8, 5))
#plt.plot(x, f, label='f(x) = 2ˣ', linewidth=2)
#plt.plot(x, f_minus_x, '--', label='f(-x) = 2⁻ˣ', linewidth=2)
#plt.title('f(x) → f(-x)')
#plt.legend()
#plt.grid(True)
#plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
#plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
#plt.show()











