import numpy as np
import matplotlib.pyplot as plt

# Параметры для создания ленты Мёбиуса
r = 1.5  # радиус ленты
width = 1  # ширина ленты

# Углы от 0 до 2*pi
theta = np.linspace(0, 2 * np.pi, 100)
# Параметр t, который изменяется от -1 до 1, чтобы перейти вокруг всей ленты
t = np.linspace(-1, 1, 100)

# Параметрические уравнения для ленты Мёбиуса
X = (r + width * np.outer(t, np.cos(theta / 2))) * np.cos(theta)
Y = (r + width * np.outer(t, np.cos(theta / 2))) * np.sin(theta)
Z = width * np.outer(t, np.sin(theta / 2))

# Создание трехмерного графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение ленты Мёбиуса
ax.plot_surface(X, Y, Z, color='b', edgecolor='none')

# Настройка графика
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Лента Мёбиуса')


# Показать график
plt.show()
