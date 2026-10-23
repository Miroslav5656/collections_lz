import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 4, 100)
x_ints = np.array([1, 2, 3, 4])
y1 = x**2 #значения функций
y2 = np.exp(x)
y3 = np.log(x)
y4 = x**3
y1_ints = x_ints**2 #значения функций в целых точках
y2_ints = np.exp(x_ints)
y3_ints = np.log(x_ints)
y4_ints = x_ints**3
plt.plot(x, y1, color="blue", label="x^2") # график x**2 синий цвет кружок
plt.plot(x_ints, y1_ints, color="blue", marker="o", linestyle="")
plt.plot(x, y2, color="red", label="e^x") #график e^x красный цвет крестик
plt.plot(x_ints, y2_ints, color="red", marker="x", linestyle="")
plt.plot(x, y3, color="green", label="ln(x)") #график ln(x) зеленый цвет квадратик
plt.plot(x_ints, y3_ints, color="green", marker="s", linestyle="")
plt.plot(x, y4, color="purple", label="x^3")#график x^3 фиолетовый цвет треугольник
plt.plot(x_ints, y4_ints, color="purple", marker="^", linestyle="")
plt.grid(True) #добавляем сетку заголовок подпись осей заголовок
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Графики функций")
plt.legend()
plt.show() #отображаем график