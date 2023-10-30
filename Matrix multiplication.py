import numpy as np
matrix_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix_b = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
matrix_b = np.transpose(matrix_b)
# enumerate method
new_matrix = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

for index_a, i in enumerate(matrix_a):
    for index_b, j in enumerate(matrix_b):
        new_matrix[index_a][index_b] = sum(i * j)

print(new_matrix, end='\n\n')

#List comprehension
new_matrix = [[sum(a * b) for b in matrix_b] for a in matrix_a]
for _ in new_matrix:
    print(_)