import numpy as np

def linDependency(matrix):
    mat = np.array(matrix) #к numpy-матрице
    determinant = np.linalg.det(mat) #вычисляем определитель

    if determinant == 0:
        return True
    else:
        return False

mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 80]
]

print("Исходная матрица:")
for row in mat:
    print(row)

if linDependency(mat):
    print("Столбцы линейно зависимы")
else:
    print("Столбцы линейно независимы")
