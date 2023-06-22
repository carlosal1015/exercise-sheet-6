import numpy as np
from tabulate import tabulate


def F(x: np.ndarray):
    return np.array(
        object=[x[0] ** 2 + x[0] * x[1] - 77, x[0] * x[1] + x[1] ** 2 - 44], dtype=float
    )


def DF(x: np.ndarray):
    return np.array(
        object=[[2 * x[0] + x[1], x[0]], [x[1], x[0] + 2 * x[1]]], dtype=float
    )


N_MAX_ITER = 10
x = np.array(object=[1, 1], dtype=float)
header = [
    [
        "N° de iteración",
        "x^(k)",
        "||h^(k+1)||_oo = ||x^(k + 1) - x^(k)||_oo",
        "|DF(x^(k))|",
    ]
]


def Newton_system(F, DF, x0, tol, nmax):
    pass


if __name__ == "__main__":
    for k in range(N_MAX_ITER):
        x_old = x
        try:
            Jinv = np.linalg.inv(a=DF(x))
            x = x - Jinv @ F(x)
        except:
            x = np.linalg.solve(a=DF(x), b=DF(x) @ x - F(x))

        det = np.linalg.det(a=DF(x))
        error = np.linalg.norm(x=x - x_old, ord=np.inf)
        new_iteration = [k, x, error, det]
        header.append(new_iteration)
        tabla = tabulate(
            header, headers="firstrow", tablefmt="fancy_grid", stralign="center"
        )
        if error < 1e-5:
            break

    print(tabla)
