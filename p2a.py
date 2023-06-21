import numpy as np


def F(x: np.ndarray):
    assert x.shape == (3, 1)

    return np.array(
        object=[x[0] ** 2 + x[0] * x[1] - 77, x[0] * x[1] + x[1] ** 2 - 44], dtype=float
    )


def DF(x):
    return np.array(object=[[2 * x[0] + x[1], x[0]], [x[1], x[0] + 2 * x[1]]])


n = 10
x = np.array([1, 1])

for i in range(n):
    xold = x
    try:
        Jinv = np.linalg.inv(DF(x))
        x = x - Jinv @ F(x)
    except:
        x = np.linalg.solve(DF(x), DF(x) @ x - F(x))
    e = np.linalg.norm(x - xold)
    print(f"En la iteracion {i}: {x}\terror: {e}")
    if e < 1e-5:
        break
