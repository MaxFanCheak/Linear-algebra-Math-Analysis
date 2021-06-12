import numpy as np


for n in range(1, 24):
    matrix = [[i + 5 for i in range(n)] for j in range(n)]
    for i in range(n):
        matrix[i][i] = i + 6
    for i in range(n):
        print(*matrix[i])
    if (n < 10):
        print("(n = ", n , " ) numpy.det = ", np.linalg.det(np.array(matrix)))
    else:
        print("(n = ", n , ") numpy.det = ", np.linalg.det(np.array(matrix)))
