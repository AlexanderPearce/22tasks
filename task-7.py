# -*- coding: utf-8 -*-

"""
Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы, а каждое
число внутри равно сумме двух расположенных над ним чисел.
               1
              1 1             
             1 2 1
            1 3 3 1
           1 4 6 4 1
         1 5 10 10 5 1
       1 6 15 20 15 6 1
"""

triangle_matrix = []
n = int(input('Lines number: '))

for i in range(n+1):  # Инициализация квадратной матрицы.
    triangle_matrix.append([1] + [0] * n)

for i in range(1, n+1):
    for j in range(1, i+1):  # Обход до главной диоганали матрици, было range(1, n+1).
        triangle_matrix[i][j] = triangle_matrix[i-1][j] + triangle_matrix[i-1][j-1]

for i in range(0, n+1):  # Вывод матрици до главной диоганали, было range(0, n+1).
    for j in range(0, i+1):
        print(triangle_matrix[i][j], end=' ')
    print()
