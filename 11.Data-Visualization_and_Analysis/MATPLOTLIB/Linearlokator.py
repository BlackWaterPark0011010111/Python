import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator

fig=plt.figure(figsize=(7,4))
ax=fig.add_subplot()
ax.plot(np.arange(1,5,0.25))

#lc=NullLocator()
#ax.xaxis.set_major_locator(lc)  или еще вот так чтобы не создавать обьект класса "lc"
ax.xaxis.set_major_locator(LinearLocator(5))
ax.grid()
plt.show()

"""LinearLocator == создан для того чтобы распределить нужное колличество которое мы задаем на строке
11 --ax.xaxis.set_major_locator(LinearLocator(5))   ------ мы задаем 5
. так вот это будет именно то количество  рисочек на выбранной нами оси(xaxis или yaxis)"""