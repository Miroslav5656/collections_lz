import numpy as np
n = int(input("Введите количество строк N: "))  # кол во строк
m = int(input("Введите количество столбцов M: "))  #кол во столбцов
matl = []  # создаем пустой список для матрицы
for i in range(n):
  r = []
  for j in range(m):
    el = int(input("Введите элемент матрицы: "))
    r.append(el)
  matl.append(r)
mat = np.array(matl)  # преобразуем список в массив numpy
print("Исходная матрица:")
print(mat)
transposed_mat = mat.T  # транспонируем матрицу
print("Транспонированная матрица:")
print(transposed_mat)
if n == m: #считаем определитель квадратных матриц
  do = np.linalg.det(mat)
  dt = np.linalg.det(transposed_mat)
  print("Определитель исходной матрицы:", do)
  print("Определитель транспонированной матрицы:", dt)
  if do == dt:
    print("Сравнение: определители равны")
  else:
    print("Сравнение: определители не равны")
else:
  print("Определитель рассчитывается только для квадратных матриц")