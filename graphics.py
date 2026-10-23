import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 4, 100)
xg = np.array([1, 2, 3, 4])
y1 = x**2  # значения функций
y2 = np.exp(x)
y3 = np.log(x)
y4 = x**3
y1g = xg**2  # значения функций в целых точках
y2g = np.exp(xg)
y3g = np.log(xg)
y4g = xg**3
plt.plot(x, y1, color="blue", label="x^2")  # график x**2 синий цвет кружок
plt.plot(xg, y1g, color="blue", marker="o", linestyle="")
plt.plot(x, y2, color="red", label="e^x")  # график e^x красный цвет крестик
plt.plot(xg, y2g, color="red", marker="x", linestyle="")
plt.plot(x, y3, color="green", label="ln(x)")  # график ln(x) зеленый цвет квадратик
plt.plot(xg, y3g, color="green", marker="s", linestyle="")
plt.plot(x, y4, color="purple", label="x^3")  # график x^3 фиолетовый цвет треугольник
plt.plot(xg, y4g, color="purple", marker="^", linestyle="")
plt.grid(True)  # добавляем сетку заголовок подпись осей заголовок
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Графики функций")
plt.legend()
plt.show()  # отображаем график