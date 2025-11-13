import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(7,4))
ax_3d=fig.add_subplot(projection='3d')

x=np.linspace(0,10,50)
# координата x которая будет менятся от 0 до 10 и будет разбиватся на 50 равных поддиапазонов,отрезков 
z=np.cos(x)
# а Z - вычисляет ксинусоиду на основе предоставленых значений X
ax_3d.plot(x,x,z)
# Для наименования осей
ax_3d.set_xlabel('X')
ax_3d.set_ylabel('Y')
ax_3d.set_zlabel('Z')
plt.show() 