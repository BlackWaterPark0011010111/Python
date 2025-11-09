import matplotlib.pyplot as plt
import numpy as np

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,5))

x = np.linspace(0,2*np.pi,50)

line1, = ax1.plot(x,np.sin(x),'b--o',label='sin(x)')
#если мы определяем label в одной линии
line2, = ax1.plot(x,np.cos(x),'r:s',label='cos(x)')
#то она должна быть и в каждой линии
ax1.legend(
    loc='upper right',
    frameon=True,
    shadow=True,
    fancybox=True,
    facecolor='lightgray',
    edgecolor='black',
    fontsize=10)

#кастомизация
line3, = ax2.plot(x, np.tan(x),'g-^',label='tan(x)')
line4, = ax2.plot(x, np.exp(-x),'m-D',label='exp(-x)')

ax2.legend(loc='lower center',
    bbox_to_anchor=(0.5, -0.2),
    ncol=2,
    title=r'Математические функции',
    title_fontsize=12,
    framealpha=0.8)

plt.tight_layout()
plt.show()