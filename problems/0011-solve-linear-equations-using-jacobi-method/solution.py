import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> np.ndarray:

    x = np.zeros(len(b))

    for k in range(n):

        x_new = np.zeros(len(b))

        for i in range(len(b)):

            sum = 0

            for j in range(len(b)):

                if j != i:
                    sum = sum + A[i][j] * x[j]

            x_new[i] = (1 / A[i][i]) * (b[i] - sum)

        x = x_new

    return x