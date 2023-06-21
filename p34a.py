import numpy as np


# Implementación del lado derecho
# x'(t) = f( x(t) ) = -(DF(x(t)))F(a)


def f(x):
    # a = np.zeros(shape=(3, 1), dtype=float)
    Fa = np.array(object=[-5, 9, 4], dtype=float).T
    DF_inv = np.array([])
    return np.array([x[1], -x[0] - 0.01 * x[1] - 100 * x[2], x[1] - 1000.0 * x[2]])
