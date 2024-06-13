import random

n_fila = random.randint(3, 10)
n_cols = n_fila

A = [[random.randint(0, 100)for _ in range(n_cols)]for _ in range(n_fila)]

DP = [A[i][i] for i in range(n_fila)]

print("Matriz A:")
for fila in A:
    print (fila)

print("Vector DP: \n", DP)