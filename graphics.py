import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
y1 = x**2  # значения функций
y2 = np.exp(x)
y3 = np.log(x)
y4 = x**3
plt.plot(x, y1, color="blue", label="x^2",marker="o")  # график x**2 синий цвет кружок
plt.plot(x, y2, color="red", label="e^x",marker="x")  # график e^x красный цвет крестик
plt.plot(x, y3, color="green", label="ln(x)",marker="s")  # график ln(x) зеленый цвет квадратик
plt.plot(x, y4, color="purple", label="x^3",marker="^")  # график x^3 фиолетовый цвет треугольник
plt.grid(True)  # добавляем сетку заголовок подпись осей заголовок
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Графики функций")
plt.show()  # отображаем график