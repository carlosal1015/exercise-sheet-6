#!/usr/bin/env python

"""Programa Faddeev-LeVerrier.py
https://sci-hub.ru/10.1137/0610040
https://arxiv.org/pdf/2008.04247.pdf
https://avosz.fr/wp-content/uploads/Computational-Methods-for-Linear-Algebra-D.K.Faddeev-2c88ddb0837548a735039428fa89f68cc85cc9a3.pdf
"""

import numpy as np

n = 5  # tamaño de la matriz
I = np.identity(n)
A = np.random.randn(n, n).astype("i8")  # matriz
c = [1, -A.trace()]  # coeficientes del polinomio característico
N = A + c[1] * I  #

for k in range(2, n + 1):
    M = np.matmul(A, N)
    c.append(-M.trace() / k)
    N = M + c[k] * I

print(f"A:\n{A}")
print(f"c:\n{N}")
print(f"M:\n{M}")
