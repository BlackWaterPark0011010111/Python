import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,4))
ax_3d = fig.add_subplot(projection='3d')

X = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
Y = np.arange(-2 * np.pi, 2 * np.pi, 0.2)

xgrid, ygrid = np.meshgrid(X, Y)

zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

#ax_3d.plot_wireframe(xgrid,ygrid,zgrid)
#ax_3d.plot_surface(xgrid,ygrid,zgrid)
ax_3d.plot_surface(xgrid,ygrid,zgrid,rstride=5, cstride=5, cmap='plasma')
#rstride,cstride--шаг слежования по оси x y. то есть индекс 5- это как мы булем перебирать,с каким шагом,если поставить 2,рисунок будет более градиентный
ax_3d.set_xlabel('X Axis')
ax_3d.set_ylabel('Y Axis')
ax_3d.set_zlabel('Z Axis')
plt.show()