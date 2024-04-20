import numpy as np
import matplotlib.pyplot as plt

# a = np.arange(9)
# print(a)
# a = a.reshape(3, 3)
# print(a)
# b = np.array([[10,2,3],
#              [4,5,6],
#              [7,8,9]])
# c = a @ b
# print(c)

# a = np.arange(15)
# print(f'a = \n{a}')
# a = a.reshape(3,5)
# print(f'a = \n{a}')
# b = a[1:3, 3:5]
# print(f'b = \n {b}')

# x = np.linspace(-np.pi, np.pi, 35)
# y_sen = np.sin(x)
# y_cos = np.cos(x)

# fig, (ax1, ax2) = plt.subplots(2)
# ax1.grid(True)
# ax1.plot(x, y_sen)
# ax1.set(title ='Funções Trigonométricas', ylabel = 'sen(x)')
# ax1.set_xlim(-np.pi, np.pi)

# ax2.grid(True)
# ax2.plot(x, y_cos, color='orange')
# ax2.set(xlabel='Ângulo [rad]', ylabel='cos(x)')
# ax2.set_xlim(-np.pi, np.pi)

# plt.show()

x = np.arange(-np.pi, np.pi, 0.1)
y = np.arange(-np.pi, np.pi, 0.1)

x, y = np.meshgrid(x, y)

f_xy = x**2 + y**2

z = f_xy

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x,y,z, cmap="cool")
plt.show()